import sqlite3



def get_sql_pictures_all( **kwargs):
    #  print kwargs
    jurisdiction = kwargs["jurisdiction"]
    connectstring = kwargs["connectstring"]
    publication = kwargs["publication"]
    publication_year = kwargs["publication_year"]
    car_make = kwargs["car_make"]
    car_model = kwargs["car_model"]

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
    elif  jurisdiction == "all" and publication != "all":
        sql = f"select * from pictures where {car_make_and_model} publication = '{publication}'"
    elif jurisdiction != "all" and publication != "all" and publication_year != "all":
        sql = f"select * from pictures where {car_make_and_model} publication = '{publication}' and iso_advert_date LIKE '{publication_year}%'"
    else:
        sql = f"select * from pictures where {car_make_and_model} jurisdiction = '{jurisdiction}' and publication = '{publication}'"

    print("get_sql_pictures_all", sql, kwargs)

    try:
        conn = sqlite3.connect(connectstring)
        cursor = conn.cursor()
        print('connected!' + connectstring)
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

        return pics_table

    except:
        print("I am unable to connect to the database")
        conn.close()

