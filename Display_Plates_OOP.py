import sqlite3
import re
from collections import defaultdict
from sydney_exchange import get_exchange_dict
from datetime import datetime
from NSW_Plate_Info import get_month



def check_plate_nsw2(target_plate, model, make):

    renault_model_start = {'RXX': '1960', 'R8': '1963', 'R10': '1965', 'R10S': '1970','R12': '1969', 'R16':'1965','R17':'1973'}
    peugeot_model_start = {'403': '1955', '403B': '1958', '404': '1963', '504': '1969'}
    rover_model_start = {'100': '1960', '2000': '1965', '2000TC': '1965', '3500': '1967','P5B': '1965', 'P5': '1965', 'P5Bcoupe': '1965', 'P5coupe': '1965'}
    rambler_model_start = {'Ambassador': '1960', 'Hornet': '1970','Gremlin': '1970', 'Rebel': '1967', 'Javelin': '1969', 'AMX': '1969', 'Matador':'1971', 'American':'1963', 'Classic':'1961'}
    model_start_year = '1960'
    if make == 'Renault':
        model_start_year = renault_model_start[model]
    if make == 'Rambler':
        model_start_year = rambler_model_start[model]
    if make == 'Peugeot':
        model_start_year = peugeot_model_start[model]
    if make == 'Rover':
        model_start_year = rover_model_start[model]

    nsw_series_one = {'1955': 'AUG000', '1956': 'BCC000', '1957': 'BKC000', '1958': 'BSA000', '1959': 'BWA000', '1960': 'CAA000', '1961': 'CLL000', '1962': 'CTA000', '1963' : 'DAA000',
                    '1964': 'DKA000', '1965': 'DOJ000', '1966': 'EDA000', '1967': 'EMA000',
                      '1968': 'AAA000', '1969': 'BAJ000', '1970': 'BZZ999'}

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

    def __init__(self, title="", jurisdiction="NSW", make="", model="", colour="", phone1="", ad_index="",
                 car_year="", month="None", ad_date="", year_predict="1999", nsw_epoch=7, suburb="wallyville"):

        self.title = title
        self.jurisdiction = jurisdiction
        self.make = make
        self.model = model
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
        no_of_ads = len(self.ads_list)
        estimate_month = get_month(self.title)
        if estimate_month == "none":
            estimate_month = ""

        #print " {title} {year} {make} {model} {index}".format(index=self.index, title=self.title, year=self.year, make=self.make, model=self.model)
#        print ('{0:6} | {1:4} | {2:9} | {3:8} | {4:10} | {5:20} | {6:11} | {7:16} | {8:10} | {9:4}| {10:4} | {11:4}'.format(self.title, self.year, self.month,
#                self.make, self.model, self.colour, self.phone1, self.suburb, self.ad_date, self.year_predict, self.index, no_of_ads))

        print ('{0:6} | {1:2} | {2:4} | {3:7} | {4:9} | {5:10} | {6:20} | {7:11} | {8:30} | {9:10} | {10:4}| {11:4}' \
               .format(self.title, no_of_ads, self.year, estimate_month, self.month, self.model, self.colour, self.ad_date,\
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




def main():
  plate_list = []
  go_again = 'y'
  while go_again != 'n':
    while True:
        Make_list = ["Rambler", "Renault", "Peugeot", "Rover", "Ford", "Mascot"]
        print Make_list
        pick_make = "Wally"
        pick_make = raw_input("Car Make?")
        print pick_make
        print go_again
        if pick_make == "ra" or pick_make == "Rambler":
            Rambler_list = ["Gremlin", "Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American",
                            "AMX"]
            print Rambler_list
            pick_model = raw_input("please enter Rambler model: ")
            if pick_model != "all":
                Rambler_list = [pick_model]
            ads_table = get_sql_data(car_model_list=Rambler_list, car_make="Rambler", connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW")
            break
        elif pick_make == "fo" or pick_make == "Ford":
            Ford_list = ["Falcon", "Cortina", "Capri"]
            ads_table = get_sql_data(car_model_list=Ford_list, car_make="Ford", connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW")
            break
        elif pick_make == "re" or pick_make == "Renault":
            Renault_list = ["R8", "R10", "R12", "R16", "R10S", "10S", "R17", "RXX"]
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
            if pick_model != "all":
                Peugeot_list = [pick_model]
            ads_table = get_sql_data(car_model_list=Peugeot_list, car_make ="Peugeot", connectstring="advertisements_indexed.db",
                                   jurisdiction="NSW")
            break
        elif pick_make == "ro" or pick_make == "Rover":
            Rover_list = ["2000", "2000TC", "3500", "P5B", "P5", "P5Bcoupe", "P5coupe", "100"]
            print Rover_list
            pick_model = raw_input("please enter Rover model: ")
            if pick_model != "all":
                Rover_list = [pick_model]
            ads_table = get_sql_data(car_model_list=Rover_list, car_make ="Rover", connectstring="advertisements_indexed.db",
                                   jurisdiction="NSW")
            break
        elif pick_make == "mm" or pick_make == "Mascot":
            Rambler_list = ["Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American", "AMX"]
            print Rambler_list
            pick_model = raw_input("please enter Rambler/AMC model: ")
            if pick_model != "all":
                Rambler_list = [pick_model]
            ads_table = get_sql_data_mascot(car_model_list=Rambler_list, car_make ="Rambler", connectstring="advertisements_indexed.db",
                                     jurisdiction="NSW")
            break
        elif pick_make == 'x':
            break
        else:
            print "try again"
    print "finished sql query"
    plate_list_index = []
    no_of_cars = 0
    for ads_record in ads_table:  # we make a lists of database indexes for distinct plate numbers, insert into dictionary
        plate = str(ads_record[1])

        if re.match('^[A-Q][A-Z][A-Z][0-9]{3}', plate):  # check valid plate
            plate_exists_already = False
#            for plate_stored in plate_list:
#                if str(ads_record[1]) == plate_stored.title:
            if plate not in plate_list_index:
                new_plate = RegoPlate(ad_index=ads_record[0], title=ads_record[1], jurisdiction=ads_record[2],
                                      make=ads_record[6],
                                      model=ads_record[7], colour=ads_record[10], phone1=ads_record[11],
                                      car_year=ads_record[8],
                                      month=ads_record[21], ad_date=ads_record[3])
                no_of_cars = no_of_cars +1

                if new_plate.jurisdiction == "NSW":
                    nsw_list = check_plate_nsw2(target_plate=ads_record[1], model=ads_record[7],make=ads_record[6])
                    new_plate.set_year_predict("1999")
                    new_plate.set_nsw_epoch(nsw_list)
                       #print plate_checker_out, nsw_list
                plate_list.append(new_plate)
                plate_list_index.append(plate)
            else:
                for plate_stored in plate_list:
                    if plate_stored.title == plate:
                         plate_stored.grow_ad_list(ads_record[0])
    print "no of cars =" , no_of_cars
    go_again = raw_input("Go Again y/n: ")

  plate_list.sort()
  for x in range(1, 5):
      print "*" * 140
      for plate_stored in sorted(plate_list, key=lambda plate: plate.title):
          nsw_epoch = plate_stored.get_nsw_epoch()
          suburb = plate_stored.set_suburb()
          if x == int(nsw_epoch):  # there are 4 nsw plate lists
              plate_stored.print_plate()




if __name__ == '__main__':
    main()
