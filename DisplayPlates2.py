import sqlite3
from collections import defaultdict
from datetime import datetime


def get_sql_data(car_model_list, **kwargs):
    #  print kwargs
    jurisdiction = kwargs["jurisdiction"]
    connectstring = kwargs["connectstring"]
    stop = len(car_model_list)
    car_model_or_string = "( car_model = '{}'".format(car_model_list[0])
    for x in range(1, stop):
        car_model_or_string += " or " + "car_model = '{}'".format(car_model_list[x])
    #      print car_model_list[x]
    car_model_or_string += " and jurisdiction  = '{}' )".format(jurisdiction)
    #     sql = "select * from adverts"
    #  car_model_string = "car_model = '{}'".format(car_model_list[0])
    sql = "select * from adverts where {} \
and (rego_plate LIKE '%I%' or rego_plate LIKE '%Q%') and  \
(rego_plate LIKE 'C%' or rego_plate LIKE 'D%' or \
rego_plate LIKE 'E%' or rego_plate LIKE 'A%' or rego_plate LIKE 'B%' ) ORDER BY iso_advert_date".format(car_model_or_string)
    print sql

    try:
        conn = sqlite3.connect(connectstring)
        cursor = conn.cursor()
        print 'connected!' + connectstring
        results = cursor.execute(sql)
        ads = results.fetchall()
        conn.close()
        return ads

    except:
        print "I am unable to connect to the database"
        conn.close()


def print_header():
    print
    print (
        '{0:<6} | {1:<4} | {14:10} {16:2} |{4:<10} |{5:6}| {6:8} ! {7:12} | {8:10} | {9:10} ! {10:10} | {12:12} ! {11:10} ! {15:6s} '.format(
            'rego', 'year', 'AUS', 'car_make', 'car_model', 'trim_lvl', 'body_style',
            'colour', 'interior', 'phone1', 'phone2', 'who', 'dealer', 'pub', 'add_date', 'price', 'item'))
    print ("-" * 200)

def print_row(search_index, sql_data, total_no_of_ads):

    for ads_record in sql_data:
        master_index = ads_record[0]
        rego_plate = ads_record[1]
        jurisdiction = ads_record[2]
        iso_advert_date = ads_record[3]
        item_number = ads_record[4]
        publication = ads_record[5]
        car_make = ads_record[6]
        car_model = ads_record[7]
        model_year = ads_record[8]
        capacity = ads_record[9]
        if capacity == "none":
            capacity = ""
        colour = ads_record[10]
        phone1 = ads_record[11]
        phone2 = ads_record[12]
        dealers_licence = ads_record[13]
        who = ads_record[14]
        interior_trim = ads_record[15]
        body_style = ads_record[16]
        trim_level = ads_record[17]
        if trim_level == "none":
            trim_level = ""
        price = ads_record[18]
        miles = ads_record[19]
        model_code = ads_record[20]
        if capacity == "****":
            car_model = "**********"
        if master_index == search_index:
            #print (
            #'{0:3} ! {1:6} | {2:4} | {3:10} | {4:5} | {5:10} | {6:1} | {7:6} | {8:6} | {9:10} | {10:6} | {11:20} | {12:16} | {13:16} ! {14:10} | {15:10} ! {16:10} ! {17:8} ! {18:2} ! {19} '.format(
            #master_index, rego_plate, model_year, car_model, capacity, iso_advert_date, total_no_of_ads, trim_level, body_style,
            #phone1, price ,colour, interior_trim, who, dealers_licence, publication, miles, phone2, item_number, rego_plate))
            print ( '{0:6} | {1:4} | {2:10} | {3:5} | {4:6} | {5:6} | {6:10} | {7:6} | {8:10} | {9:2} '.format(
                 rego_plate, model_year, car_model, capacity, trim_level, body_style, phone1, price, iso_advert_date, item_number))


def main():
  go_again = 'y'
  while go_again != 'n':
      pick_make = raw_input("Make? Rambler Renault Ford")
      if pick_make == "ra":
        pick_model = raw_input("please enter model: ")
        if pick_model == "h":
            rambler_list = ["Hornet", "NSW"]
        elif pick_model == "m":
            rambler_list = ["Matador", "NSW"]
        elif pick_model == "r":
            rambler_list = ["Rebel", "NSW"]
        elif pick_model == "rm":
            rambler_list = ["Rebel", "Matador", "NSW"]
        elif pick_model == "rmh":
            rambler_list = ["Rebel", "Matador", "Hornet", "NSW_IQ", "NSW"]
        elif pick_model == "j":
            rambler_list = ["Javelin", "NSW"]
        elif pick_model == "c":
            rambler_list = ["Classic", "NSW"]
        elif pick_model == "an":
            rambler_list = ["American", "NSW"]
        elif pick_model == "x":
            rambler_list = ["AMX", "NSW"]
        elif pick_model == "ar":
            rambler_list = ["Ambassador"]
        else:
            rambler_list = ["Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American", "AMX"]
        ads_table = get_sql_data(car_model_list=rambler_list, connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW",
                                     order_by="iso_advert_date")
        break
      elif pick_make == "fo":
            Ford_list = ["Falcon", "Cortina", "Capri"]
            ads_table = get_sql_data(car_model_list=Ford_list, connectstring="advertisements_indexed.db",                                jurisdiction="NSW", order_by="iso_advert_date")
            break
      elif pick_make == 'x':
            break
      else:
            print "try again"


  plate_keys = []
  plates_table = defaultdict(list)
  plates_total = 0
  for ads_record in ads_table:
            #     print ads_record
            plates_table[str(ads_record[1])].append(ads_record[0])
            if not str(ads_record[1]) in plate_keys:
                plate_keys.append(str(ads_record[1]))  # my list of rego plates
                plates_total += 1
            print('we have found {} plates'.format(plates_total))

  plate_keys.sort()
  plate_index = 0
  last_plate = "XYZ123"
  for plate in plate_keys:
            plate_index += 1
            this_plate = str(plate)
            ads_index_list = plates_table[plate]
            #    print plate_index, plate, ads_index_list
            no_of_ads = len(ads_index_list)
            for ad_index in ads_index_list:
                if not this_plate == last_plate:  # dont print multiple ads of same car
                    print_row(search_index=ad_index, sql_data=ads_table, total_no_of_ads=no_of_ads)
                    last_plate = this_plate
  go_again = raw_input("Go Again y/n: ")

if __name__ == '__main__':
    main()
