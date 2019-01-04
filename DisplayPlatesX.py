import sqlite3
from datetime import datetime

def get_sql_data(car_model_list, jurisdiction, order_by):

    connectstring = 'advertisements_mascot.db'
    stop = len(car_model_list)
    car_model_or_string = "( car_model = '{}'".format(car_model_list[0])
    for x in range(1,stop):
        car_model_or_string += " or " + "car_model = '{}'".format(car_model_list[x])
        print car_model_list[x]
    car_model_or_string += " )"
    #     sql = "select * from adverts"
  #  car_model_string = "car_model = '{}'".format(car_model_list[0])
    sql = "select * from adverts where {} and jurisdiction = '{}' ORDER BY {}".format(car_model_or_string, jurisdiction,                                                                            order_by)
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


def print_row(row):
    rego_plate = row[0]
    jurisdiction = row[1]
    iso_advert_date = row[2]
    item_number = row[3]
    publication = row[4]
    car_make = row[5]
    car_model = row[6]
    model_year = row[7]
    capacity = row[8]
    colour = row[9]
    phone1 = row[10]
    phone2 = row[11]
    dealers_licence = row[12]
    who = row[13]
    interior_trim = row[14]
    body_style = row[15]
    trim_level = row[16]
    price = row[17]
   # print rego_plate, model_year, jurisdiction, car_make, car_model, trim_level, body_style, capacity, colour, \
#    interior_trim, phone1, phone2, who, dealers_licence , publication ,iso_advert_date, price
   # print "%6s %7s %3s %-10s %-10s %6s %11s %20s %10s %10s %10s %8s %16s %6s %10s %6s " % (rego_plate, model_year, jurisdiction, car_make, car_model, trim_level, body_style,
   #                                      colour, interior_trim, phone1, phone2, who, dealers_licence, publication, iso_advert_date, price )
    print ('{0:<6} | {1:<4} | {2:3} | {3:^10} | {4:<10} | {5:6} | {6:11} ! {7:20} | {8:10} | {9:10} ! {10:10} | {11:8} ! {12:16} ! {13:3} ! {14:10} ! {15:6s} ' .format(
    rego_plate, model_year, jurisdiction, car_make, car_model, trim_level, body_style,
    colour, interior_trim, phone1, phone2, who, dealers_licence, publication, iso_advert_date, price))

def main():
    car_model_list = ["Hornet", "Matador", "Rebel", "Classic", "Ambassador", "Javelin", "American"]
    ads = get_sql_data(  car_model_list, jurisdiction = "NSW" , order_by = "rego_plate")
#    ads.sort()
    print (
    '{0:<6} | {1:<4} | {2:3} | {3:^10} | {4:<10} |{5:6}| {6:11} ! {7:20} | {8:10} | {9:10} ! {10:10} | {11:8} ! {12:16} ! {13:3} ! {14:10} ! {15:6s} '.format(
        'rego', 'year', 'AUS', 'car_make', 'car_model', 'trim_lvl', 'body_style',
        'colour', 'interior', 'phone1', 'phone2', 'who', 'dealers_licence', 'pub', 'add_date', 'price'))
    print ("-" *200)
    for row in ads:
        print_row(row)



if __name__ == '__main__':
    main()