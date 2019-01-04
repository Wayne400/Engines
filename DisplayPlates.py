import sqlite3
from collections import defaultdict
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

    if (((letterQ in stuff) or (letterI in stuff)) and target_plate < nsw_series_four["1973"]):
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

    return year_list[search_key - 1], nsw_list

def get_sql_data(car_model_list, **kwargs):
    #  print kwargs
    jurisdiction = kwargs["jurisdiction"]
    order_by = kwargs["order_by"]
    connectstring = kwargs["connectstring"]
    stop = len(car_model_list)
    car_model_or_string = "( car_model = '{}'".format(car_model_list[0])
    for x in range(1, stop):
        car_model_or_string += " or " + "car_model = '{}'".format(car_model_list[x])
    #      print car_model_list[x]
    car_model_or_string += " )"
    #     sql = "select * from adverts"
    #  car_model_string = "car_model = '{}'".format(car_model_list[0])
    sql = "select * from adverts where {} and jurisdiction = '{}' ORDER BY {}".format(
        car_model_or_string, jurisdiction, order_by)
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
            '{0:4} | {1:6} | {2:4} | {3:10} | {4:20} | {5:8} | {6:5} | {7:6} | {8:6} | {9:10} | {10:6} | {11:10} | {12:2} '.format(
                master_index, rego_plate, model_year, car_model, colour, interior_trim, capacity, trim_level,
                body_style, phone1, price, iso_advert_date, item_number))



def print_renault_nsw(search_index, sql_data, total_no_of_ads):
    nsw_list = 0
    for ads_record in sql_data:
        master_index = ads_record[0]
        rego_plate = ads_record[1]
        jurisdiction = ads_record[2]
        plate_checker_out, nsw_list = check_plate_nsw(rego_plate)
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
            '{0:4} | {1:6} | {2:4} | {3:4} | {4:9} | {5:4}  | {6:2} | {7:16} | {8:10} | {9:6} | {10:10} | {11:1}'.format(
         master_index, rego_plate, model_year, plate_checker_out, month, car_model, trim_level,  colour, phone1, price, iso_advert_date, nsw_list))

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
            ads_table = get_sql_data(car_model_list=Rambler_list, connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW",
                                     order_by="iso_advert_date")
            break
        elif pick_make == "fo":
            Ford_list = ["Falcon", "Cortina", "Capri"]
            ads_table = get_sql_data(car_model_list=Ford_list, connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW", order_by="iso_advert_date")
            break
        elif pick_make == "re":
            Renault_list = ["R10", "R12", "R16","NSW2"]
            ads_table = get_sql_data(car_model_list=Renault_list, connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW", order_by="iso_advert_date")
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
    plates_table = defaultdict(list)  # this is a dictionary of lists
    plates_total = 0
    for ads_record in ads_table:  # we make a lists of database indexes for distinct plate numbers, insert into dictionary
        plates_table[str(ads_record[1])].append(ads_record[0])  # plate number and database index
        if ads_record[0] in master_index_check:
            print "help duplicate", ads_record[0]
        else:
            master_index_check.append(ads_record[0])
        if not str(ads_record[1]) in plate_keys:
            plate_keys.append(str(ads_record[1]))  # my list of rego plates
            plates_total += 1

    print('we have found {} plates'.format(plates_total))

    #   print plates_table.items()
    plate_keys.sort()
#    print plate_keys
    plate_index = 0
    last_plate = "XYZ123"
    for plate in plate_keys:
        plate_index += 1
        this_plate = str(plate)
        ads_index_list = plates_table[plate]
#        print plate_index, plate, ads_index_list
        no_of_ads = len(ads_index_list)
        for ad_index in ads_index_list:
            if not this_plate == last_plate:  # dont print multiple ads of same car
                if pick_make == "ra":
                    print_row(search_index=ad_index, sql_data=ads_table, total_no_of_ads=no_of_ads)
                elif pick_make == "re":
                    print_renault_nsw(search_index=ad_index, sql_data=ads_table, total_no_of_ads=no_of_ads)
                elif pick_make == "fo":
                    print_ford(search_index=ad_index, sql_data=ads_table, total_no_of_ads=no_of_ads)
                else:
                    print "ouch"
                last_plate = this_plate
    go_again = raw_input("Go Again y/n: ")


if __name__ == '__main__':
    main()
