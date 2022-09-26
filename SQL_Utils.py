import sqlite3



def get_sql_pictures_all( **kwargs):
    #  print kwargs
    jurisdiction = kwargs["jurisdiction"]
    connectstring = kwargs["connectstring"]
    publication = kwargs["publication"]
    publication_year = kwargs["publication_year"]

   #     sql = "select * from adverts"
    if jurisdiction == "all"  and publication == "all":
        sql = "select * from pictures"
    elif jurisdiction != "all"  and publication == "all":
        sql = "select * from pictures where jurisdiction = '{}'".format(jurisdiction)
    elif  jurisdiction == "all"  and publication != "all":
        sql = "select * from pictures where publication = '{}'".format(publication)
    elif jurisdiction != "all" and publication != "all" and publication_year != "all":
        sql = "select * from pictures where publication = '{0}' and iso_advert_date LIKE '{1}%'".format(publication, publication_year)
    else:
        sql = "select * from pictures where jurisdiction = '{}' and publication = '{}' ".format(
                     jurisdiction, publication)

    print(sql)

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

