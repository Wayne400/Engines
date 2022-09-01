import sqlite3
import re

def get_sql_plate_data( plate ):
    #  print kwargs

    conn = open_database('../advertisements_indexed.db')

    sql = "select * from adverts where rego_plate LIKE '{0}%'".format( plate)

    #print(sql)

    try:
        cursor = conn.cursor()
        results = cursor.execute(sql)
        ads = results.fetchall()
        conn.close()
        return ads

    except:
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
        #print(sql)
        try:
            cursor.execute(sql)
        except:
            print("failed to add data")
            pass
        conn.commit()
        conn.close()



def main():
    from Display_Plates_V3 import Advertisement
    Data_Fill = { "master_index": '99999999',
                  "rego_plate": 'ABC123',
                  "jurisdiction": 'NSW',
                  "iso_advert_date": '1999-09-09',
                  "item_number": 1 ,
                  "publication": 'smh',
                  "car_make": 'aston martin',
                  "car_model": 'DB5',
                  "model_year": '1965',
                  "model_code": 'MKIV',
                  "model_level": 'none',
                  "trim_level": 'XXX',
                  "body_style": 'Coupe',
                  "transmission": 'Man',
                  "capacity": 'none',                 # 5 - 9
                  "colour": 'Green',
                  "interior_trim": 'Red Leather',
                  "phone1": '(047)1000007',
                  "phone2": '0243650791',
                  "dealers_licence": 'DL007',
                  "who": 'James Bond',                          # 10 - 14
                  "price": '$2888',
                  "milage":'55000mis',                  # 15 - 19
                  "month":'January',
                  "air": 'YES',
                 "VIN": 'XXX007',
                 "Engine_No": 'ENG007',
                 "Body_No": 'BOND-007',
                 "Location": 'Albury'}                                     # 25 - 28


    while True:
      Make_list = ["Rambler", "Renault", "Peugeot", "Rover", "Triumph", "Ford", "Mascot", "Valiant", "Leyland", "x = exit"]
      print(Make_list)
      pick_make = input("Car Make?")
      if pick_make != 'x':
        print(pick_make)
        if pick_make == "Ram" or pick_make == "Rambler":
            Rambler_list = ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American",
                            "AMX", "Marlin", "X-Coupe", "Wagon"]
            print(Rambler_list)
            dont_ask = {'master_index': '99999999',
                        'jurisdiction': 'NSW',
                        'item_number': 1,
                        'publication': "smh",
                        'car_make': 'Rambler',
                        'transmission': 'none',
                        'phone2': 'none',
                        'dealers_licence': 'none',
                        'who': 'WW',
                        "model_code": "none",
                        'body_style': 'none',
                        'air': 'none',
                        'model_level': 'none',
                        'VIN': 'none',
                        'Engine_No': 'none',
                        'Body_No': 'none',
                        'Location': 'Sydney'}
            must_ask = {"rego_plate": 'RAM232',
                        "iso_advert_date": '1970-02-28',
                        "car_model": "NO Default",
                        "trim_level": 'none',
                        "model_year": 'none',
                        "capacity": 'none',
                        "colour": 'unknown',
                        "interior_trim": 'none',
                        "phone1": 'No Default',
                        "price": 'none',
                        "milage": 'none',
                        "month": 'none'}
            clues = {"rego_plate": "RAM258", 'iso_advert_date': "1984-12-25",
                    'car_model': ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American",
                                  "AMX", "Marlin", "X-Coupe", "Wagon"],
                    'trim_level': ["SST", "770", "440", "660", "330"],
                    'model_year': ["1960", "1979"],
                    'capacity': ["232", "258", "290", "360", "287", "6cyl"],
                    'colour': ["Big Bad Orange", "White", "Cream", "Grey", "Black"],
                    'interior_trim': ["Bone", "Red", "Beige", "Buckskin", "Tan", "Fawn","Brown", "Black"],
                    'phone1': ["91844207"], 'price': ["$3400"], 'milage': ["40000mis", "55000kms"],
                    'month': ["January", "February", "March"]}



        elif pick_make == "fo" or pick_make == "Ford":
            Ford_list = ["Falcon", "Cortina", "Capri"]
            print(Ford_list)

        elif pick_make == "Ren" or pick_make == "Renault":
            Renault_list = ["R4", "R8", "R10", "R12", "R16", "R10S", "10S", "R15", "R17", "1.4", "RXX"]
         #   print(Renault_list)
            dont_ask = {'master_index': '99999999',
                        'jurisdiction': 'NSW',
                        'item_number': 1,
                        'publication': "smh",
                        'car_make': 'Renault',
                        'capacity': 'none',
                        'phone2': 'none',
                        'dealers_licence': 'none',
                        'who': 'WW',
                        "model_code": "none",
                        'body_style': 'none',
                        'air': 'none',
                        'model_level': 'none',
                        'VIN': 'none',
                        'Engine_No': 'none',
                        'Body_No': 'none',
                        'Location': 'Sydney'}
            must_ask = {"rego_plate": 'REN123',
                        "iso_advert_date": '1970-02-28',
                        "car_model": "RXX",
                        "trim_level": 'XX',
                        "model_year": 'none',
                        "transmission": 'none',
                        "colour": 'unknown',
                        "interior_trim": 'none',
                        "phone1": 'No Default',
                        "price": 'none',
                        "milage": 'none',
                        "month": 'none'}
            clues = {"rego_plate": "REN123", 'iso_advert_date': "1984-12-25",
                    'car_model': ["750", "R4", "R8", "R10", "R12", "R16", "R10S", "10S", "R15", "R17", "1.4", "R20", "RXX"],
                    'trim_level': ["TL", "TS", "GL", "S", "Gordini"],
                    'model_year': ["1960", "1979"],
                    'transmission': ["Auto", "Man"],
                    'colour': ["White", "Cream", "Grey", "Black"],
                    'interior_trim': ["Champagne", "Red Leather", "Burgundy", "Bone Leather", "Tan", "Fawn","Brown", "Brick"],
                    'phone1': ["91844207"], 'price': ["$3400"], 'milage': ["40000mis", "55000kms"],
                    'month': ["January", "February", "March"]}

        elif pick_make == "Peu" or pick_make == "Peugeot":
            Peugeot_list = ["403", "403B", "404", "504", "203", "203C"]
            dont_ask = {'master_index': '99999999',
                        'jurisdiction': 'NSW',
                        'item_number': 1,
                        'publication': "smh",
                        'car_make': 'Peugeot',
                        'capacity': 'none',
                        'phone2': 'none',
                        'dealers_licence': 'none',
                        'who': 'WW',
                        "model_code": "none",
                        'body_style': 'none',
                        "trim_level": 'none',
                        'air': 'none',
                        'model_level': 'none',
                        'VIN': 'none',
                        'Engine_No': 'none',
                        'Body_No': 'none',
                        'Location': 'Sydney'}
            must_ask = {"rego_plate": 'PEU123',
                        "iso_advert_date": '1970-02-28',
                        "car_model": "X0X",
                        "model_year": 'none',
                        "transmission": 'none',
                        "colour": 'unknown',
                        "interior_trim": 'none',
                        "phone1": 'No Default',
                        "price": 'none',
                        "milage": 'none',
                        "month": 'none'}
            clues = {"rego_plate": "PEU123", 'iso_advert_date': "1984-12-25",
                    'car_model': Peugeot_list,
                    'model_year': ["1960", "1979"],
                    'transmission': ["Auto", "Man"],
                    'colour': ["White", "Ivory", "Burgundy","Maroon", "Black"],
                    'interior_trim': ["Champagne", "Red Leather", "Burgundy", "Bone Leather", "Tan", "Fawn","Brown", "Brick"],
                    'phone1': ["91844207"], 'price': ["$3400"], 'milage': ["40000mis", "55000kms"],
                    'month': ["January", "February", "March"]}

        elif pick_make == "Rov" or pick_make == "Rover":
            Rover_list = ["105R", "105S", "2000", "2000TC", "3500", "P5B", "P5", "P5Bcoupe", "P5coupe", "3L", "100"]
            #print(Rover_list)
            dont_ask = {'master_index': '99999999',
                        'jurisdiction': 'NSW',
                        'item_number': 1,
                        'publication': "smh",
                        'car_make': 'Rover',
                        'capacity': 'none',
                        'phone2': 'none',
                        'dealers_licence': 'none',
                        'who': 'WW',
                        'body_style': 'none',
                        'air': 'none',
                        'model_level': 'none',
                        'VIN': 'none',
                        'Engine_No': 'none',
                        'Body_No': 'none',
                        'Location': 'Sydney'}
            must_ask = {"rego_plate": 'ROV123',
                        "iso_advert_date": '1970-02-28',
                        "car_model": "NO Default",
                        "model_code": "none",
                        "trim_level": 'XX',
                        "model_year": 'none',
                        "transmission": 'none',
                        "colour": 'unknown',
                        "interior_trim": 'none',
                        "phone1": 'No Default',
                        "price": 'none',
                        "milage": 'none',
                        "month": 'none'}
            clues = {"rego_plate": "ROV123", 'iso_advert_date': "1984-12-25",
                    'car_model': ["75", "90", "95", "100", "105R", "105S", "110", "2000", "2000TC", "3500", "P5B",
                    "P5", "P5Bcoupe","P5coupe", "3L", "3.5L", "SD1"],
                    'model_code': ["MKI", "MKII", "MKIII"],
                    'trim_level': ["TC", "Coupe", "S"],
                    'model_year': ["1960", "1979"],
                    'transmission': ["Auto", "Man"],
                    'colour': ["White", "Cream", "Grey", "Black"],
                    'interior_trim': ["Champagne", "Red Leather", "Burgundy", "Bone Leather", "Tan", "Fawn","Brown", "Brick"],
                    'phone1': ["(043)844207"], 'price': ["$3400"], 'milage': ["40000mis", "55000kms"],
                    'month': ["January", "February", "March"]}

        elif pick_make == "Tri" or pick_make == "Triumph":
            Triumph_list = ["2000", "2500" ]
            dont_ask = {'master_index': '99999999',
                        'jurisdiction': 'NSW',
                        'item_number': 1,
                        'publication': "smh",
                        'car_make': 'Triumph',
                        'capacity': 'none',
                        'phone2': 'none',
                        'dealers_licence': 'none',
                        'who': 'WW',
                        'body_style': 'none',
                        'air': 'none',
                        'model_level': 'none',
                        'VIN': 'none',
                        'Engine_No': 'none',
                        'Body_No': 'none',
                        'Location': 'Sydney'}
            must_ask = {"rego_plate": 'TRI123',
                        "iso_advert_date": '1970-02-28',
                        "car_model": "NO Default",
                        "model_code": "none",
                        "trim_level": 'none',
                        "model_year": 'none',
                        "transmission": 'none',
                        "colour": 'unknown',
                        "interior_trim": 'none',
                        "phone1": 'No Default',
                        "price": 'none',
                        "milage": 'none',
                        "month": 'none'}
            clues = {"rego_plate": "TRI123", 'iso_advert_date': "1984-12-25",
                    'car_model': Triumph_list,
                    'model_code': ["MKI", "MKII"],
                    'trim_level': ["TC", "PI", "S"],
                    'model_year': ["1960", "1979"],
                    'transmission': ["Auto", "Man"],
                    'colour': ["White", "Cream", "Grey", "Black"],
                    'interior_trim': ["Champagne", "Red Leather", "Burgundy", "Bone Leather", "Tan", "Fawn","Brown", "Brick"],
                    'phone1': ["(043)844207"], 'price': ["$3400"], 'milage': ["40000mis", "55000kms"],
                    'month': ["January", "February", "March"]}

        elif pick_make == "Leyland":
            Leyland_list = ["P76"]
            print(Leyland_list)

        elif pick_make == "Val" or pick_make == "Valiant":
            #print(Valiant_list)
            dont_ask = {'master_index': '99999998',
                        'jurisdiction': 'NSW',
                        'item_number': 1,
                        'publication': "smh",
                        'car_make': 'Chrysler',
                        'car_model': "Valiant",
                        'phone2': 'none',
                        'dealers_licence': 'none',
                        'who': 'WW',
                        "interior_trim": "none",
                        'air': 'none',
                        'VIN': 'none',
                        'Engine_No': 'none',
                        'Body_No': 'none',
                        'Location': 'Sydney'}
            must_ask = {"rego_plate": 'VAL123',
                        "iso_advert_date": '1970-02-28',
                        "model_year": "none",
                        "model_code": 'none',
                        "model_level": 'none',
                        "trim_level": 'none',
                        "capacity": 'none',
                        "body_style": 'none',
                        "transmission": 'none',
                        "colour": 'unknown',
                        "phone1": 'No Default',
                        "price": 'none',
                        "milage": 'none',
                        "month": 'none'}
            clues = {"rego_plate": "VAL123",
                    'iso_advert_date': "1984-12-25",
                    'model_year': ["1960", "1979"],
                    'model_code': ["R","S","AP5", "AP6", "VC", "VE","VF","VG","VH","VJ","VK","CL","CM"],
                    'model_level': ["Valiant", "Regal", "Safari", "VIP", "Pacer", "Ranger", "Charger"],
                    'trim_level': ["XL", "770", "Drifter", "E38", "E48", "E49"],
                    'capacity': ["215", "225", "245", "265", "273", "318", "360"],
                    'body_style': ["Sedan", "Wagon", "Utility", "Panel Van", "Coupe"],
                    'transmission': ["Auto", "Man"],
                    'colour': ["White", "Cream", "Grey", "Black"],
                    'phone1': ["(043)844207"],
                    'price': ["$2100"],
                    'milage': ["40000mis", "55000kms"],
                    'month': ["January", "February", "March"]}

        else:
            break

        ads_dict = {}
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

        plate = Data_Fill["rego_plate"][0:3]
        add_adverts( Data_Fill)
        ads = get_sql_plate_data(plate)
        for ads_record in ads:  # we make a lists of database indexes for distinct plate numbers, insert into dictionary
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
            new_ad.set_dealer()
            ads_dict[ads_master_index] = new_ad

        #print(ads)
        for old_ads in ads_dict:
            ads_dict[old_ads].print_ad()

if __name__ == '__main__':
    main()
