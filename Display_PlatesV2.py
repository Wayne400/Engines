import sqlite3
import re
from collections import defaultdict
from plate_checker import get_block_number, get_IQ_index
from datetime import datetime

def check_plate_nsw(target_plate):

    nsw_list = 0
    nsw_series_one = {'1960':"CAA000" , '1961': 'CLL000', '1962': 'CTA000', '1963' : 'DAA000',
                    '1964': 'DKA000', '1965': 'DOJ000', '1966': 'EDA000', '1967': 'EMA000',
                    '1968': 'EZZ999'}

    nsw_series_two = {'1968': 'AAA000', '1969': 'BAJ000', '1970': 'BZZ999'}


    nsw_series_three = { '1970': 'AAI000', '1971': 'CWI000','1972': 'DXI000', '1973': 'EZQ999'}

    nsw_series_four = {'1972': 'GAA000','1973': 'GEA000', '1974': 'GQA000', '1975': 'HEA000',
                    '1976': 'HQA000', '1977': 'JCA050', '1978':'JPE050', '1979': 'KBH050',
                    '1980': 'FOA000', '1981':'LCZ050', '1982':'LOS050', '1983':'MBE050', '1984':'MOZ050'}


 #   target_plate = rego_nsw
#    print(target_plate)
    plate_list = []
    stuff = list(target_plate)
    letterQ = 'Q'
    letterI = 'I'

    if (((letterQ in stuff) or (letterI in stuff)) and target_plate < nsw_series_four["1972"]):
        nsw_series = nsw_series_three
        year_list = list(nsw_series_three.keys())
        nsw_list = 3
    elif target_plate < nsw_series_one["1960"]:
        nsw_series = nsw_series_two
        year_list = list(nsw_series_two.keys())
        nsw_list = 2
    elif target_plate >= nsw_series_four["1972"]:
        nsw_series = nsw_series_four
        year_list = list(nsw_series_four.keys())
        nsw_list = 4
    else:
        nsw_series = nsw_series_one
        year_list = list(nsw_series_one.keys())
        nsw_list = 1


    year_list.sort()
#    print year_list
    for year in year_list: # create list from wiki table, sort by year
#        print year , nsw_series[year]
        plate_list.append(nsw_series[year])


    search_key = 0
    for plate in plate_list:
#        print plate , year_list[search_key]
        if  plate > target_plate:
#            print target_plate, year_list[search_key -1 ]
            break
        search_key = search_key + 1
#        print search_key , plate, target_plate, year_list[search_key - 1], nsw_list


    return year_list[search_key - 1], nsw_list

def get_sql_data(car_model_list, **kwargs):
    #  print kwargs
    jurisdiction = kwargs["jurisdiction"]
    connectstring = kwargs["connectstring"]
    car_make = kwargs["car_make"]
    stop = len(car_model_list)
    car_model_or_string = "( car_model = '{}'".format(car_model_list[0])
    for x in range(1, stop):
        car_model_or_string += " or " + "car_model = '{}'".format(car_model_list[x])
    #      print car_model_list[x]
    car_model_or_string += " )"
    #     sql = "select * from adverts"
    #  car_model_string = "car_model = '{}'".format(car_model_list[0])
    sql = "select * from adverts where {} and jurisdiction = '{}' and car_make = '{}' ".format(
        car_model_or_string, jurisdiction, car_make)
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


def print_rambler(search_index, sql_data, total_no_of_ads, year_estimate):
    for ads_record in sql_data:
        master_index = ads_record[0]
        rego_plate = ads_record[1]
        if re.match('^[A-E][I,Q][A-Z][0-9][0-9][0-9]', rego_plate) or \
                re.match('^[A-E][A-Z][I,Q][0-9][0-9][0-9]',rego_plate):
            block_number = get_IQ_index(rego_plate)
        else:
            block_number = get_block_number(rego_plate)
#        block_number = get_block_number(rego_plate)
        jurisdiction = ads_record[2]
        iso_advert_date = ads_record[3]
        item_number = ads_record[4]
        publication = ads_record[5]
        car_make = ads_record[6]
        car_model = ads_record[7]
        model_year = ads_record[8]
        if model_year == "none":
            model_year = ""
        capacity = ads_record[9]
        if capacity == "none":
            capacity = ""
        colour = ads_record[10]
        if colour == "unknown":
            colour = ""
        phone1 = ads_record[11]
        if str(phone1) == "6672484" or str(phone1) == "6674460":
            phone1 = ""
        phone2 = ads_record[12]
        dealers_licence = ads_record[13]
        who = ads_record[14]
        interior_trim = ads_record[15]
        if interior_trim == "none":
            interior_trim = ""
        body_style = ads_record[16]
        if body_style == "Sedan":
            body_style = ""
        trim_level = ads_record[17]
        if trim_level == "none":
            trim_level = ""
        price = ads_record[18]
        if price == "none":
            price = ""
        miles = ads_record[19]
        model_code = ads_record[20]
        if capacity == "****":
            car_model = "**********"
        if master_index == search_index:
            # print (
            # '{0:3} ! {1:6} | {2:4} | {3:10} | {4:5} | {5:10} | {6:1} | {7:6} | {8:6} | {9:10} | {10:6} | {11:20} | {12:16} | {13:16} ! {14:10} | {15:10} ! {16:10} ! {17:8} ! {18:2} ! {19} '.format(
            # master_index, rego_plate, model_year, car_model, capacity, iso_advert_date, total_no_of_ads, trim_level, body_style,
            # phone1, price ,colour, interior_trim, who, dealers_licence, publication, miles, phone2, item_number, rego_plate))
            print (
            '{0:6} | {1:4} | {2:4} | {3:4} | {4:10} | {5:20} | {6:8} | {7:5} | {8:6} | {9:6} | {10:10} | {11:6} | {12:10} | {13:4} | {14:2} '.format(
                rego_plate, year_estimate, block_number, model_year, car_model, colour, interior_trim, capacity, trim_level,
                body_style, phone1, price, iso_advert_date, master_index, item_number))



def print_renault_nsw(search_index, sql_data, total_no_of_ads, year_estimate):
    nsw_list = 0
    for ads_record in sql_data:
        master_index = ads_record[0]
        rego_plate = ads_record[1]
        if re.match('^[A-E][I,Q][A-Z][0-9][0-9][0-9]', rego_plate) or \
                re.match('^[A-E][A-Z][I,Q][0-9][0-9][0-9]',rego_plate):
            block_number = get_IQ_index(rego_plate)
        else:
            block_number = get_block_number(rego_plate)
#       block_number = get_block_number(rego_plate)
        jurisdiction = ads_record[2]
#        plate_checker_out, nsw_list = check_plate_nsw(rego_plate)
#        print nsw_list
#        plate_checker_out = ads_record[8]
        iso_advert_date = ads_record[3]
        item_number = ads_record[4]
        publication = ads_record[5]
        car_make = ads_record[6]
        car_model = ads_record[7]
        if car_model == "NSW2" or car_model == "NSW":
            car_model = ""
        model_year = ads_record[8]
        if model_year == "none":
            model_year = ""
        capacity = ads_record[9]
        if capacity == "none":
            capacity = ""
        colour = ads_record[10]
        if colour == "unknown":
            colour = ""
        phone1 = ads_record[11]
        phone2 = ads_record[12]
        dealers_licence = ads_record[13]
        who = ads_record[14]
        interior_trim = ads_record[15]
        if interior_trim == "none":
            interior_trim = ""
        body_style = ads_record[16]
        if body_style == "Sedan":
            body_style = ""
        trim_level = ads_record[17]
        if trim_level == "none" or trim_level == "XX":
            trim_level = ""
        price = ads_record[18]
        if price == "none":
            price = ""
        miles = ads_record[19]
        model_code = ads_record[20]
        month = ads_record[21]
        if month == "none":
            month = ""
        if capacity == "****":
            capacity = "**********"
        if master_index == search_index:
            # print (
            # '{0:3} ! {1:6} | {2:4} | {3:10} | {4:5} | {5:10} | {6:1} | {7:6} | {8:6} | {9:10} | {10:6} | {11:20} | {12:16} | {13:16} ! {14:10} | {15:10} ! {16:10} ! {17:8} ! {18:2} ! {19} '.format(
            # master_index, rego_plate, model_year, car_model, capacity, iso_advert_date, total_no_of_ads, trim_level, body_style,
            # phone1, pricera
            #  ,colour, interior_trim, who, dealers_licence, publication, miles, phone2, item_number, rego_plate))
            print (
            '{0:6} | {1:4} | {2:4} | {3:4} | {4:9} | {5:4}  | {6:2} | {7:19} | {8:10} | {9:6} | {10:10} | {11:3}'.format(
            rego_plate, year_estimate, block_number, model_year, month, car_model, trim_level,  colour, phone1, price, iso_advert_date, master_index))

def print_ford(search_index, sql_data, total_no_of_ads):
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
        if model_year == "none":
            model_year = ""
        capacity = ads_record[9]
        if capacity == "none":
            capacity = ""
        colour = ads_record[10]
        if colour == "unknown":
            colour = ""
        phone1 = ads_record[11]
        phone2 = ads_record[12]
        dealers_licence = ads_record[13]
        who = ads_record[14]
        interior_trim = ads_record[15]
        if interior_trim == "none":
            interior_trim = ""
        body_style = ads_record[16]
        if body_style == "Sedan":
            body_style = ""
        trim_level = ads_record[17]
        if trim_level == "none":
            trim_level = ""
        price = ads_record[18]
        if price == "none":
            price = ""
        miles = ads_record[19]
        model_code = ads_record[20]
        if capacity == "****":
            car_model = "**********"
        if master_index == search_index:
            # print (
            # '{0:3} ! {1:6} | {2:4} | {3:10} | {4:5} | {5:10} | {6:1} | {7:6} | {8:6} | {9:10} | {10:6} | {11:20} | {12:16} | {13:16} ! {14:10} | {15:10} ! {16:10} ! {17:8} ! {18:2} ! {19} '.format(
            # master_index, rego_plate, model_year, car_model, capacity, iso_advert_date, total_no_of_ads, trim_level, body_style,
            # phone1, price ,colour, interior_trim, who, dealers_licence, publication, miles, phone2, item_number, rego_plate))
            print (
            '{0:4} | {1:6} | {2:4} | {3:10} | {4:20} | {5:8} | {6:5} | {7:6} | {8:6} | {9:10} | {10:6} | {11:10} | {12:2} '.format(
                master_index, rego_plate, model_year, car_model, colour, interior_trim, capacity, trim_level,
                body_style, phone1, price, iso_advert_date, item_number))



def main():
  go_again = 'y'
  while go_again != 'n':
    while True:
        pick_make = raw_input("Make? Rambler Renault Ford")
        if pick_make == "ra":
            pick_model = raw_input("please enter model: ")
            if pick_model == "h":
                Rambler_list = ["Hornet", "NSW2"]
            elif pick_model == "m":
                Rambler_list = ["Matador", "NSW2"]
            elif pick_model == "r":
                Rambler_list = ["Rebel", "NSW"]
            elif pick_model == "rm":
                Rambler_list = ["Rebel", "Matador", "NSW2"]
            elif pick_model == "rac":
                Rambler_list = ["Rebel", "American","Classic","NSW"]
            elif pick_model == "rmh":
                Rambler_list = ["Rebel", "Matador", "Hornet", "NSW2"]
            elif pick_model == "j":
                Rambler_list = ["Javelin", "NSW2"]
            elif pick_model == "c":
                Rambler_list = ["Classic", "NSW"]
            elif pick_model == "an":
                Rambler_list = ["American", "NSW"]
            elif pick_model == "x":
                Rambler_list = ["AMX"]
            elif pick_model == "ar":
                Rambler_list = ["Ambassador", "NSW"]
            else:
                Rambler_list = ["Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American", "AMX"]
            ads_table = get_sql_data(car_model_list=Rambler_list, car_make="Rambler", connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW")
            break
        elif pick_make == "fo":
            Ford_list = ["Falcon", "Cortina", "Capri"]
            ads_table = get_sql_data(car_model_list=Ford_list, car_make="Ford", connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW")
            break
        elif pick_make == "re":
            Renault_list = ["R10", "R12", "R16","R10S","10S"]
            ads_table = get_sql_data(car_model_list=Renault_list, car_make ="Renault", connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW")
            break
        elif pick_make == 'x':
            break
        else:
            print "try again"
    print "goodbye"
    #  ads_table.sort
    # print ads
    plate_keys = []
    master_index_check = []
    ads_list = defaultdict(list)  # this is a dictionary of lists
    nsw_dummy_object_list = defaultdict(list)  # this is a dictionary of lists
    plates_total = 0
    for ads_record in ads_table:  # we make a lists of database indexes for distinct plate numbers, insert into dictionary
      if re.match('^[A-Q][A-Z][A-Z][0-9][0-9][0-9]', str(ads_record[1])):
        ads_list[str(ads_record[1])].append(ads_record[0])  # plate number and database index
        if ads_record[0] in master_index_check:
            print "help duplicate", ads_record[0]
        else:
            master_index_check.append(ads_record[0])
        if not str(ads_record[1]) in plate_keys:
            plate_keys.append(str(ads_record[1]))  # my list of rego plates
            plate_checker_out, nsw_list = check_plate_nsw(ads_record[1])
            nsw_dummy_object_list[str(ads_record[1])].append(plate_checker_out)
            nsw_dummy_object_list[str(ads_record[1])].append(nsw_list)
            plates_total += 1

    print('we have found {} plates'.format(plates_total))


    go_again = raw_input("Go Again y/n: ")

    #   print ads_list.items()
    plate_keys.sort()
    print plate_keys
    plate_index = 0
    last_plate = "XYZ123"
    for x in range(1, 5):
        print "*" * 140
        for plate in plate_keys:
            plate_index += 1
            year_estimate = "1955"
            this_plate = str(plate)
            ads_index_list = ads_list[plate]
            nsw_dummy_object = nsw_dummy_object_list[plate]
            #        print plate_index, plate, ads_index_list, nsw_dummy_object[0], nsw_dummy_object[1]
            no_of_ads = len(ads_index_list)
            ad_index = ads_index_list[0]  ### temporary
            #          print x, nsw_dummy_object[1]
            if x == int(nsw_dummy_object[1]):  # there are 4 nsw plate lists
  #              print ad_index

  if pick_make == "ra":
      print_rambler(search_index=ad_index, sql_data=ads_table, total_no_of_ads=no_of_ads,
                    year_estimate=nsw_dummy_object[0])
  elif pick_make == "re":
      print_renault_nsw(search_index=ad_index, sql_data=ads_table, total_no_of_ads=no_of_ads,
                        year_estimate=nsw_dummy_object[0])
  elif pick_make == "fo":
      print_ford(search_index=ad_index, sql_data=ads_table, total_no_of_ads=no_of_ads)
  else:
      print "ouch"


if __name__ == '__main__':
    main()
