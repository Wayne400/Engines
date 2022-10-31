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

def Do_Car_Sales_Menu(car_make):

    Data_Fill = { "car_make": car_make,
                  "car_model": 'none',
                  "model_code": 'none',
                  "model_level": 'none',
                  "trim_level": 'none',
                  "model_year": 'none',
                  }                                     # 25 - 28

    dont_ask = {
        'Alfa': ['car_make', 'model_code', 'model_level', 'trim_level'],
        'Chrysler': [ 'car_make'],
        'Citroen': [ 'car_make', 'model_code', 'model_level'],
        'Datsun': [ 'car_make', 'model_code', 'model_level', 'trim_level'],
        'Ford': [ 'car_make', 'model_level'],
        'Fiat': [ 'car_make', "model_code", "model_level", "trim_level"],
        'Holden': [ 'car_make', "model_level"],
        'Honda': [ 'car_make', "model_code", "model_level", "trim_level"],
        'Leyland': [ 'car_make', 'model_code'],
        'Mazda': [ 'car_make', "model_code", "model_level", "trim_level"],
        'Mercedes': [ 'car_make', "model_code", "model_level", "trim_level"],
        'Peugeot': [ 'car_make', "model_code", "model_level"],
        'Rambler': [ 'car_make', 'model_code', 'model_level'],
        'Renault': [ 'car_make', "model_code", "model_level"],
        'Rolls Royce': [ 'car_make', "model_code", "model_level", "trim_level"],
        'Rover': [ 'car_make', "model_level"],
        'Toyota': [ 'car_make', "model_code", "model_level", "trim_level"],
        'Triumph': [ 'car_make', "model_level"],
        'Volkswagen': [ 'car_make', 'trim_level', 'model_level']
    }

    must_ask = {
        'Alfa': ['car_model', 'trim_level'],
        'Chrysler': ['car_model', 'model_code', 'model_level', 'trim_level'],
        'Citroen': [ 'car_make', 'model_code', 'model_level'],
        'Datsun': [ 'car_make', 'model_code', 'model_level', 'trim_level'],
        'Ford': ['car_model', 'model_code', 'trim_level'],
        'Fiat': [ 'car_model'],
        'Holden': [ 'car_model','model_code', 'trim_level'],
        'Honda': [ 'car_model', "model_code", "model_level", "trim_level"],
        'Leyland': [ 'car_model', 'model_level', 'trim_level'],
        'Mazda': [ 'car_make', "model_code", "model_level", "trim_level"],
        'Mercedes': [ 'car_make', "model_code", "model_level", "trim_level"],
        'Peugeot': [ 'car_make', "model_code", "model_level"],
        'Rambler': [ 'car_model', 'model_code', 'model_level'],
        'Renault': [ 'car_model', "model_code", "model_level"],
        'Rolls Royce': [ 'car_make', "model_code", "model_level", "trim_level"],
        'Rover': [ 'car_model', "model_level"],
        'Subaru': ['car_model'],
        'Toyota': [ 'car_model', "model_code", "trim_level"],
        'Triumph': ['car_model', "trim_level", "model_code"],
        'Volkswagen': [ 'car_model', 'model_code'],
        'Volvo': [ 'car_model', 'trim_level']
    }


    Make_Dict = {}
    Model_Code = {}
    Model_Level = {}
    Trim_Level = {}
    clues = {}
    clues['model_year'] = '1969'

    Make_Dict["Alfa"] = ['Alfasud','Alfetta']
    Trim_Level["Alfa", "Alfasud"] = [ 'Ti']
    Trim_Level["Alfa", "Alfetta"] = ['none']

    Make_Dict['Chrysler'] = ['Valiant', 'Dodge', 'Centura']
    Model_Code['Chrysler', 'Dodge'] = ['Phoenix', 'Custom 880']
    Model_Code['Chrysler', 'Centura'] = ['KB', 'KC']
    Model_Code['Chrysler', 'Valiant'] = ["R", "S", "AP5", "AP6", "VC", "VE", "VF", "VG", "VH", "VJ", "VK", "CL", "CM"],
    Model_Level['Chrysler', 'Valiant'] = ["Valiant", "Regal", "Safari", "VIP", "Pacer", "Ranger", "Charger"],
    Model_Level['Chrysler', 'Centura'] = ["none"],
    Trim_Level['Chrysler', 'Valiant'] = ["XL", "770", "Drifter", "E31", "E34", "E38", "E48", "E49"],
    Trim_Level['Chrysler', 'Centura'] = ["XL", "GL", "GLX"],

    Make_Dict["Citroen"] = ['GS']
    Trim_Level["Citroen", "DS"] = ['Pallas']
    Trim_Level["Citroen", "GS"] = [ 'Club']

    Make_Dict["Datsun"] = ['180B', '120Y', '1600']

    Make_Dict["Fiat"] = ['124S', '132', '127']

    Make_Dict["Ford"] = ["Falcon", "Cortina", "Capri", "Escort"]
    Trim_Level['Ford', "Falcon"] = ['XL', 'GS', 'GTHO', 'GT']
    Trim_Level['Ford', "Cortina"] = ['Lotus', 'XL', 'XLE']
    Trim_Level['Ford', "Escort"] = ['RS2000', 'GHIA','XL','Little Ripper']
    Model_Code['Ford', "Falcon"] = ['XL', 'XM', 'XT', 'XR', 'XT', 'XW', 'XY', 'XA', 'XB', 'XC']
    Model_Code['Ford', "Cortina"] = ['MKI', 'MKII', 'TC', 'TD', 'TE', 'TF']
    Model_Code['Ford', "Escort"] = ['MKI', 'MKII']

    Make_Dict['Holden'] = ["Standard", "Special", "Kingswood", "Torana", "Premier", "Monaro", "Belmont", "Statesman", "Gemini"]
    Trim_Level['Holden', 'Kingswood'] = ['SL', 'SS']
    Trim_Level['Holden', 'Statesman'] = ['De Ville', 'Caprice', 'none']
    Trim_Level['Holden', 'Monaro'] = ['GTS', 'GTS 327', 'GTS 350']
    Model_Code["Standard"] = ['EJ', 'EH', 'HD', 'HR']
    Model_Code["Special"] = ['EJ', 'EH', 'HD', 'HR']
    Model_Code["Premier"] = ['EJ', 'EH', 'HD', 'HR']
    Model_Code["Brougham"] = ['HK', 'HT', 'HG']
    Model_Code['Holden', 'Kingswood'] = ['HK', 'HT', 'HG', 'HQ', 'HJ', 'HZ']
    Model_Code['Holden', 'Monaro'] = ['HK', 'HT', 'HG', 'HQ', 'HJ', 'HZ']
    Model_Code['Holden', 'Belmont'] = ['HK', 'HT', 'HG', 'HQ', 'HJ', 'HZ']
    Model_Code['Holden', 'Statesman'] = ['HQ', 'HJ', 'HZ', 'WB']
    Model_Code['Holden', 'Torana'] = ['HB', 'LC', 'LH', 'LJ', 'LX', 'UC']
    Trim_Level['Holden', 'Torana'] = ['S', 'SL', 'XU-1', 'SLE', 'SLR/5000']
    Model_Code['Holden', 'Gemini'] = ['TX', 'TC', 'TD', 'TF', 'TG']
    Trim_Level['Holden', 'Gemini'] = ['S', 'SL', 'Coupe']

    Make_Dict["Honda"] = ['s600', 'Civic', 'Z', '1500']

    Make_Dict['Leyland'] = ["P76", "Austin", "Morris", "Mini", "Wolseley"]
    Model_Level['Leyland', "Austin"] = ["Freeway", "1800", "Tasman", "Kimberly"]
    Model_Level['Leyland', "Morris"] = ["Marina", "1100", "1300", "1500", "Nomad"]
    Model_Level['Leyland', "P76"] = ["none"]
    Model_Level['Leyland', "Mini"] = ['850', '1100']
    Trim_Level['Leyland', "Austin"] = ["none"]
    Trim_Level['Leyland', "P76"] = ['Super', 'Executive', 'Super Six', 'De Luxe', 'Targa Florio']
    Trim_Level['Leyland', "Morris"] = ['Super', 'Executive', 'Super Six', 'De Luxe']
    Trim_Level['Leyland', "Mini"] = [ 'Deluxe']

    Make_Dict["Mazda"] = ["RX4", "Capella", "1300", "1800"]

    Make_Dict["Mercedes"] = ["280"]

    Make_Dict["Peugeot"] = ["403", "403B", "404", "504", "203", "203C"]
    Trim_Level["Peugeot"] = ['none']

    Make_Dict["Rambler"] = ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American",
                            "AMX", "Marlin", "X-Coupe", "Wagon"]
    Trim_Level["Hornet"] = ['SST']
    Trim_Level["Javelin"] = ['SST']
    Trim_Level["Ambassador"] = ['SST']
    Trim_Level["Classic"] = ['330', '440', '660', '770']
    Trim_Level["American"] = ['330', '440', '660', '770']

    Make_Dict["Renault"] = ["R4", "R8", "R10", "R12", "R16", "R10S", "10S", "R15", "R17", "1.4", "RXX"]
    Trim_Level["Renault"] = ['GL', 'TL', 'TS', 'Gordini']

    Make_Dict["Rolls Royce"] = ["Silver Shadow"]

    Make_Dict["Rover"] = ["105R", "105S", "2000", "2000TC", "3500", "P5B", "P5", "P5Bcoupe", "P5coupe", "3L", "100"]
    Trim_Level['Rover', 'P5B'] = [ "Coupe", "Sedan"],
    Trim_Level['Rover', '2000'] = ["TC", "S"],
    Model_Code["Rover"] = ['MKI', 'MKII', 'MKIII']
    Model_Code['Rover', '2000'] = ['MKI', 'MKII', 'MKIII']

    Make_Dict["Subaru"] = ["Sedan", "Coupe", "Wagon", "4WD Wagon"]

    Make_Dict["Toyota"] = ['Crown', '1900', 'Corolla', 'Corona', 'Celica']
    Trim_Level["Toyota",'Corona'] = ['SE']
    Trim_Level["Toyota",'Corolla'] = ['SE']
    Trim_Level["Toyota",'Crown'] = ['Super Saloon']
    Model_Code['Toyota', 'Corona'] = ['MKI', 'MKII', 'none']
    Model_Code['Toyota', 'Crown'] = ['none']


    Make_Dict['Triumph'] = ['2000', '2500', '2.5', 'Stag']
    Trim_Level['Triumph', '2.5'] = ["TC", "PI", "S"],
    Trim_Level['Triumph', '2000'] = ["TC"],
    Trim_Level['Triumph', '2500'] = ["TC", "S"],
    Trim_Level['Triumph', 'Stag'] = ['none'],
    Model_Code['Triumph', '2.5'] = ['MKI', 'MKII']
    Model_Code['Triumph', '2000'] = ['MKI', 'MKII']
    Model_Code['Triumph', '2500'] = ['MKI', 'MKII']
    Model_Code['Triumph', 'Stag'] = ['none']

    Make_Dict["Volkswagen"] = ["Beetle", "Bug", "Super Bug", "1200", "1500", "1600", "Karman Ghia", "Kombi Van",
                               "Passat", "Camper Van"]
    Model_Code['Volkswagen', '1200'] = ['Type 1']
    Make_Dict["Volvo"] = ["142", "144", "145", "164", "242", "244" , "245", "264"]
    Trim_Level['Volvo', '244'] = ['DL', 'GL']
    Trim_Level['Volvo', '264'] = ['GL']


    # for question in must_ask:
    clues["car_model"] = Make_Dict[car_make]
    retry = False
    for question in must_ask[car_make]:
            if question == 'model_code':
                # print('model_code', Data_Fill['car_model'])  # stored previously
                clues['model_code'] = Model_Code[car_make, Data_Fill['car_model']]
            if question == 'model_level':
                # print('model_level', Data_Fill['car_model'])
                clues['model_level'] = Model_Level[car_make, Data_Fill['car_model']]
            if question == 'trim_level':
                # print('trim_level', Data_Fill['car_model'] )
                clues['trim_level'] = Trim_Level[car_make, Data_Fill['car_model']]
            print(clues[question])
            answer = input(question + "<" + Data_Fill[question] + ">")
            if answer == "":
                answer = Data_Fill[question]
            if question == "car_model":
                if answer not in Make_Dict[car_make]:
                    print("wally")
                    Data_Fill[question] = 'none'
                else:
                    Data_Fill[question] = answer
            else:
                Data_Fill[question] = answer
    return Data_Fill

def Menu(Default_Data_Fill):


    Make_list = ["Ford", "Leyland", "Peugeot", "Rambler", "Renault", "Rover", "Triumph", "Valiant", "Volkswagen",
                 "x = exit"]
    print(Make_list)
    car_make = input("Car Make?")
    Data_Fill  = Do_Car_Sales_Menu(car_make)
    clues = {
        "rego_plate": 'RAM232',
        "jurisdiction": 'NSW',
        "rego_sticker": 'none',
        'magazine': "Wheels",
        "iso_publication_date": '1972-07-01',
        'page_number': "28",
        "model_year": 'none',
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
                                 publication="all", publication_year="all")
    for pics_record in pics_table:
        print(pics_record[0], pics_record[1], pics_record[2], pics_record[3], pics_record[4], pics_record[5],
              pics_record[6], pics_record[7], pics_record[8], pics_record[9], pics_record[10], pics_record[11])


    while True:
        Data_Fill = Menu(Default_Fill)
        add_pictures( Data_Fill)
        pics_table = get_sql_pictures_all(connectstring="../advertisements_indexed.db", jurisdiction="all",
                                 publication="all", publication_year="all")
        for pics_record in pics_table:
            print(pics_record[0], pics_record[1], pics_record[2], pics_record[3], pics_record[4], "page", pics_record[5],
                          pics_record[6], pics_record[7], pics_record[8], pics_record[9], pics_record[10],
                          pics_record[11])
        plate = Data_Fill["rego_plate"][0:3]
        get_sql_plate_data(plate)



if __name__ == '__main__':
    main()
