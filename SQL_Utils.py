import sqlite3

class Picture(object):

    def __init__(self, picture_index="", rego_plate="", jurisdiction="", rego_sticker="",
                 iso_publication_date="", page_number=0, magazine="",
                 make="", model="", description="",
                 car_year="none", model_code ="",
                 model_level="none",trim_level=""):

        self.picture_index = picture_index
        self.title = rego_plate
        self.jurisdiction = jurisdiction
        self.rego_sticker = rego_sticker
        self.iso_publication_date = iso_publication_date
        self.page_number = page_number
        self.magazine = magazine
        self.make = make
        self.model = model
        self.description = description
        self.year = car_year
        self.model_code = model_code
        self.model_level = model_level
        self.trim_level = trim_level


    def print_picture(self):
        if self.description == "none":
            self.description = ""
        if self.model == "none":
            self.model = ""
        if self.year == "none":
            self.year = ""
        if self.rego_sticker == "none":
            self.rego_sticker = ""
        if self.model_code == "none":
            self.model_code = ""
        if self.model_level == "none":
            self.model_level = ""
        if self.trim_level == "none":
            self.trim_level = ""
        combined_description = ""
        combined_description = self.make + " " + self.model_code + " " + self.model + " " + self.model_level + " " + self.trim_level
#        combined_description = self.make + " " + self.model_code + " " + self.model

        print('{0:6} {1:3} {2:5} {3:4} {4:30} {5:40} {6:24} p{7:3} {8:11} '.format(
            self.title, self.jurisdiction, self.rego_sticker, self.year, combined_description,
            self.description, self.magazine, str(self.page_number), self.iso_publication_date))


def get_sql_pictures_all(**kwargs):
    #  print kwargs
    jurisdiction = kwargs["jurisdiction"]
    connectstring = kwargs["connectstring"]
    publication = kwargs["publication"]
    publication_year = kwargs["publication_year"]
    car_make = kwargs["car_make"]
    car_model = kwargs["car_model"]
    car_plate = kwargs["car_plate"]
    plate_series = car_plate[0:3]
    pics_dict = {}

    if car_plate == "none":
        if car_make == "all":
            car_make_and_model = ""
        else:
            if car_model == "all":
                car_make_and_model = f" car_make = '{car_make}' and"
            else:
                car_make_and_model = f" car_make = '{car_make}' and car_model = '{car_model}' and"

        #     sql = "select * from adverts"
        if jurisdiction == "all" and publication == "all":
            if car_make == "all":
                sql = "select * from pictures "
            else:
                sql = f"select * from pictures where {car_make_and_model[:-3]} "
        elif jurisdiction != "all" and publication == "all":
            sql = f"select * from pictures where {car_make_and_model} jurisdiction = '{jurisdiction}'"
        elif jurisdiction == "all" and publication != "all":
            sql = f"select * from pictures where {car_make_and_model} publication = '{publication}'"
        elif jurisdiction != "all" and publication != "all" and publication_year != "all":
            sql = f"select * from pictures where {car_make_and_model} publication = '{publication}' and iso_advert_date LIKE '{publication_year}%'"
        else:
            sql = f"select * from pictures where {car_make_and_model} jurisdiction = '{jurisdiction}' and publication = '{publication}'"
    else:
        sql = "select * from pictures where rego_plate LIKE '{0}%'".format(plate_series)

#    print("get_sql_pictures_all", sql, kwargs)

    try:
        conn = sqlite3.connect(connectstring)
        cursor = conn.cursor()
        # print('connected!' + connectstring)
        results = cursor.execute(sql)
        pics_table = results.fetchall()
        conn.close()
        for picture in pics_table:
            plate = picture[1]
            jurisdiction = picture[2]
            rego_sticker = picture[3]
            mag_date = picture[4]
            page_number = str(picture[5])
            mag_title = picture[6]
            make = picture[7]
            model = picture[8]
            description = picture[9]
            model_year = picture[10]
            model_code = picture[11]
        #           print(plate, jurisdiction, rego_sticker, model_year, make, model, description, mag_title, mag_date, "page", page_number, model_code)

        for pics_record in pics_table:  # create the picture objects
            new_pic = Picture(picture_index=pics_record[0], rego_plate=pics_record[1],
                              jurisdiction=pics_record[2], rego_sticker=pics_record[3],
                              iso_publication_date=pics_record[4], page_number=pics_record[5],
                              magazine=pics_record[6], make=pics_record[7],
                              model=pics_record[8], description=pics_record[9],
                              car_year=pics_record[10], model_code=pics_record[11],
                              model_level=pics_record[12], trim_level=pics_record[13])
            pics_dict[pics_record[0]] = new_pic

        return pics_dict

    except:
        print("I am unable to connect to the database")
        conn.close()
