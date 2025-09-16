import sqlite3
import re
from Display_Plates_V3 import Advertisement, get_sql_number
from Get_Car_Sales_Data import Car_Sales_Data
from SQL_Utils import get_sql_pictures_all

def  create_ads(ads_dict):
    ads = {}
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
      #  for old_ads in ads:
       #     new_ad.set_suburb()
        #    ads[old_ads].print_ad()

    return ads

def get_sql_plate_data(plate):
    #  print kwargs

    conn = open_database('../advertisements_indexed.db')

    sql = "select * from adverts where rego_plate LIKE '{0}%'".format( plate)

    print(sql)
    ads_dict = {}

    try:
        cursor = conn.cursor()
        results = cursor.execute(sql)
        ads_dict = results.fetchall()
        conn.close()
    except Exception as e:
        print(e)
        print("I am unable to connect to the database")
        conn.close()

#    ads = create_ads(ads_dict)

    return ads_dict
"""        for ads_record in ads_dict:  # we make a lists of database indexes for distinct plate numbers, insert into dictionary
        
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
"""
#    except Exception as e:
#        print(e)
#        print("I am unable to connect to the database")
#        conn.close()


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
                  body_style, transmission, model_code, model_level, model_series, trim_level, price, milage, month,
                   air, VIN, Engine_No, Body_No, Location)
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{transmission}", "{model_code}", "{model_level}", "{model_series}", "{trim_level}","{price}", "{milage}", "{month}",
          "{air}", "{VIN}", "{Engine_No}", "{Body_No}", "{Location}")'''

        sql = sql.format(master_index=master_index1, rego_plate=row["rego_plate"],
                        jurisdiction=row["jurisdiction"],
                        iso_advert_date=row["iso_advert_date"],
                        item_number=row["item_number"], publication=row["publication"],
                        car_make=row["car_make"], car_model=row["car_model"], model_year=row["model_year"],
                        capacity=row["capacity"],model_level=row["model_level"], model_series=row["model_series"],
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

def Do_Car_Sales_Menu2( publication, clues):

    Make_List = ["Datsun", "Ford", "Holden", "Isuzu", "Jaguar", "Leyland", "Peugeot", "Rambler",
                 "Renault", "Rover", "Triumph", "Valiant", "Volkswagen",
                ]

    print(Make_List)
    car_make = input("Car Make?")
    Make_Info = {}
    Make_Dict = {}
    Model_Code = {}
    Model_Level = {}
    Model_Series = {}
    Trim_Level = {}
    Body_Style = {}
    Data_Fill = {}
    Car_Sales_Data(car_make,Make_Info,Make_Dict,Model_Code,Model_Level,Model_Series,Trim_Level,Body_Style)


    if publication == "smh" or publication == "age"  or publication == "Top Tests No.2": # Not Unique or Just Cars
        clues['transmission'] = 'Man'
        clues['capacity'] = ['V8', '6cyl', '4.3', '258']
        clues['colour'] = 'Green'
        clues['interior_trim'] = 'Red Leather'
        clues['model_year'] = '1969'
        for key, value in clues.items():  # append Make_Info so questions get asked
            Make_Info[car_make].append(key)
            if key == 'colour':
                Data_Fill[key] = 'unknown'
            else:
                Data_Fill[key] = 'none'

        Data_Fill['VIN'] = 'none'     # Dont append so dont ask.
        Data_Fill['Engine_No'] = 'none'
        Data_Fill['Body_No'] = 'none'
        Data_Fill['Location'] = 'none'
        Data_Fill['air'] = 'none'  # Mascot Motors ads



    if publication == "Just Cars" or publication == "Unique Cars":  # Not Unique or Just Cars

        clues['transmission'] = 'Man'
        clues['capacity'] = ['V8', '6cyl', '4.3', '258']
        clues['colour'] = 'Green'
        clues['interior_trim'] = 'Red Leather'
        clues['model_year'] = '1969'

        clues['VIN'] = 'none'
        clues['Engine_No'] = 'none'
        clues['Body_No'] = 'none'
        clues['Location'] = 'none'

        for key, value in clues.items():  # append Make_Info so questions get asked
          #  print(key,car_make)
            Make_Info[car_make].append(key)
            if key == 'colour':
                Data_Fill[key] = 'unknown'
            else:
                Data_Fill[key] = 'none'
        Data_Fill['air'] = 'none'  # Mascot Motors ads only

    for question in Make_Info[car_make]:
  #      if question != 'model_code':
    #for question in Data_Fill[car_make]:
            if question == 'model_code':
     #           print('model_code', Data_Fill['car_model'])  # stored previously
                clues['model_code'] = Model_Code[car_make, Data_Fill['car_model']]
            elif question == 'model_level':
                # print('model_level', Data_Fill['car_model'])
                clues['model_level'] = Model_Level[car_make, Data_Fill['car_model']]
            elif question == 'model_series':
      #          print('model_series', Data_Fill['car_model'])
                clues['model_series'] = Model_Series[car_make, Data_Fill['car_model']]
            elif question == 'trim_level':
                # print('trim_level', Data_Fill['car_model'] )
                clues['trim_level'] = Trim_Level[car_make, Data_Fill['car_model']]
            elif question == 'body_style':
                clues['body_style'] = Body_Style[car_make, Data_Fill['car_model']]
    #        print(Data_Fill[question])
            Data_Fill[question] = "none"
          #  print(clues[question])
#            answer = input(question + "<" + Data_Fill[question] + ">")
#            if answer == "":
#                answer = Data_Fill[question]
            if question == "car_model": # always the first value in Make_Dict list
                print(Make_Dict[car_make])
                answer = input(question + "<none>")
                if answer not in Make_Dict[car_make] or answer == "":
            #        print("wally, not in model list!")
                    Data_Fill[question] = 'none'   # need for Holdens etc where EH, EK is more important
                #    break
                else:
                    Data_Fill[question] = answer
            else:
                print(clues[question])
                answer = input("select from above the " + question + "<" + Data_Fill[question] + ">")
                if answer == "":
                    answer = Data_Fill[question]
                Data_Fill[question] = answer
    return Data_Fill

def Menu():

    Publication_List = ["smh", "age", "Just Cars", "Unique Cars","FarmWrecksFacebook"]
    print(Publication_List)
    publication = input("Publication?")
    clues = {}
#    if publication == "smh" or publication == "age" or publication == "FarmWrecksFacebook" or publication == "Unique Cars":
    must_ask = {
                  "rego_plate": 'ABC123',
                  "jurisdiction": 'NSW',
                  "iso_advert_date": '1974-08-03',
                  "item_number": "82",
                  "phone1": '4971055',
                  "phone2": 'none',
                  "dealers_licence": 'none',
                  "who": 'WW',
                  "price": 'none',
                  "milage":'none',
                  "month": 'none'
      }

    Data_Fill = Do_Car_Sales_Menu2(publication, clues)
    Data_Fill['publication'] = publication


    # for question in must_ask:
    for question in must_ask:
            if question in clues:
                print(clues[question])
                answer = input(question + "<<" + must_ask[question] + ">")
            else:
                print(must_ask[question])
                answer = input(question + "<" + must_ask[question] + ">>")
            if answer == "":
                Data_Fill[question] = must_ask[question]
            else:
                Data_Fill[question] = answer

    return Data_Fill


def main():
    Default_Fill = {
                  "master_index": '99999999',
                  "rego_plate": "ABC123"
    }
    while True:
            Data_Fill = Menu()
#            ads_dict = []
#            print(Data_Fill)
            ads_dict = {}
            plate = Data_Fill["rego_plate"][0:3]
            add_adverts(Data_Fill)
            ads_dict = get_sql_plate_data(plate)    # look for plates in same series with SQL
            ads = create_ads(ads_dict)                # create ad objects
            for old_ads in ads:
                ads[old_ads].print_ad()
            pics_dict = {}
            pics_dict = get_sql_pictures_all(connectstring="../advertisements_indexed.db", jurisdiction=Data_Fill["jurisdiction"],
                                          publication="all", publication_year="all", car_make="all", car_model="all", car_plate=Data_Fill["rego_plate"] )
            for pic in pics_dict: # print them out
                new_pic = pics_dict[pic]
                new_pic.print_picture()

            other_ads = get_sql_number(connectstring="../advertisements_indexed.db",number=Data_Fill["phone1"])
            ads1 = create_ads(other_ads)
            for old_ads in ads1:
                ads1[old_ads].print_ad()

if __name__ == '__main__':
    main()
