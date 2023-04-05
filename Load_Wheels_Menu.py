import sqlite3
import re
from Load_Plates_Menu2 import get_sql_plate_data, Do_Car_Sales_Menu2
from Display_Plates_V3 import RegoPlate
from SQL_Utils import get_sql_pictures_all

def create_table_pictures(cursor):

    sql = '''create table pictures ( 
                 picture_index integer,
                 rego_plate text,
                 jurisdiction text,
                 rego_sticker text,
                 iso_publication_date text,
                 page_number integer,
                 magazine text,
                 car_make text,
                 car_model text,
                 description text)'''
    print(sql)
    try:
        cursor.execute(sql)
    except:
        print("failed to create table")
        pass





def open_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def add_pictures( row):

        conn = open_database('../advertisements_indexed.db')
        cursor = conn.cursor()
#        create_table_pictures(cursor)
        master_index1 = 100000
#        picture_index = 1
        sql = 'SELECT MAX(picture_index) FROM pictures'
        print(sql)
        try:
            results = cursor.execute(sql)
            max_index = results.fetchall()
            master_index1 = max_index[0][0]
            master_index1 += 1
        except:
            print("failed to add data")
            pass

        sql = '''insert into pictures (picture_index, rego_plate, jurisdiction,
         rego_sticker, iso_publication_date, page_number, magazine,
                 car_make, car_model, description, model_year, model_code, model_level, trim_level)
                  values
         ({picture_index}, "{rego_plate}", "{jurisdiction}", "{rego_sticker}", 
         "{iso_publication_date}", {page_number}, "{magazine}", 
        "{car_make}", "{car_model}", "{description}", "{model_year}", "{model_code}", "{model_level}", "{trim_level}")'''

        sql = sql.format(picture_index=master_index1, rego_plate=row["rego_plate"],
                        jurisdiction=row["jurisdiction"], rego_sticker=row["rego_sticker"],
                        iso_publication_date=row["iso_publication_date"],
                        page_number=row["page_number"], magazine=row["magazine"],
                        car_make=row["car_make"], car_model=row["car_model"],
                        description=row["description"], model_year=row["model_year"],
                        model_code=row["model_code"],model_level=row["model_level"], trim_level=row["trim_level"])
        print(sql)
        try:
            cursor.execute(sql)
        except:
            print("failed to add data")
            pass
        conn.commit()
        conn.close()


def Menu(Default_Data_Fill):

    Magazine_List = ["Wheels", "Modern Motor", "Wheels Road Tests"]
    print(Magazine_List)
    magazine = input("<Magazine> ")
    Data_Fill  = Do_Car_Sales_Menu2(magazine)
    Data_Fill['magazine'] = magazine
    clues = {
        "rego_plate": 'RAM232',
        "jurisdiction": 'NSW',
        "rego_sticker": 'none',
        "iso_publication_date": '1972-07-01',
        'page_number': "28",
        "description": 'none'
    }

    # for question in must_ask:
    retry = False
    for question in clues:
            print(clues[question])
            answer = input(question + "<" + clues[question] + ">")
            if answer == "":
                Data_Fill[question] = clues[question]
            else:
                Data_Fill[question] = answer

    return Data_Fill

def main():
    Default_Fill = {
                  "master_index": '99999999',
    }

    pics_table = get_sql_pictures_all(connectstring="../advertisements_indexed.db", jurisdiction="all",
                                 publication="all", publication_year="all", car_model="all", car_make="all")
    for pics_record in pics_table:
        print(pics_record[0], pics_record[1], pics_record[2], pics_record[3], pics_record[4], pics_record[5],
              pics_record[6], pics_record[7], pics_record[8], pics_record[9], pics_record[10], pics_record[11],
              pics_record[12], pics_record[13])


    while True:
        Data_Fill = Menu(Default_Fill)
        add_pictures( Data_Fill)
        pics_table = get_sql_pictures_all(connectstring="../advertisements_indexed.db", jurisdiction="all",
                                 publication="all", publication_year="all", car_make="all", car_model="all")
        for pics_record in pics_table:
            print(pics_record[0], pics_record[1], pics_record[2], pics_record[3], pics_record[4], "page", pics_record[5],
                          pics_record[6], pics_record[7], pics_record[8], pics_record[9], pics_record[10],
                          pics_record[11], pics_record[12], pics_record[13])
        plate = Data_Fill["rego_plate"][0:3]
        get_sql_plate_data(plate)



if __name__ == '__main__':
    main()
