import sqlite3
import re
from collections import defaultdict
from sydney_exchange import get_exchange_dict
from Dealers import dealers_list
from datetime import datetime
from NSW_Plate_Info import get_month



def check_production( make, model, sort1, sort2, sort3):
    if model == 'none' and make != 'Chrysler':
        model = "RXX"
    renault_model_start = {'RXX': '1960','R4': '1958', 'R8': '1961','Gordini': '1963', 'R10': '1965', 'R10S': '1970','R12': '1969','R16':'1965', 'R15': '1971','R17':'1973'}
    peugeot_model_start = {'RXX': '1960','403': '1955', '403B': '1958', '404': '1963', '504': '1969'}
    rover_model_start = {'RXX': '1960','75': '1954','90': '1954','P4': '1954','95': '1961','100': '1960','110': '1961','105R': '1955',\
                         '105S': '1955','2000': '1965', '2000TC': '1965', '3500': '1967','P5B': '1965','3L':'1960',\
                         'P5': '1959', 'P5Bcoupe': '1967', 'P5coupe': '1964'}
    rambler_model_start = {'Rambler': '1960','Ambassador': '1960', 'Hornet': '1970','Gremlin': '1970',\
                           'Rebel': '1967', 'Javelin': '1969', 'AMX': '1969', 'Matador':'1971',\
                           'American':'1963', 'Classic':'1961', 'Marlin':'1964', 'X-Coupe':'1975', 'RXX':'1960'}
    valiant_series_start = {'RXX': '1960', 'R': '1962', 'S': '1962', 'AP5': '1963', 'AP6': '1965', 'VC': '1966', 'VE': '1967', \
                            'VF':'1969', 'VG': '1970', 'VH':'1971', 'VJ':'1973', 'VK': '1975', 'CL':'1976', 'CM':'1978','CH':'1973','CJ':'1973', 'CK':'1975'}
    valiant_model_start = {'Utility':'1965', 'Regal': '1963', 'Charger': '1971', 'VIP': '1967', 'Safari': '1964', 'Ranger': '1971', \
                            'Chrysler':'1972', 'Valiant': '1962', 'Pacer':'1969', 'Hardtop':'1969','Wagon':'1966' }

    model_start_year = '1960'
    if make == 'Renault':
        model_start_year = renault_model_start[model]
    if make == 'Rambler':
        model_start_year = rambler_model_start[model]
    if make == 'Peugeot':
        model_start_year = peugeot_model_start[model]
    if make == 'Rover':
        model_start_year = rover_model_start[model]
    if model == 'Valiant':
        if sort3 > '5000' and sort3 != 'none':
          sort3 = '19' + sort3[0:2]

        if sort1 != "none":
            #print sort2 , target_plate
            model_start_year = valiant_series_start[sort1]
            #print model_start_year
        elif sort1 == "none"  and sort2 != "none":
            model_start_year = valiant_model_start[sort2]
            #print sort1, target_plate
            #print model_start_year
        elif sort1 == "none"  and sort2 == "none" and sort3 != "none":
            model_start_year = sort3
        #    print make, model, sort1, sort2, sort3, model_start_year,

    return  model_start_year


def check_plate_nsw3(target_plate, model_start_year):

    nsw_series_one = {'1955': 'AUG000', '1956': 'BCC000', '1957': 'BKC000', '1958': 'BSA000', '1959': 'BWA000', '1960': 'CAA000', '1961': 'CLL000', '1962': 'CSA000', '1963' : 'DAA000',
                    '1964': 'DAA000', '1965': 'DOJ000', '1966': 'EAA000', '1967': 'EMA000',
                      '1968': 'AEZ000', '1969': 'BAJ000', '1970': 'BZZ999'}

    #if target_plate == 'AFJ078':
    #    print "i'm here"
    year_list = list(nsw_series_one.keys())
    nsw_list = 0
    model_start_plate = "AAA000"
    nsw_era_4_start = "GAA000"
    nsw_era_4_end = "KZZ999"
    nsw_era_5_start = "FAA000"
    nsw_era_5_end = "FZZ999"
    nsw_era_6_start = "LAA000"
    nsw_era_2_end = "EZZ999"
    if model_start_year in year_list:
        model_start_plate = nsw_series_one[model_start_year]

    # got to era 3
    if (re.match('[A-E][I|Q][A-Z]', target_plate)) or (re.match('[A-E][A-Z][I|Q]', target_plate)) and target_plate < nsw_era_4_start:
        nsw_list = 3
    # go to era 4
    if target_plate >= nsw_era_4_start and target_plate <= nsw_era_4_end:
        nsw_list = 4
        #if target_plate == 'AFJ078':
        #    print "i'm here  nsw = 4"

    # check the F era 1979/1980
    if target_plate >= nsw_era_5_start and target_plate <= nsw_era_5_end:
        nsw_list = 5
        #if target_plate == 'AFJ078':
        #    print "i'm here  nsw = 5"

    # check > 1981
    if target_plate >= nsw_era_6_start:
        nsw_list = 6

    # go to era 1 after checking model introduction year , 1968 onwards is when repeats happened
    if (target_plate > model_start_plate and target_plate < nsw_era_2_end) \
            and nsw_list == 0 and model_start_year < '1969':
        nsw_list = 1
        #if target_plate == 'AFJ078':
        #    print "i'm here  nsw = 1" , model_start_year, model_start_plate, nsw_era_2_end

    # go to era 2 , the reuse era
    if nsw_list == 0:
        nsw_list = 2

    return  nsw_list


class RegoPlate(object):

    def __init__(self, title="", jurisdiction="NSW", make="", model="", model_level = "", model_code = "",
                 colour="", ad_index="", trim_level="", capacity="none", body_style = "none", interior_trim = "none",
                 car_year="none", year_predict="1999", nsw_epoch=7, transmission="none"):

        self.title = title
        self.jurisdiction = jurisdiction
        self.make = make
        self.model = model
        self.model_level = model_level
        self.model_code = model_code
        self.trim_level = trim_level
        self.colour = colour
        self.interior_trim = interior_trim
        self.capacity = capacity
        self.body_style = body_style
        self.ads_list = [ad_index]
        self.year = car_year
        self.year_predict = year_predict
        self.nsw_epoch = nsw_epoch
        self.transmission = transmission

    def set_year_predict(self, year_predict):
        self.year_predict = year_predict
    def set_year(self, year):
        if year != 'none':
            self.year = year
    def set_colour(self, colour):
        if colour != 'unknown':
            self.colour = colour

    def set_capacity(self, capacity):
      if capacity != 'none':
        self.capacity = capacity
    def set_interior_trim(self, interior_trim):
      if interior_trim != 'none':
        self.interior_trim = interior_trim


    def get_year_predict(self):
        return self.year_predict

    def set_nsw_epoch(self, nsw_epoch):
        self.nsw_epoch = nsw_epoch

    def get_nsw_epoch(self):
        return self.nsw_epoch

    def grow_ad_list(self,ad_index):
        self.ads_list.append(ad_index)

    def print_plate(self):
        if self.colour == "unknown":
            self.colour = ""
        if self.model == "none":
            self.model = ""
        if self.transmission == "none":
            self.transmission = ""


        description = self.make

        if self.model == "Valiant":
            description = self.model
            if self.model_code != "none":
                description = self.model_code + " " + description
            if self.model_level != "Valiant" and self.model_level != "none":
                description = description + " " + self.model_level
            if self.trim_level != "none":
                description = description + " " + self.trim_level
            if self.body_style != "none" and self.body_style != "Sedan":
                description = description + " " + self.body_style
            if self.capacity != "none":
                description = description + " " + self.capacity



        if self.model == "P76":
            description = description + " " + self.model
            if self.trim_level != "none":
                description = description + " " + self.trim_level
            if self.capacity != "none":
                description = description + " " + self.capacity


        if self.make == "Rover":
            if self.model != "none":
                description  = description  + " " + self.model + " " + self.transmission



        if self.make == "Peugeot":
            if self.model != 'none':
                description = description + " " + self.model


        if self.make == "Renault":
            if self.model != 'RXX':
                description = description + " " + self.model
            if self.trim_level != "XX":
                description = description + " " + self.trim_level


        if self.make == "Rambler":
            if self.model != "none" or self.model != "Rambler":
                description = description+ " " + self.model
            if self.trim_level != "none":
                description = description + " " + self.trim_level
            if self.capacity != "none":
                description = description + " " + self.capacity

        colour_description = ""
        if self.colour != "unknown":
            colour_description = self.colour
        if self.interior_trim != "none":
            colour_description = colour_description + " with " + self.interior_trim + " Trim"

        if self.year != "none":
            description = self.year + " " + description


        no_of_ads_string = ""
        no_of_ads = len(self.ads_list)
        if no_of_ads > 1:
            no_of_ads_string = str(no_of_ads)
        estimate_month = get_month(self.title)
        if estimate_month == "none":
            estimate_month = ""

        print ('{0:6} | {1:2} | {2:7} | {3:40} | {4:30}' \
               .format(self.title, no_of_ads_string, estimate_month, description, colour_description ))



class Advertisement(object):

    def __init__(self, title="", jurisdiction="NSW", make="", model="", model_level = "", model_code = "",
                 colour="", phone1="", ad_index="", trim_level="", capacity="", body_style="", interior_trim="none",
                 car_year="none", month="none", ad_date="", year_predict="1999", suburb="none", price="$$$", milage="none", transmission="none"):

        self.title = title
        self.jurisdiction = jurisdiction
        self.make = make
        self.model = model
        self.model_level = model_level
        self.model_code = model_code
        self.trim_level = trim_level
        self.interior_trim = interior_trim
        self.colour = colour
        self.capacity = capacity
        self.body_style = body_style
        self.phone1 = phone1
        self.index = ad_index
        self.year = car_year
        self.month = month
        self.ad_date = ad_date
        self.year_predict = year_predict
        self.suburb = suburb
        self.price = price
        self.milage = milage
        self.transmission = transmission

    def set_suburb(self):
        exchange_dictionary = get_exchange_dict()
        number = self.phone1
        prefix = '000'
        if len(number) == 5:
            prefix = number[:1]
        if len(number) == 6:
            prefix = number[:2]
        if len(number) == 7:
            prefix = number[:3]
        exchange_list = list(exchange_dictionary.keys())
        if prefix in exchange_list:
            self.suburb = exchange_dictionary[prefix]
        else:
            self.suburb = ''

    def print_ad(self):
        months = "January", "February", "March", "April", "May", "June", "July", \
                 "August", "September", "October", "November", "December"
        if str(self.month) not in months:
            self.month = ""
        if self.colour == "unknown":
            self.colour = ""
        if self.price == "none":
            self.price = ""
        if self.transmission == "none":
            self.transmission = ""

        description = self.make


        if self.model == "Valiant":
            description = self.model
            if self.model_code != "none":
                description = self.model_code + " " + description
            if self.model_level != "Valiant" and self.model_level != "none":
                description = description + " " + self.model_level
            if self.trim_level != "none":
                description = description + " " + self.trim_level
            if self.body_style != "none" and self.body_style != "Sedan":
                description = description + " " + self.body_style
            if self.capacity != "none":
                description = description + " " + self.capacity


        if self.model == "P76":
            description = description + " " + self.model
            if self.trim_level != "none":
                description = description + " " + self.trim_level
            if self.capacity != "none":
                description = description + " " + self.capacity


        if self.make == "Rover":
            if self.model != "none":
                description  = description  + " " + self.model + " " + self.transmission

        if self.make == "Peugeot":
            if self.model != "none":
                description =  description + " " + self.model

        if self.make == "Renault":
            if self.model != 'RXX':
                description = description + " " + self.model
            if self.trim_level != "XX":
                description = description + " " + self.trim_level

        if self.make == "Rambler":
            if self.model != "none" or self.model != "Rambler":
                description = description  + " " + self.model
            if self.trim_level != "none":
                description = description + " " + self.trim_level
            if self.capacity != "none":
                description = description + " " + self.capacity

        if self.milage != "none":
            description = description + " " + self.milage
        if self.year != "none":
            description = self.year + " " + description


        print ('{0:6} {1:3} {2:10} {3:35} {4:16} {5:7} {6:11} {7:20}' \
               .format(self.title, self.month[0:3], self.ad_date, description, self.colour, \
                        self.price, self.phone1, self.suburb))




def get_sql_data(car_model_list, **kwargs):
    #  print kwargs
    jurisdiction = kwargs["jurisdiction"]
    connectstring = kwargs["connectstring"]
    car_make = kwargs["car_make"]
    stop = len(car_model_list)
    car_model_or_string = "(car_model = '{}'".format(car_model_list[0])
    for x in range(1, stop):
        car_model_or_string += " or " + "car_model = '{}'".format(car_model_list[x])
    #      print car_model_list[x]
    car_model_or_string += " )"
    #     sql = "select * from adverts"
    #  car_model_string = "car_model = '{}'".format(car_model_list[0])
    sql = "select * from adverts where {0} and jurisdiction = '{1}'  and car_make = '{2}'".format(
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

def get_sql_data_rambler(car_model_list, **kwargs):
    #  print kwargs
    jurisdiction = kwargs["jurisdiction"]
    connectstring = kwargs["connectstring"]
    car_make = kwargs["car_make"]
    stop = len(car_model_list)
    if stop == 1 and car_model_list[0] == "Wagon":
        sql = "select * from adverts where car_make = 'Rambler' and body_style = 'Wagon' and jurisdiction = 'NSW'"
    else:
      car_model_or_string = "( car_model = '{}'".format(car_model_list[0])
      for x in range(1, stop):
        car_model_or_string += " or " + "car_model = '{}'".format(car_model_list[x])
      car_model_or_string += " )"
    #     sql = "select * from adverts"
    #  car_model_string = "car_model = '{}'".format(car_model_list[0])
      sql = "select * from adverts where {} and jurisdiction = '{}'".format(
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



def get_sql_data_mascot(car_model_list, **kwargs):
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
    sql = "select * from adverts where {} and jurisdiction = '{}' and car_make = '{}' and phone1 = '6672484'".format(
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


def get_sql_data_series(car_model_list, **kwargs):
    #  print kwargs
    jurisdiction = kwargs["jurisdiction"]
    connectstring = kwargs["connectstring"]
    car_make = kwargs["car_make"]
    stop = len(car_model_list)
    car_model_or_string = "( model_code = '{}'".format(car_model_list[0])
    for x in range(1, stop):
        car_model_or_string += " or " + "model_code = '{}'".format(car_model_list[x])
    #      print car_model_list[x]
    car_model_or_string += " )"
    #     sql = "select * from adverts"
    #  car_model_string = "car_model = '{}'".format(car_model_list[0])
    sql = "select * from adverts where {} and jurisdiction = '{}' and car_make = '{}'".format(
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



def get_sql_data_all( **kwargs):
    #  print kwargs
    jurisdiction = kwargs["jurisdiction"]
    connectstring = kwargs["connectstring"]
   #     sql = "select * from adverts"
    sql = "select * from adverts where jurisdiction = '{}' ".format(jurisdiction)

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


def get_sql_data_state( **kwargs):
    #  print kwargs
    jurisdiction = kwargs["jurisdiction"]
    connectstring = kwargs["connectstring"]
   #     sql = "select * from adverts"
    sql = "select * from adverts where jurisdiction = '{}' ".format(jurisdiction)

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



def main():
  plate_list = []
  ads_list = []

  go_again = 'y'
  pick_make = 'none'
  while go_again != 'n':
    while True:
        Make_list = ["Rambler", "Renault", "Peugeot", "Rover", "Ford", "Mascot", "Valiant", "Leyland"]
        print Make_list
        pick_make = "Wally"
        pick_make = raw_input("Car Make?")
        print pick_make
        print go_again
        if pick_make == "ra" or pick_make == "Rambler":
            Rambler_list = ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American",
                            "AMX", "Marlin", "X-Coupe","Wagon"]
            print Rambler_list
            pick_model = raw_input("please enter Rambler model: ")
         #   if pick_model == "all":
         #       Rambler_list = ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American",
         #                   "AMX", "Marlin", "none","X-Coupe", "Rambler"]
            if pick_model in Rambler_list:
                Rambler_list = [pick_model]


            ads_table = get_sql_data_rambler(car_model_list=Rambler_list, car_make="Rambler", connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW")
            break
        if  pick_make == "Mascot":
            Rambler_list = ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American",
                            "AMX", "Marlin", "X-Coupe","Wagon"]
            print Rambler_list
            pick_model = raw_input("please enter Rambler model: ")
            if pick_model == "all":
                Rambler_list = ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American",
                            "AMX", "Marlin", "none","X-Coupe"]
            if pick_model in Rambler_list:
                Rambler_list = [pick_model]
            ads_table = get_sql_data_mascot(car_model_list=Rambler_list, car_make="Rambler", connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW")
            break

        elif pick_make == "fo" or pick_make == "Ford":
            Ford_list = ["Falcon", "Cortina", "Capri"]
            ads_table = get_sql_data(car_model_list=Ford_list, car_make="Ford", connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW")
            break
        elif pick_make == "re" or pick_make == "Renault":
            Renault_list = ["R4", "R8", "R10", "R12", "R16", "R10S", "10S", "R15", "R17", "RXX"]
            print Renault_list
            pick_model = raw_input("please enter Renault model: ")
            if pick_model != "all":
                Renault_list = [pick_model]
            ads_table = get_sql_data(car_model_list=Renault_list, car_make ="Renault", connectstring="advertisements_indexed.db",
                                   jurisdiction="NSW")
            break
        elif pick_make == "pe" or pick_make == "Peugeot":
            Peugeot_list = ["403", "403B", "404", "504"]
            print Peugeot_list
            pick_model = raw_input("please enter Peugeot model: ")
            if pick_model == "all":
                Peugeot_list = ["403", "403B", "404", "504", "none"]
            ads_table = get_sql_data(car_model_list=Peugeot_list, car_make ="Peugeot", connectstring="advertisements_indexed.db",
                                   jurisdiction="NSW")
            break
        elif pick_make == "ro" or pick_make == "Rover":
            Rover_list = ["105R","105S", "2000", "2000TC", "3500", "P5B", "P5", "P5Bcoupe", "P5coupe","3L", "100"]
            print Rover_list
            pick_model = raw_input("please enter Rover model: ")
            if pick_model != "all":
                Rover_list = [pick_model]
            else:
                Rover_list = ["75","90","105R","105S","2000", "2000TC", "3500", "P5B", "P5", "P5Bcoupe", "P5coupe","3L", "100", "none"]
            ads_table = get_sql_data(car_model_list=Rover_list, car_make ="Rover", connectstring="advertisements_indexed.db",
                                   jurisdiction="NSW")
            break
        elif pick_make == "Leyland":
            Leyland_list = ["P76"]
            ads_table = get_sql_data(car_model_list=Leyland_list, car_make ="Leyland", connectstring="advertisements_indexed.db",
                                   jurisdiction="NSW")
            break
        elif pick_make == "val" or pick_make == "Valiant":
            Valiant_list = ["R", "S", "AP5", "AP6", "VC", "VE", "VF", "VG", "VH", "VJ", "VK", "CL", "CM"]
            print Valiant_list
            pick_model = raw_input("please enter Valiant series: ")
            if pick_model != "all":
                Valiant_list = [pick_model]
            else:
                Valiant_list = ["none","R", "S", "AP5", "AP6", "VC", "VE", "VF", "VG", "VH", "VJ", "VK", "CL", "CM"]

            ads_table = get_sql_data_series(car_model_list=Valiant_list, car_make="Chrysler", connectstring="advertisements_indexed.db",
                                   jurisdiction="NSW")
            break

        elif pick_make == "all":
            ads_table = get_sql_data_all( connectstring="advertisements_indexed.db", jurisdiction="NSW")
            break
        elif pick_make == "NSW" or pick_make == "VIC" or pick_make == "QLD":
            ads_table = get_sql_data_state( connectstring="advertisements_indexed.db",jurisdiction=pick_make )
            break
        elif pick_make == 'x':
            break
        else:
            print "try again"
    print "finished sql query"
    ###### process data but can gather more


    plate_list_index = []
    no_of_cars = 0
    already_found = 0
    ads_dict = {}
    for ads_record in ads_table:  # we make a lists of database indexes for distinct plate numbers, insert into dictionary
        plate = str(ads_record[1])
        jurisdiction = ads_record[2]
        ad_date = ads_record[3]
        publication = ads_record[5]
        make = ads_record[6]
        model = ads_record[7]
        colour = ads_record[10]
        phone1 = ads_record[11]
        ads_master_index = ads_record[0]
        if ads_master_index not in ads_list:
            ads_list.append(ads_master_index)
            new_ad = Advertisement(ad_index=ads_master_index, title=ads_record[1], jurisdiction=jurisdiction,
                                  make=make, model_code=ads_record[20], trim_level=ads_record[17],
                                  model=model, colour=colour, phone1=phone1,
                                  car_year=ads_record[8], capacity=ads_record[9], body_style=ads_record[16],
                                  model_level=ads_record[24], interior_trim=ads_record[15],
                                  month=ads_record[21], ad_date=ads_record[3], price=ads_record[18],milage=ads_record[19],transmission=ads_record[22] )
            new_ad.set_suburb()
            ads_dict[ads_master_index] = new_ad
        #        if re.match('^[A-Q][A-Z][A-Z][0-9]{3}', plate):  # check valid plate
        if re.match('^[A-Q][A-Z][A-Z][0-9]{3}', plate) or  re.match('^[A-Z][A-Z][0-9]{3}', plate):# check valid plate

            if plate not in plate_list_index:
                new_plate = RegoPlate(ad_index=ads_master_index, title=ads_record[1], jurisdiction=ads_record[2],
                                      make=ads_record[6], model_code=ads_record[20], trim_level=ads_record[17],
                                      model=ads_record[7], colour=ads_record[10],
                                      car_year=ads_record[8], capacity=ads_record[9], body_style=ads_record[16],
                                      model_level=ads_record[24], interior_trim=ads_record[15],transmission=ads_record[22])

                no_of_cars = no_of_cars +1
                # new_plate.set_suburb(ads_record[11])
                if new_plate.jurisdiction == "NSW":
                  if not re.match('^[A-Z][A-Z][0-9]{3}', plate):
                    return_above = check_production( make=ads_record[6], model=ads_record[7], sort1=ads_record[20],sort2=ads_record[24], sort3=ads_record[8])
                    nsw_list = check_plate_nsw3(target_plate=ads_record[1], model_start_year=return_above)
                    new_plate.set_year_predict("1999")
                    new_plate.set_nsw_epoch(nsw_list)
                  else:
                    new_plate.set_nsw_epoch(7)  # for personal plates 5 digit match
                if new_plate.jurisdiction == "VIC" or new_plate.jurisdiction == "QLD":
                    new_plate.set_nsw_epoch(7)  # for personal plates 5 digit match

                plate_list.append(new_plate)
                plate_list_index.append(plate)
            else:
                already_found = already_found + 1
                for plate_stored in plate_list:
                    if plate_stored.title == plate:
                         plate_stored.set_year(ads_record[8])
                         plate_stored.set_colour(ads_record[10])
                         plate_stored.grow_ad_list(ads_record[0])
#                         if ads_record[10] != "unknown":
#                             plate_stored.colour = ads_record[10]
                         if ads_record[15] != "none":
                             plate_stored.set_interior_trim(ads_record[15])
                         if ads_record[9] != "none":
                             plate_stored.capacity = ads_record[9]
        elif (plate == model) or (plate == make): # Dont create a plate object
            print make, model, colour,publication,ad_date, phone1, jurisdiction


    print "no of cars =" , no_of_cars , "no_of_ads =" , no_of_cars + already_found
    if pick_make == 'all':
        break
    go_again = raw_input("Go Again y/n: ")

  plate_list.sort()
  for x in range(1, 8):
      print "*" * 80
      for plate_stored in sorted(plate_list, key=lambda plate: plate.title):
          nsw_epoch = plate_stored.get_nsw_epoch()
          # suburb = plate_stored.set_suburb()
          if x == int(nsw_epoch):  # there are 4 nsw plate lists
              plate_stored.print_plate()
  # ads_dict = []
  go_again = 'y'
  pick_make = 'none'
  while go_again != 'n':
      while True:
          plate_search = raw_input("Enter Plate number or q for quit: ")
          if plate_search != 'q':
              prefix_search_flag = False
              plate_selected = {}
              if plate_search == "number" or plate_search == "n":
                  number_search = raw_input("Enter Phone number: ")
                  if number_search in dealers_list:
                          dealer_data = dealers_list[number_search]
                          dealer_street = dealer_data[1]
                          dealer_licence = dealer_data[3]
                          dealer_name = dealer_data[0]
                          dealer_suburb = dealer_data[2]
                          if dealer_suburb != "unknown":
                              print dealer_name, dealer_street, dealer_suburb, dealer_licence
                          else:
                              print number_search, dealer_name, dealer_licence
                  for ad2 in ads_list:
                      advert = ads_dict[ad2]
                      if advert.phone1 == number_search:
                          advert.print_ad()


              else:
                  if len(plate_search) == 3 or len(plate_search) == 2:
                      prefix_search_flag = True
                  for ad in ads_list:
                      advert = ads_dict[ad]
                      if prefix_search_flag:
                          if advert.title[:3] == plate_search or advert.title[:2] == plate_search or advert.title[:4] == plate_search:
                              plate_selected[advert.ad_date] = advert
                      else:
                          if advert.title == plate_search:
                              plate_selected[advert.ad_date] = advert
                  for key in sorted(plate_selected):
                      plate_selected[key].print_ad()
                  go_again = plate_search
          else:
              plate_search = "wally"
              go_again = 'n'
              break


if __name__ == '__main__':
    main()
