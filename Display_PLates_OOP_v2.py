import sqlite3
import re
from collections import defaultdict
from sydney_exchange import get_exchange_dict
from datetime import datetime
from NSW_Plate_Info import get_month



def check_production( make, model, sort1, sort2, sort3):
    if model == 'none' and make != 'Chrysler':
        model = "RXX"
    renault_model_start = {'RXX': '1960','R4': '1958', 'R8': '1961','Gordini': '1963', 'R10': '1965', 'R10S': '1970','R12': '1969','R16':'1965', 'R15': '1971','R17':'1973'}
    peugeot_model_start = {'RXX': '1960','403': '1955', '403B': '1958', '404': '1963', '504': '1969'}
    rover_model_start = {'RXX': '1960','75': '1954','90': '1954','P4': '1954','100': '1960','105R': '1955',\
                         '2000': '1965', '2000TC': '1965', '3500': '1967','P5B': '1965','3L':'1960',\
                         'P5': '1961', 'P5Bcoupe': '1965', 'P5coupe': '1965'}
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
      # if sort3 > '1961' and sort3 < '1981':
      #  model_start_year = sort3
      # else:
        if sort1 == "none":
            #print sort2 , target_plate
            model_start_year = valiant_model_start[sort2]
            #print model_start_year
        else:
            model_start_year = valiant_series_start[sort1]
            #print sort1, target_plate
            #print model_start_year

    return  model_start_year


def check_plate_nsw2(target_plate, model_start_year):

    nsw_series_one = {'1955': 'AUG000', '1956': 'BCC000', '1957': 'BKC000', '1958': 'BSA000', '1959': 'BWA000', '1960': 'CAA000', '1961': 'CLL000', '1962': 'CSA000', '1963' : 'DAA000',
                    '1964': 'DAA000', '1965': 'DOJ000', '1966': 'EAA000', '1967': 'EMA000',
                      '1968': 'AEZ000', '1969': 'BAJ000', '1970': 'BZZ999'}

    year_list = list(nsw_series_one.keys())
    nsw_list = 0
    model_start_plate = "AUG001"
    nsw_era_4_start = "GAA000"
    nsw_era_2_end = "EZZ999"
    if model_start_year in year_list:
        model_start_plate = nsw_series_one[model_start_year]

    # got to era 3
    if (re.match('[A-E][I|Q][A-Z]', target_plate)) or (re.match('[A-E][A-Z][I|Q]', target_plate)) and target_plate < nsw_era_4_start:
        nsw_list = 3
    # got to era 4
    if target_plate >= nsw_era_4_start:
        nsw_list = 4
    # go to era 1 after checking model introduction year
    if (target_plate > model_start_plate and target_plate < nsw_era_2_end) \
            and nsw_list == 0 and model_start_year < "1969":
        nsw_list = 1
    # go to era 2 , the reuse era
    if nsw_list == 0:
        nsw_list = 2

    return  nsw_list


class RegoPlate(object):

    def __init__(self, title="", jurisdiction="NSW", make="", model="", model_level = "", model_code = "",
                 colour="", phone1="", ad_index="", trim_level="",
                 car_year="", month="None", ad_date="", year_predict="1999", nsw_epoch=7, suburb="wallyville", price="$$$"):

        self.title = title
        self.jurisdiction = jurisdiction
        self.make = make
        self.model = model
        self.model_level = model_level
        self.model_code = model_code
        self.trim_level = trim_level
        self.colour = colour
        self.phone1 = phone1
        self.ads_list = [ad_index]
        self.index = ad_index
        self.year = car_year
        self.month = month
        self.ad_date = ad_date
        self.year_predict = year_predict
        self.nsw_epoch = nsw_epoch
        self.suburb = suburb
        self.price = price

    def set_year_predict(self, year_predict):
        self.year_predict = year_predict

    def get_year_predict(self):
        return self.year_predict

    def set_nsw_epoch(self, nsw_epoch):
        self.nsw_epoch = nsw_epoch

    def get_nsw_epoch(self):
        return self.nsw_epoch

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

    def grow_ad_list(self,ad_index):
        self.ads_list.append(ad_index)

    def print_plate(self):
        months = "January", "February", "March", "April", "May", "June", "July", \
                 "August", "September", "October", "November", "December"
        if str(self.month) not in months:
            self.month = ""
        if self.colour == "unknown":
            self.colour = ""
        if self.year == "none":
            self.year = ""
        if self.model == "none":
            self.model = ""
        if self.price == "none":
            self.price = ""
        if self.model == "Valiant" and self.model_level != "none":
            if self.model_code != "none":
                self.model = self.model_code + " " + self.model_level
            else:
                self.model = self.model_level
            if self.trim_level != "none":
                self.model = self.model + " " + self.trim_level

        if self.model == "P76" and self.trim_level != "none":
            if self.trim_level != "none":
                self.model = self.model + " " + self.trim_level

        if self.make == "Rover":
            if self.model != "none":
                self.model = self.make + " " + self.model

        if self.make == "Peugeot":
            if self.model != "none":
                self.model = self.make + " " + self.model

        if self.make == "Renault":
            if self.model != 'RXX':
                self.model = self.make + " " +self.model
            else:
                self.model = self.make
                if self.trim_level != "XX":
                    self.model = self.model + " " + self.trim_level

        if self.make == "Rambler":
            if self.model != "none":
                self.model = self.make + " " + self.model
            if self.trim_level != "none" and self.model != 'none':
                self.model = self.model + " " + self.trim_level



        no_of_ads = len(self.ads_list)
        estimate_month = get_month(self.title)
        if estimate_month == "none":
            estimate_month = ""

 #       print ('{0:6} | {1:2} | {2:4} | {3:7} | {4:9} | {5:20} | {6:5} |{7:20} | {8:11} | {9:30} | {10:10} | {11:4}| {12:4}' \
  #             .format(self.title, no_of_ads, self.year, estimate_month, self.month, self.model, self.price, self.colour, self.ad_date,\
   #                    self.suburb, self.phone1, self.make, self.index ))
        print ('{0:6} | {1:2} | {2:4} | {3:20} | {4:5} |{5:20} | {6:11} | {7:30} | {8:10} | {9:4}| {10:4}' \
               .format(self.title, no_of_ads, self.year, self.model, self.price, self.colour, self.ad_date,\
                       self.suburb, self.phone1, self.make, self.index ))



class Advertisement(object):

    def __init__(self, title="", jurisdiction="NSW", make="", model="", model_level = "", model_code = "",
                 colour="", phone1="", ad_index="", trim_level="",
                 car_year="", month="None", ad_date="", year_predict="1999", nsw_epoch=7, suburb="wallyville", price="$$$"):

        self.title = title
        self.jurisdiction = jurisdiction
        self.make = make
        self.model = model
        self.model_level = model_level
        self.model_code = model_code
        self.trim_level = trim_level
        self.colour = colour
        self.phone1 = phone1
        self.ads_list = [ad_index]
        self.index = ad_index
        self.year = car_year
        self.month = month
        self.ad_date = ad_date
        self.year_predict = year_predict
        self.nsw_epoch = nsw_epoch
        self.suburb = suburb
        self.price = price

    def set_year_predict(self, year_predict):
        self.year_predict = year_predict

    def get_year_predict(self):
        return self.year_predict

    def set_nsw_epoch(self, nsw_epoch):
        self.nsw_epoch = nsw_epoch

    def get_nsw_epoch(self):
        return self.nsw_epoch

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

    def grow_ad_list(self,ad_index):
        self.ads_list.append(ad_index)

    def print_plate(self):
        months = "January", "February", "March", "April", "May", "June", "July", \
                 "August", "September", "October", "November", "December"
        if str(self.month) not in months:
            self.month = ""
        if self.colour == "unknown":
            self.colour = ""
        if self.year == "none":
            self.year = ""
        if self.model == "none":
            self.model = ""
        if self.price == "none":
            self.price = ""
        if self.model == "Valiant" and self.model_level != "none":
            if self.model_code != "none":
                self.model = self.model_code + " " + self.model_level
            else:
                self.model = self.model_level
            if self.trim_level != "none":
                self.model = self.model + " " + self.trim_level

        if self.model == "P76" and self.trim_level != "none":
            if self.trim_level != "none":
                self.model = self.model + " " + self.trim_level

        if self.make == "Rover":
            if self.model != "none":
                self.model = self.make + " " + self.model

        if self.make == "Peugeot":
            if self.model != "none":
                self.model = self.make + " " + self.model

        if self.make == "Renault":
            if self.model != 'RXX':
                self.model = self.make + " " +self.model
            else:
                self.model = self.make
                if self.trim_level != "XX":
                    self.model = self.model + " " + self.trim_level

        if self.make == "Rambler":
            if self.model != "none":
                self.model = self.make + " " + self.model
            if self.trim_level != "none" and self.model != 'none':
                self.model = self.model + " " + self.trim_level



        no_of_ads = len(self.ads_list)
        estimate_month = get_month(self.title)
        if estimate_month == "none":
            estimate_month = ""

#        print ('{0:6} | {1:2} | {2:4} | {3:7} | {4:9} | {5:20} | {6:5} |{7:20} | {8:11} | {9:30} | {10:10} | {11:4}| {12:4}' \
#              .format(self.title, no_of_ads, self.year, estimate_month, self.month, self.model, self.price, self.colour, self.ad_date,\
#                      self.suburb, self.phone1, self.make, self.index ))

        print ('{0:6} | {1:2} | {2:4} | {3:20} | {4:5} |{5:20} | {6:11} | {7:30} | {8:10} | {9:4}| {10:4}' \
               .format(self.title, no_of_ads, self.year, self.model, self.price, self.colour, self.ad_date,\
                       self.suburb, self.phone1, self.make, self.index ))



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



def main():
  plate_list = []
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
                            "AMX", "Marlin", "X-Coupe"]
            print Rambler_list
            pick_model = raw_input("please enter Rambler model: ")
            if pick_model == "all":
                Rambler_list = ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American",
                            "AMX", "Marlin", "none","X-Coupe"]
            if pick_model in Rambler_list:
                Rambler_list = [pick_model]
            ads_table = get_sql_data(car_model_list=Rambler_list, car_make="Rambler", connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW")
            break
        if  pick_make == "Mascot":
            Rambler_list = ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American",
                            "AMX", "Marlin", "X-Coupe"]
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
            Rover_list = ["105R", "2000", "2000TC", "3500", "P5B", "P5", "P5Bcoupe", "P5coupe","3L", "100"]
            print Rover_list
            pick_model = raw_input("please enter Rover model: ")
            if pick_model != "all":
                Rover_list = [pick_model]
            else:
                Rover_list = ["75","90","105R", "2000", "2000TC", "3500", "P5B", "P5", "P5Bcoupe", "P5coupe","3L", "100", "none"]
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
        elif pick_make == 'x':
            break
        else:
            print "try again"
    print "finished sql query"
    plate_list_index = []
    no_of_cars = 0
    already_found = 0
    for ads_record in ads_table:  # we make a lists of database indexes for distinct plate numbers, insert into dictionary
        plate = str(ads_record[1])

#        if re.match('^[A-Q][A-Z][A-Z][0-9]{3}', plate):  # check valid plate
        if re.match('^[A-Q][A-Z][A-Z][0-9]{3}', plate) or  re.match('^[A-Z][A-Z][0-9]{3}', plate):# check valid plate

            if plate not in plate_list_index:
                new_plate = RegoPlate(ad_index=ads_record[0], title=ads_record[1], jurisdiction=ads_record[2],
                                      make=ads_record[6], model_code=ads_record[20], trim_level=ads_record[17],
                                      model=ads_record[7], colour=ads_record[10], phone1=ads_record[11],
                                      car_year=ads_record[8], model_level=ads_record[24],
                                      month=ads_record[21], ad_date=ads_record[3], price=ads_record[18],)
                no_of_cars = no_of_cars +1

                if new_plate.jurisdiction == "NSW":
                  if not re.match('^[A-Z][A-Z][0-9]{3}', plate):
                    return_above = check_production( make=ads_record[6], model=ads_record[7], sort1=ads_record[20],sort2=ads_record[24], sort3=ads_record[8])
                    nsw_list = check_plate_nsw2(target_plate=ads_record[1], model_start_year=return_above)
                    new_plate.set_year_predict("1999")
                    new_plate.set_nsw_epoch(nsw_list)
                  else:
                    new_plate.set_nsw_epoch(5)  # for personal plates 5 digit match

                plate_list.append(new_plate)
                plate_list_index.append(plate)
            else:
                already_found = already_found + 1
                for plate_stored in plate_list:
                    if plate_stored.title == plate:
                         plate_stored.grow_ad_list(ads_record[0])
    print "no of cars =" , no_of_cars , "no_of_ads =" , no_of_cars + already_found
    if pick_make == 'all':
        break
    go_again = raw_input("Go Again y/n: ")

  plate_list.sort()
  for x in range(1, 6):
      print "*" * 140
      for plate_stored in sorted(plate_list, key=lambda plate: plate.title):
          nsw_epoch = plate_stored.get_nsw_epoch()
          suburb = plate_stored.set_suburb()
          if x == int(nsw_epoch):  # there are 4 nsw plate lists
              plate_stored.print_plate()




if __name__ == '__main__':
    main()
