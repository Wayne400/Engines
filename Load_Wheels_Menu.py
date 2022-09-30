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



def main():
    pics_table = get_sql_pictures_all(connectstring="../advertisements_indexed.db", jurisdiction="all",
                                 publication="all", publication_year="all")
    for pics_record in pics_table:
        print(pics_record[0], pics_record[1], pics_record[2], pics_record[3], pics_record[4], pics_record[5],
              pics_record[6], pics_record[7], pics_record[8], pics_record[9], pics_record[10], pics_record[11])

    Data_Fill = { "car_make": 'aston martin',
                  "master_index": '99999999',
                  "jurisdiction": 'NSW',
                  "rego_plate": 'ABC123',
                  "rego_sticker": '5-69',
                  "magazine": 'Wheels',
                  "iso_publication_date": '1973-09-01',
                  "page_number": 1,
                  "car_model": 'DB5',
                  "model_code": 'VG',
                  "model_level": 'none',
                  "trim_level": 'none',
                  "model_year": '1949',
                  "description": 'E49 six pack limelight'}                                     # 25 - 28

    while True:

#        dont_ask = {
#            'master_index': '99999999',
#        }
        dont_ask = {
            'Leyland': ['master_index', 'car_make', 'model_code'],
            'Rambler': ['master_index', 'car_make', 'model_code', 'model_level' ],
            'Ford': ['master_index', 'car_make'],
            'Renault': ['master_index', 'car_make', "model_code", "model_level"],
            'Peugeot': ['master_index', 'car_make', "model_code", "model_level"],
            'Rover': ['master_index', 'car_make', "model_level"],
            'Triumph': ['master_index', 'car_make', "model_level"]
        }
        must_ask = {
            "rego_plate": 'RAM232',
            "jurisdiction": 'NSW',
            "rego_sticker": 'none',
            'magazine': "Modern Motor",
            "iso_publication_date": '1971-07-01',
            'page_number': "none",
            'model_year': '1970',
            'car_make': 'No Default',
            "model_code": "none",
            "car_model": "none",
            "model_level": "none",
            "trim_level": "none",
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
            "car_model": ["Falcon"],
            "model_level": ['none'],
            "trim_level": ['none'],
            "description": 'GTHO Phase III'
        }
        Make_Dict = {}
        Model_Dict = {}
        Model_Code = {}
        Trim_Level = {}
        Make_Dict["Rambler"] = ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American",
                        "AMX", "Marlin", "X-Coupe", "Wagon"]
        Trim_Level["Rambler"] = ['330', '440', '660', '770', 'SST']

        Make_Dict["Ford"] = ["Falcon", "Cortina", "Capri"]
        Trim_Level["Ford"] = ['XL', 'XLE', 'GHIA', 'GS', 'GTHO', 'GT', 'Lotus']
        Model_Code["Ford"] = ['XL', 'XM', 'XT', 'XR', 'XT', 'XW', 'XY','XA','XB','XC']

        Make_Dict["Renault"] = ["R4", "R8", "R10", "R12", "R16", "R10S", "10S", "R15", "R17", "1.4", "RXX"]
        Trim_Level["Renault"] = ['GL', 'TL', 'TS', 'Gordini']

        Make_Dict["Peugeot"] = ["403", "403B", "404", "504", "203", "203C"]
        Trim_Level["Peugeot"] = ['none']

        Make_Dict["Rover"] = ["105R", "105S", "2000", "2000TC", "3500", "P5B", "P5", "P5Bcoupe", "P5coupe", "3L", "100"]
        Trim_Level['Rover'] = ["TC", "Coupe", "S"],
        Model_Code["Rover"] = ['MKI', 'MKII', 'MKIII']

        Make_Dict["Triumph"] = ["2000", "2500"]
        Trim_Level['Triumph'] = ["TC", "PI", "S"],
        Model_Code["Triumph"] = ['MKI', 'MKII']

        Make_Dict["Leyland"] = ["P76", "Austin", "Morris", "Mini", "Wolseley"]
        Model_Dict["Austin"] = ["Freeway", "1800", "Tasman", "Kimberly"]
        Model_Dict["Morris"] = ["Marina", "1100", "1300", "1500", "Nomad"]
        Model_Dict["P76"] = ["none"]
        Trim_Level["Leyland"] = ['Super', 'Executive', 'Super Six', 'De Luxe']

        Make_Dict["Volkswagen"] = ["Beetle", "Bug", "Super Bug", "1500", "1600", "Karman Ghia", "Kombi Van", "Camper Van"]
        make_found = False
        car_make = "Wallmeister"
        while make_found == False:
            car_make = input("Car Make?")
            if car_make in dont_ask:
                make_found = True

        # for question in must_ask:
        clues["car_model"] = Make_Dict[car_make]
        clues["trim_level"] = Trim_Level[car_make]
        for question in Data_Fill:
            if question not in dont_ask[car_make]:
                if question == "model_code":
                    clues["model_code"] = Model_Code[car_make]
                print(clues[question])
                answer = input(question + "<" + must_ask[question] + ">")
                if answer == "":
                    answer = must_ask[question]
                if question == "car_model" and answer in Model_Dict:
                    clues["model_level"] = Model_Dict[answer]


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
