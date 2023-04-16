import sqlite3
import re
from Display_Plates_V3 import Advertisement
from SQL_Utils import get_sql_pictures_all

def get_sql_plate_data(plate):
    #  print kwargs

    conn = open_database('../advertisements_indexed.db')

    sql = "select * from adverts where rego_plate LIKE '{0}%'".format( plate)

    print(sql)
    ads = {}

    try:
        cursor = conn.cursor()
        results = cursor.execute(sql)
        ads_dict = results.fetchall()
        conn.close()
        for ads_record in ads_dict:  # we make a lists of database indexes for distinct plate numbers, insert into dictionary
            plate = str(ads_record[1])
            title = ads_record[1]
            jurisdiction = ads_record[2]
            ad_date = ads_record[3]
            publication = ads_record[5]
            make = ads_record[6]
            model = ads_record[7]
            car_year = ads_record[8]
            capacity = ads_record[9]
            colour = ads_record[10]
            phone1 = ads_record[11]
            interior_trim = ads_record[15]
            body_style = ads_record[16]
            trim_level = ads_record[17]
            price = ads_record[18]
            milage = ads_record[19]
            model_code = ads_record[20]
            month = ads_record[21]
            transmission = ads_record[22]
            model_level = ads_record[24]
            ads_master_index = ads_record[0]
            new_ad = Advertisement(ad_index=ads_master_index, title=title, jurisdiction=jurisdiction,
                               make=make, model_code=model_code, trim_level=trim_level,
                               model=model, colour=colour, phone1=phone1,
                               car_year=car_year, capacity=capacity, body_style=body_style,
                               model_level=model_level, interior_trim=interior_trim,
                               month=month, ad_date=ad_date, price=price, milage=milage,
                               transmission=transmission)
            new_ad.set_suburb()
#            new_ad.set_dealer()
#            print("master_index = ", str(ads_master_index))
            ads[ads_master_index] = new_ad

        for old_ads in ads:
            new_ad.set_suburb()
            ads[old_ads].print_ad()

        return ads

    #except:
    except Exception as e:
        print(e)
        print("I am unable to connect to the database")
        conn.close()


def open_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def add_adverts( row):

        conn = open_database('../advertisements_indexed.db')
        cursor = conn.cursor()


        master_index1 = 100000
        sql = 'SELECT MAX(master_index) FROM adverts'
        #print(sql)
        try:
            results = cursor.execute(sql)
            max_index = results.fetchall()
            master_index1 = max_index[0][0]
            master_index1 += 1
        except:
            print("failed to add data")
            pass


        sql = '''insert into adverts (master_index, rego_plate, jurisdiction, iso_advert_date, item_number, publication,
                 car_make, car_model, model_year, capacity, colour, phone1, phone2, dealers_licence, who, interior_trim,
                  body_style, transmission, model_code, model_level, trim_level, price, milage, month,
                   air, VIN, Engine_No, Body_No, Location)
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{transmission}", "{model_code}", "{model_level}", "{trim_level}","{price}", "{milage}", "{month}",
          "{air}", "{VIN}", "{Engine_No}", "{Body_No}", "{Location}")'''

        sql = sql.format(master_index=master_index1, rego_plate=row["rego_plate"],
                        jurisdiction=row["jurisdiction"],
                        iso_advert_date=row["iso_advert_date"],
                        item_number=row["item_number"], publication=row["publication"],
                        car_make=row["car_make"], car_model=row["car_model"], model_year=row["model_year"],
                        capacity=row["capacity"],model_level=row["model_level"],
                        colour=row["colour"], phone1=row["phone1"], phone2="none",
                        dealers_licence=row["dealers_licence"], who=row["who"], interior_trim=row["interior_trim"],
                        body_style=row["body_style"], model_code=row["model_code"], trim_level=row["trim_level"],
                        transmission=row["transmission"], price=row["price"], milage=row["milage"],month=row["month"],
                        air=row["air"],
                        VIN=row["VIN"], Engine_No=row["Engine_No"], Body_No=row["Body_No"],Location=row["Location"])
        print(sql)
        try:
            cursor.execute(sql)
        except:
            print("failed to add data")
            pass
        conn.commit()
        conn.close()

def Do_Car_Sales_Menu2( publication):

    Make_List = ["Datsun", "Ford", "Holden", "Isuzu", "Jaguar", "Leyland", "Peugeot", "Rambler",
                 "Renault", "Rover", "Triumph", "Valiant", "Volkswagen",
                ]

    print(Make_List)
    car_make = input("Car Make?")


    Data_Fill = { "car_make": car_make,
                  "car_model": 'none',
                  "model_code": 'none',
                  "model_level": 'none',
                  "trim_level": 'none',
                  "body_style": 'none',
                  "model_year": 'none',
                  }                                     # 25 - 28

    must_ask = {
        'Citroen': [ 'car_model', 'model_code', 'model_level'],
        'Datsun': [ 'car_model', 'model_level', 'trim_level'],
        'Mazda': [ 'car_model', "model_code", "model_level", "trim_level"],
        'Peugeot': [ 'car_model', "model_code", "model_level"],
        'Renault': [ 'car_model', "trim_level"],
        'Rolls Royce': [ 'car_make', "model_code", "model_level", "trim_level"],
        'Subaru': ['car_model'],
        'Suzuki': ['car_model'],
        'Triumph': ['car_model', "trim_level", "model_code"],
    }

    clues = {}
    Make_Dict = {}
    Model_Code = {}
    Model_Level = {}
    Trim_Level = {}
    Body_Style = {}

    must_ask['Alfa'] = ['car_model', 'trim_level']
    Make_Dict["Alfa"] = ['Alfasud', 'Alfetta', '2600']
    Trim_Level["Alfa", "Alfasud"] = [ 'Ti']
    Trim_Level["Alfa", "Alfetta"] = ['none']
    Trim_Level["Alfa", "2600"] = ['Sprint']

    must_ask['BMW'] = ['car_model', 'trim_level']
    Make_Dict["BMW"] = ['2002', '318']
    Trim_Level["BMW", "2002"] = ['none']

    must_ask['Chrysler'] = ['car_model', 'model_code', 'model_level', 'trim_level'],
    Make_Dict['Chrysler'] = ['Valiant', 'Dodge', 'Centura', 'Royal']
    Model_Code['Chrysler', 'Dodge'] = ['Phoenix', 'Custom 880']
    Model_Code['Chrysler', 'Centura'] = ['KB', 'KC']
    Model_Code['Chrysler', 'Royal'] = ['AP1','AP2','AP3']
    Model_Code['Chrysler', 'Valiant'] = ["R", "S", "AP5", "AP6", "VC", "VE", "VF", "VG", "VH", "VJ", "VK", "CL", "CM"],
    Model_Level['Chrysler', 'Valiant'] = ["Valiant", "Regal", "Safari", "VIP", "Pacer", "Ranger", "Charger"],
    Model_Level['Chrysler', 'Centura'] = ["none"],
    Model_Level['Chrysler', 'Royal'] = ["none"],
    Trim_Level['Chrysler', 'Valiant'] = ["XL", "770", "Drifter", "E31", "E34", "E38", "E48", "E49"],
    Trim_Level['Chrysler', 'Centura'] = ["XL", "GL", "GLX"],
    Trim_Level['Chrysler', 'Royal'] = ["none"],

    Make_Dict["Citroen"] = ['GS']
    Trim_Level["Citroen", "DS"] = ['Pallas']
    Trim_Level["Citroen", "GS"] = [ 'Club']

    Make_Dict['Datsun'] = ['180B', '120Y', '1600', '240Z', 'Bluebird']
    Model_Level['Datsun', "Bluebird"] = ["1300"]
    Model_Level['Datsun', "180B"] = ["180B"]
    Trim_Level['Datsun','1300'] = ['SS']
    Trim_Level['Datsun','180B'] = ['SSS']

    must_ask['Fiat'] = ['car_model','body_style']
    Make_Dict["Fiat"] = ['124', '124S', '125', '127', '128', '132', '500', '850', '1100', '2300']
    Body_Style['Fiat', '124'] = ["Sedan", "Station Wagon", "Coupe"],
    Body_Style['Fiat', '124S'] = ["Sedan", "Station Wagon", "Coupe"],
    Body_Style['Fiat', '125'] = ["Sedan", "Station Wagon", "Coupe"],
    Body_Style['Fiat', '127'] = ["Sedan", "Station Wagon", "Coupe"],
    Body_Style['Fiat', '128'] = ["Sedan", "Station Wagon", "Coupe"],
    Body_Style['Fiat', '132'] = ["Sedan", "Station Wagon", "Coupe"],
    Body_Style['Fiat', '500'] = ["Sedan"],
    Body_Style['Fiat', '850'] = ["Sedan", "Coupe"],
    Body_Style['Fiat', '1100'] = ["Sedan", "Station Wagon", "Coupe"],
    Body_Style['Fiat', '2300'] = ["Sedan", "Station Wagon", "Coupe"],

    must_ask['Ford'] = ['car_model', 'model_code', 'trim_level','body_style']
    Make_Dict["Ford"] = ["Falcon", "Futura", "Fairlane", "Cortina", "Capri", "Escort", "Fairmont", "Landau", "Zephyr", "Customline", "Galaxie"]
    Trim_Level['Ford', "Falcon"] = ['XL', 'GS', 'GTHO', 'GT', '250', '500', 'Grand Sport Rally']
    Trim_Level['Ford', "Futura"] = ['XL', 'GS', 'GT', '500']
    Trim_Level['Ford', "Fairlane"] = [ 'GS', '500']
    Trim_Level['Ford', "Galaxie"] = [ 'GS', '500']
    Trim_Level['Ford', "Fairmont"] = ['XL', 'GS', 'none', 'GT']
    Trim_Level['Ford', "Capri"] = ['XL', 'GT']
    Trim_Level['Ford', "Landau"] = [ 'none']
    Trim_Level['Ford', "Customline"] = [ 'none']
    Trim_Level['Ford', "Cortina"] = ['Lotus', 'XL', 'XLE', '440']
    Trim_Level['Ford', "Escort"] = ['RS2000', 'GHIA','XL','Little Ripper']
    Trim_Level['Ford', "Zephyr"] = ['XL']
    Trim_Level['Ford', "none"] = ['XL', 'GS', 'L']
    Model_Code['Ford', "Falcon"] = ['XL', 'XM', 'XP', 'XT', 'XR', 'XT', 'XW', 'XY', 'XA', 'XB', 'XC']
    Model_Code['Ford', "Futura"] = ['XL', 'XM', 'XP', 'XT', 'XR', 'XT', 'XW', 'XY', 'XA', 'XB', 'XC']
    Model_Code['Ford', "none"] = ['XL', 'XM', 'XP', 'XT', 'XR', 'XT', 'XW', 'XY', 'XA', 'XB', 'XC']
    Model_Code['Ford', "Fairlane"] = [ 'ZA', 'ZB', 'ZC', 'ZD', 'ZF', 'ZG', 'ZH']
    Model_Code['Ford', "Galaxie"] = [ 'none']
    Model_Code['Ford', "Fairmont"] = [ 'XP', 'XT', 'XR', 'XT', 'XW', 'XY', 'XA', 'XB', 'XC']
    Model_Code['Ford', "Landau"] = [ 'P5']
    Model_Code['Ford', "Customline"] = [ 'none']
    Model_Code['Ford', "Cortina"] = ['MKI', 'MKII', 'TC', 'TD', 'TE', 'TF']
    Model_Code['Ford', "Capri"] = ['MKI', 'MKII']
    Model_Code['Ford', "Escort"] = ['MKI', 'MKII']
    Model_Code['Ford', "Zephyr"] = ['MKI', 'MKII', 'MKIII']
    Body_Style['Ford', 'Falcon'] = ["Panel Van", "Sedan", "Utility", "Station Wagon","Coupe"],
    Body_Style['Ford', 'Futura'] = ["Panel Van", "Sedan", "Utility", "Station Wagon","Coupe"],
    Body_Style['Ford', 'none'] = ["Panel Van", "Sedan", "Utility", "Station Wagon","Coupe"],
    Body_Style['Ford', 'Fairmont'] = ["Panel Van", "Sedan", "Utility", "Station Wagon", "Coupe"],
    Body_Style['Ford', 'Escort'] = ["Panel Van", "Sedan", "Coupe"],
    Body_Style['Ford', 'Customline'] = ["Panel Van", "Sedan", "Utility", "Station Wagon", "Coupe"],
    Body_Style['Ford', 'Fairlane'] = ["Sedan", "Station Wagon", "Coupe"],
    Body_Style['Ford', 'Cortina'] = ["Sedan", "Station Wagon"],
    Body_Style['Ford', 'Galaxie'] = ["Sedan", "Station Wagon"],
    Body_Style['Ford', 'Capri'] = ["Coupe"],



    must_ask['Holden'] = ['car_model', 'model_code', 'trim_level', 'body_style']
    Make_Dict['Holden'] = ["Standard", "Special", "Kingswood", "Torana", "Premier", "Monaro", "Belmont", "Statesman", "Gemini", "Brougham"]
    Trim_Level['Holden', 'Kingswood'] = ['SL', 'SS']
    Trim_Level['Holden', 'Statesman'] = ['De Ville', 'Caprice', 'none']
    Trim_Level['Holden', 'Brougham'] = ['De Ville', 'Caprice', 'none']
    Trim_Level['Holden', 'none'] = ['S', 'SL']
    Trim_Level['Holden', 'Special'] = ['none']
    Trim_Level['Holden', 'Torana'] = ['S', 'SL', 'GTR', 'GTR XU-1', 'SLE', 'SLR/5000']
    Trim_Level['Holden', 'Monaro'] = ['S', 'SS', 'GTS', 'GTS 350', 'GTS 327']
    Trim_Level['Holden', 'Premier'] = ['S', 'SS']
    Trim_Level['Holden', 'Statesman'] = ['Deville']
    Trim_Level['Holden', 'Belmont'] = ['S', 'SL']
    Trim_Level['Holden', 'Gemini'] = ['S', 'SL', 'Coupe']
    Model_Code['Holden','none'] = ['FE', 'FC', 'FB', 'EK', 'EJ', 'EH', 'HD', 'HR', 'HK', 'HT', 'HG', 'HQ', 'HJ', 'HZ']
    Model_Code['Holden','Standard'] = ['EJ', 'EH', 'HD', 'HR']
    Model_Code['Holden','Special'] = ['FE', 'FC', 'FB', 'EK', 'EJ', 'EH', 'HD', 'HR']
    Model_Code['Holden', 'Premier'] = ['EJ', 'EH', 'HD', 'HR','HK','HT','HG','HJ','HZ']
    Model_Code['Holden', 'Brougham'] = ['HK', 'HT', 'HG']
    Model_Code['Holden', 'Kingswood'] = ['HK', 'HT', 'HG', 'HQ', 'HJ', 'HZ']
    Model_Code['Holden', 'Monaro'] = ['HK', 'HT', 'HG', 'HQ', 'HJ', 'HZ']
    Model_Code['Holden', 'Belmont'] = ['HK', 'HT', 'HG', 'HQ', 'HJ', 'HZ']
    Model_Code['Holden', 'Statesman'] = ['HQ', 'HJ', 'HZ', 'WB']
    Model_Code['Holden', 'Torana'] = ['HB', 'LC', 'LH', 'LJ', 'LX', 'UC']
    Model_Code['Holden', 'Gemini'] = ['TX', 'TC', 'TD', 'TF', 'TG']
    Model_Level['Holden', 'Torana'] = ["1200", "1300", "1760", "1600", "2250","2600", "2850", "3300"],
    Model_Level['Holden', 'Monaro'] = ["186S", "308", "350"],
    Model_Level['Holden', 'Kingswood'] = ["186", "202", "253"],
    Model_Level['Holden', 'Premier'] = [ "202", "253", "308"],
    Model_Level['Holden', 'Brougham'] = [ "307", "308"],
    Model_Level['Holden', 'none'] = ["none"],
    Model_Level['Holden', 'Belmont'] = ["none"],
    Model_Level['Holden', 'Special'] = ["none"],
    Body_Style['Holden', 'Kingswood'] = ["Panel Van", "Sedan", "Utility", "Station Wagon"],
    Body_Style['Holden', 'Special'] = ["Panel Van", "Sedan", "Utility", "Station Wagon"],
    Body_Style['Holden', 'Premier'] = ["Sedan", "Station Wagon"],
    Body_Style['Holden', 'Brougham'] = ["Sedan"],
    Body_Style['Holden', 'Statesman'] = ["Sedan"],
    Body_Style['Holden', 'Monaro'] = ["Coupe"],
    Body_Style['Holden', 'Torana'] = ["Sedan", "4door", "2door", "Coupe"],
    Body_Style['Holden', 'none'] = ["Panel Van", "Sedan", "Utility", "Station Wagon"],
    Body_Style['Holden', 'Belmont'] = ["Panel Van", "Sedan", "Utility", "Station Wagon"],

    must_ask['Honda'] = ['car_model']
    Make_Dict["Honda"] = ['n360', 's600', 'Civic', 'Z', '1500']

    must_ask['Isuzu'] = ['car_model', 'model_level', 'trim_level']
    Make_Dict['Isuzu'] = ['Bellett']
    Model_Level['Isuzu', 'Bellett'] = ["1500"]
    Trim_Level['Isuzu', 'Bellett'] = ['none']

    must_ask['Jaguar'] = ['car_model']
    Make_Dict['Jaguar'] = ["XJ6", "420", "Mk.I", "Mk.II", "Mk.VII", "S-TYPE", "Mk.X", "420G", "E-Type", "XJS"]

    must_ask['Lancia'] = ['car_model', 'model_level']
    Make_Dict['Lancia'] = ['Fulvia']
    Model_Level['Lancia', 'Fulvia'] = ['2C']

    must_ask['Leyland'] = ['car_model', 'model_level', 'trim_level']
    Make_Dict['Leyland'] = ["P76", "Austin", "Morris", "Mini", "Wolseley"]
    Model_Level['Leyland', "Austin"] = ["Freeway", "1800", "Tasman", "Kimberly"]
    Model_Level['Leyland', "Morris"] = ["Marina", "1100", "1300", "1500", "Nomad"]
    Model_Level['Leyland', "P76"] = ["none"]
    Model_Level['Leyland', "Mini"] = ['850', '1100']
    Trim_Level['Leyland', "Austin"] = ["none"]
    Trim_Level['Leyland', "P76"] = ['Super', 'Executive', 'Super Six', 'De Luxe', 'Targa Florio']
    Trim_Level['Leyland', "Morris"] = ['Super', 'Executive', 'Super Six', 'De Luxe', '262 Super']
    Trim_Level['Leyland', "Mini"] = [ 'Deluxe', 'Cooper S']

    Make_Dict["Mazda"] = ["RX4", "Capella", "1300", "1800"]

    must_ask['Mercedes'] = ['car_model', 'trim_level']
    Make_Dict["Mercedes"] = ["220","280"]
    Trim_Level['Mercedes', '280'] = ['SE','E']
    Trim_Level['Mercedes', '220'] = ['SE']

    must_ask['Mitsubishi'] = ['car_model', 'trim_level']
    Make_Dict["Mitsubishi"] = ['Lancer', 'Colt', 'Galant']
    Trim_Level['Mitsubishi', 'Lancer'] = ['GL']
    Trim_Level['Mitsubishi', 'Galant'] = ['GL']

    must_ask['Oldsmobile'] = ['car_model']
    Make_Dict['Oldsmobile'] = ['Toronado']

    Make_Dict["Peugeot"] = ["403", "403B", "404", "504", "203", "203C"]
    Trim_Level["Peugeot"] = ['none']

    must_ask['Pontiac'] = ['car_model']
    Make_Dict['Pontiac'] = ['Parisienne']


    must_ask['Rambler'] = ['car_model', 'trim_level']
    Make_Dict['Rambler'] = ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American",
                            "AMX", "Marlin", "X-Coupe", "Wagon"]
    Trim_Level['Rambler','Hornet'] = ['SST']
    Trim_Level['Rambler','Javelin'] = ['SST']
    Trim_Level['Rambler','AMX'] = ['none']
    Trim_Level['Rambler','Ambassador'] = ['SST']
    Trim_Level['Rambler', 'Classic'] = ['330', '440', '660']
    Trim_Level['Rambler','American'] = ['330', '440', '660', '770']
    Trim_Level['Rambler','Rebel'] = ['770', 'SST']
    Trim_Level['Rambler','Matador'] = ['SST']

    Make_Dict["Renault"] = ["R4", "R8", "R10", "R12", "R16", "R10S", "10S", "R15", "R17", "1.4", "RXX"]
    Trim_Level['Renault', 'R8'] = ['GL', 'TL', 'TS', 'Gordini', 'none']
    Trim_Level['Renault', 'R10'] = ['Gordini', 'none']
    Trim_Level['Renault', 'R12'] = ['GL', 'TL', 'TS', 'none']
    Trim_Level['Renault', 'R16'] = ['TL', 'TS', 'Gordini']

    Make_Dict["Rolls Royce"] = ["Silver Shadow"]

    must_ask['Rootes'] = ['car_model', 'model_level', 'model_code','trim_level']
    Make_Dict['Rootes'] = ["Hillman", 'Humber', 'Singer']
    Model_Level['Rootes', 'Hillman'] = ['Minx', 'Hunter', 'Imp', 'Hustler', 'Arrow']
    Model_Level['Rootes', 'Humber'] = ['Vogue', 'Super Snipe', 'Hawk']
    Trim_Level['Rootes', 'Hillman'] = ['Deluxe', 'Safari', 'Royal']
    Trim_Level['Rootes', 'Humber'] = ['Deluxe']
    Model_Code['Rootes', "Humber"] = ['Series 1', 'Series 2', 'Series 3', 'Series 4']
    Model_Code['Rootes', "Hillman"] = ['Series 1', 'Series 2', 'Series 3', 'Series 4']

    must_ask['Rover'] = ['car_model', 'trim_level', 'model_code', 'body_style']
    Make_Dict['Rover'] = ["105R", "105S", "2000", "2000TC", "3500", "P5B", "P5", "P5Bcoupe", "P5coupe", "3L", "100","Range Rover"]
    Trim_Level['Rover', 'P5B'] = [ "none"],
    Body_Style['Rover', 'P5B'] = [ "Coupe", "Sedan"],
    Trim_Level['Rover', 'P5'] = [ "none"],
    Body_Style['Rover', 'P5'] = [ "Coupe", "Sedan"],
    Trim_Level['Rover', '3L'] = [ "Coupe", "Sedan"],
    Body_Style['Rover', '3L'] = [ "none"],
    Trim_Level['Rover', '2000'] = ["TC", "S"],
    Trim_Level['Rover', '2000'] = ["none"],
    Trim_Level['Rover', 'Range Rover'] = ['none'],
    Model_Code["Rover", "P5"] = ['MKI', 'MKII', 'MKIII']
    Model_Code["Rover", "P5B"] = ['MKI', 'MKII', 'MKIII']
    Model_Code["Rover", "3L"] = ['MKI', 'MKII', 'MKIII']
    Model_Code['Rover', '2000'] = ['MKI', 'MKII', 'MKIII']
    Model_Code['Rover', 'Range Rover'] = ['none']

    must_ask['Simca'] = ['car_model']
    Make_Dict["Simca"] = ['none','Aronde']

    must_ask['Studebaker'] = ['car_model']
    Make_Dict["Studebaker"] = ['Lark','Cruiser']



    Make_Dict["Subaru"] = ["Sedan", "Coupe", "Wagon", "4WD Wagon"]
    Make_Dict["Suzuki"] = ['LJ50']

    must_ask['Toyota'] = ['car_model', 'trim_level']
    Make_Dict["Toyota"] = ['Crown', '1900', 'Corolla', 'Corona', 'Celica', 'Corona MKII']
    Trim_Level["Toyota", 'Corona'] = ['SE']
    Trim_Level["Toyota", 'Corolla'] = ['SE']
    Trim_Level["Toyota", 'Celica'] = ['LT']
    Trim_Level["Toyota", 'Crown'] = ['Super Saloon', 'SE', 'Six']
    Model_Code['Toyota', 'Corona'] = ['MKI', 'MKII', 'none']
    Model_Code['Toyota', 'Crown'] = ['none']
    Model_Code['Toyota', 'Celica'] = ['none']


    Make_Dict['Triumph'] = ['2000', '2500', '2.5', 'Stag', 'Spitfire', 'GT6']
    Trim_Level['Triumph', '2.5'] = ["TC", "PI", "S"],
    Trim_Level['Triumph', '2000'] = ["TC"],
    Trim_Level['Triumph', '2500'] = ["TC", "S"],
    Trim_Level['Triumph', 'GT6'] = ['none'],
    Trim_Level['Triumph', 'Stag'] = ['none'],
    Model_Code['Triumph', '2.5'] = ['MKI', 'MKII']
    Model_Code['Triumph', '2000'] = ['MKI', 'MKII']
    Model_Code['Triumph', '2500'] = ['MKI', 'MKII']
    Model_Code['Triumph', 'GT6'] = ['MKI', 'MKII', 'MKIII']
    Model_Code['Triumph', 'Stag'] = ['none']

    must_ask['Vauxhall'] = ['car_model', 'model_code']
    Make_Dict["Vauxhall"] = ['Viva', 'Cresta','Victor','Unknown']
    Model_Code["Vauxhall", 'Viva'] = ['PB', 'PC', 'none']
    Model_Code["Vauxhall", 'Cresta'] = ['PA', 'PB', 'PC', 'none']
    Model_Code["Vauxhall", 'Victor'] = ['F', 'FB', 'VX4/90 ', 'none']

    must_ask['Volkswagen'] = ['car_model', 'model_code', 'trim_level']
    Make_Dict["Volkswagen"] = ["Beetle", "Bug", "Superbug", "1200", "1300", "1500", "1600", "Karman Ghia", "Kombi",
                               "Passat"]
    Model_Code['Volkswagen', '1200'] = ['Type 1']
    Trim_Level['Volkswagen', '1200'] = ['Deluxe']
    Model_Code['Volkswagen', '1300'] = ['Type 1']
    Trim_Level['Volkswagen', '1300'] = ['DeLuxe']
    Trim_Level['Volkswagen', '1500'] = ['DeLuxe']
    Model_Code['Volkswagen', '1500'] = ['Type 1']
    Model_Code['Volkswagen', '1600'] = ['Type 3']
    Trim_Level['Volkswagen', '1600'] = ['DeLuxe']
    Model_Code['Volkswagen', 'Beetle'] = ['Type 1']
    Trim_Level['Volkswagen', 'Beetle'] = ['DeLuxe']
    Model_Code['Volkswagen', 'Kombi'] = ['Type 2']
    Trim_Level['Volkswagen', 'Kombi'] = ['MicroBus', 'Camper', 'Van']
    Model_Code['Volkswagen', 'Superbug'] = ['Type 1']
    Trim_Level['Volkswagen', 'Superbug'] = ['DeLuxe']
    Model_Code['Volkswagen', 'Passat'] = ['none', 'Sedan', 'Wagon']
    Trim_Level['Volkswagen', 'Passat'] = ['DeLuxe']

    must_ask['Volvo'] = ['car_model', 'trim_level']
    Make_Dict["Volvo"] = ["122", "142", "144", "145", "164", "242", "244" , "245", "264"]
    Trim_Level['Volvo', '122'] = ['S']
    Trim_Level['Volvo', '145'] = ['E']
    Trim_Level['Volvo', '244'] = ['DL', 'GL']
    Trim_Level['Volvo', '264'] = ['GL']


    if publication == "smh" or publication == "age"  or publication == "FarmWrecksFacebook": # Not Unique or Just Cars
 #       must_ask[car_make].append('body_style')
 #       must_ask[car_make].append('transmission')
 #       must_ask[car_make].append('capacity')
 #       must_ask[car_make].append('colour')
 #       must_ask[car_make].append('interior_trim')
 #       clues['body_style'] = 'Coupe'
        clues['transmission'] = 'Man'
        clues['capacity'] = ['V8', '6cyl', '4.3', '258']
        clues['colour'] = 'Green'
        clues['interior_trim'] = 'Red Leather'
        for key, value in clues.items():
          #  print(key,car_make)
            must_ask[car_make].append(key)
            if key == 'colour':
                Data_Fill[key] = 'unknown'
            else:
                Data_Fill[key] = 'none'
        Data_Fill['VIN'] = 'none'
        Data_Fill['Engine_No'] = 'none'
        Data_Fill['Body_No'] = 'none'
        Data_Fill['Location'] = 'none'
        Data_Fill['air'] = 'none'  # Mascot Motors ads

    clues["car_model"] = Make_Dict[car_make]  # must_ask["car_model"] is prefilled in Make Data above
    # for question in must_ask:
    must_ask[car_make].append('model_year')
    clues['model_year'] = '1969'




    for question in must_ask[car_make]:
    #for question in Data_Fill[car_make]:
            if question == 'model_code':
                # print('model_code', Data_Fill['car_model'])  # stored previously
                clues['model_code'] = Model_Code[car_make, Data_Fill['car_model']]
            elif question == 'model_level':
                # print('model_level', Data_Fill['car_model'])
                clues['model_level'] = Model_Level[car_make, Data_Fill['car_model']]
            elif question == 'trim_level':
                # print('trim_level', Data_Fill['car_model'] )
                clues['trim_level'] = Trim_Level[car_make, Data_Fill['car_model']]
            elif question == 'body_style':
                clues['body_style'] = Body_Style[car_make, Data_Fill['car_model']]

            print(clues[question])
            answer = input(question + "<" + Data_Fill[question] + ">")
            if answer == "":
                answer = Data_Fill[question]
            if question == "car_model":
                if answer not in Make_Dict[car_make]:
                  #  print("wally")
                    Data_Fill[question] = 'none'
                else:
                    Data_Fill[question] = answer
            else:
                Data_Fill[question] = answer
    return Data_Fill

def Menu(Default_Data_Fill):

    Publication_List = ["smh", "age", "Just Cars", "Unique Cars","FarmWrecksFacebook"]
    print(Publication_List)
    publication = input("Publication?")

    Data_Fill = Do_Car_Sales_Menu2(publication)
    Data_Fill['publication'] = publication
    must_ask = {}
    clues = {}
    if publication == "smh" or publication == "age" or publication == "FarmWrecksFacebook":
      must_ask = {
                  "rego_plate": 'ABC123',
                  "jurisdiction": 'NSW',
                  "iso_advert_date": '1974-09-07',
                  "item_number": "73",
                  "phone1": '4971055',
                  "phone2": 'none',
                  "dealers_licence": 'none',
                  "who": 'WW',
                  "price": 'none',
                  "milage":'none',
                  "month": 'none'
      }




      clues = {
                  "rego_plate": 'ABC123',
                  "jurisdiction": 'NSW',
                  "iso_advert_date": '1999-09-09',
                  "item_number": "1",
                  "phone1": '(047)1000007',
                  "phone2": '0243650791',
                  "dealers_licence": 'DL007',
                  "who": 'James Bond',
                  "price": '$2888',
                  "milage":'55000mis',
                  "month":['January', 'February', 'March']
      }

    # for question in must_ask:
    for question in must_ask:
            print(clues[question])
            answer = input(question + "<" + must_ask[question] + ">")
            if answer == "":
                Data_Fill[question] = must_ask[question]
            else:
                Data_Fill[question] = answer

    return Data_Fill


def main():
    Default_Fill = {
                  "master_index": '99999999',
    }
    while True:
            Data_Fill = Menu(Default_Fill)
            ads_dict = []
            plate = Data_Fill["rego_plate"][0:3]
            add_adverts(Data_Fill)
            ads = get_sql_plate_data(plate)
            pics_dict = {}
            pics_dict = get_sql_pictures_all(connectstring="../advertisements_indexed.db", jurisdiction=Data_Fill["jurisdiction"],
                                          publication="all", publication_year="all", car_make="all", car_model="all", car_plate=Data_Fill["rego_plate"] )
            for pic in pics_dict: # print them out
                new_pic = pics_dict[pic]
                new_pic.print_picture()

if __name__ == '__main__':
    main()
