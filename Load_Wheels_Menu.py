import sqlite3
import re
from Load_Plates_Menu import get_sql_plate_data
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
        print ("failed to create table")
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
#        print(sql)
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
                 car_make, car_model, description, model_year, model_code)
                  values
         ({picture_index}, "{rego_plate}", "{jurisdiction}", "{rego_sticker}", 
         "{iso_publication_date}", {page_number}, "{magazine}", 
        "{car_make}", "{car_model}", "{description}", "{model_year}", "{model_code}")'''

        sql = sql.format(picture_index=master_index1, rego_plate=row["rego_plate"],
                        jurisdiction=row["jurisdiction"], rego_sticker=row["rego_sticker"],
                        iso_publication_date=row["iso_publication_date"],
                        page_number=row["page_number"], magazine=row["magazine"],
                        car_make=row["car_make"], car_model=row["car_model"],
                        description=row["description"], model_year=row["model_year"],model_code=row["model_code"])
        print(sql)
        try:
            cursor.execute(sql)
        except:
            print("failed to add data")
            pass
        conn.commit()
        conn.close()



def main():
    pics_table = get_sql_pictures_all(connectstring="../advertisements_indexed.db", jurisdiction="all",
                                 publication="all", publication_year="all")
    for pics_record in pics_table:
        print(pics_record[0], pics_record[1], pics_record[2], pics_record[3], pics_record[4], pics_record[5],
              pics_record[6], pics_record[7], pics_record[8], pics_record[9], pics_record[10], pics_record[11])

    Data_Fill = { "master_index": '99999999',
                  "jurisdiction": 'NSW',
                  "rego_plate": 'ABC123',
                  "rego_sticker": '5-69',
                  "magazine": 'Wheels',
                  "iso_publication_date": '1973-09-01',
                  "page_number": 1,
                  "car_make": 'aston martin',
                  "model_code": 'VG',
                  "car_model": 'DB5',
                  "model_year": '1949',
                  "description": 'E49 six pack limelight'}                                     # 25 - 28

    while True:

        dont_ask = {
            'master_index': '99999999',
        }
        must_ask = {
            "rego_plate": 'RAM232',
            "jurisdiction": 'NSW',
            "rego_sticker": 'none',
            'magazine': "Modern Motor",
            "iso_publication_date": '1970-11-01',
            'page_number': "none",
            'model_year': '1970',
            'car_make': 'No Default',
            "model_code": "none",
            "car_model": "none",
            "description": 'none'
        }

        clues = {
            "rego_plate": 'RAM232',
            "jurisdiction": 'NSW',
            "rego_sticker": '2-72',
            'magazine': "Wheels",
            "iso_publication_date": '1972-07-01',
            'page_number': "28",
            'model_year': '1966',
            'car_make': 'Ford',
            "model_code": "XY",
            "car_model": "Falcon",
            "description": 'GTHO Phase III'
        }


        # for question in must_ask:
        for question in Data_Fill:
            if question in must_ask:
                print(clues[question])
                answer = input(question + "<" + must_ask[question] + ">")
                if answer == "":
                    answer = must_ask[question]
            else:
                answer = dont_ask[question]
            Data_Fill[question] = answer

        add_pictures( Data_Fill)
        pics_table = get_sql_pictures_all(connectstring="../advertisements_indexed.db", jurisdiction="all",
                                 publication="all", publication_year="all")
        for pics_record in pics_table:
            print(pics_record[0], pics_record[1], pics_record[2], pics_record[3], pics_record[4], pics_record[5],
                          pics_record[6], pics_record[7], pics_record[8], pics_record[9], pics_record[10],
                          pics_record[11])
        plate = Data_Fill["rego_plate"][0:3]
        get_sql_plate_data(plate)



if __name__ == '__main__':
    main()
