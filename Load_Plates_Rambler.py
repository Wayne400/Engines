


import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("Hornet","1975-03-15","Hornet","none","SST","none","1 owner","none","7980900","$2995","none","none"),
("Ambassador","1975-05-31","Ambassador","1971","none","none","unknown","none","840257","$3750","none","none"),

("DGQ051","1986-02-07","Hornet","1974","none","none","Sunroof","none","9595086","$3500","none","none"),
("DKY248","1975-11-15","American","none","none","none","unknown","none","5694376","$1500","none","none"),
("EOF548","1975-11-15","American","1967","none","none","unknown","none","047214829","$950","none","July"),
("AUQ084","1975-11-15","Hornet","1971","none","6cyl","unknown","none","7641152","none","none","March"),
("GCR620","1975-11-15","Matador","1972","none","none","Ivory","none","430702","$4690","30000mis","November"),
("CAB223","1975-11-15","Rebel","1970","none","V8","unknown","none","Belmore","$2295","none","none"),
("AIZ538","1975-11-22","Hornet","1971","none","none","unknown","none","6421977","$2700","none","none"),
("GCR620","1975-11-22","Matador","1972","none","none","Ivory","Brown","430702","$4690","30000mis","November"),
("HIX488","1975-11-22","Matador","none","none","360","unknown","none","6672484","$3400","none","none"),
("BIJ396","1975-11-22","Rebel","1969","none","343","unknown","none","Erskinville","$450","none","none"),
("AQA558","1975-11-22","Rebel","1971","none","none","Wagon 8-seat","none","934643","none","none","none"),
("EUX631","1975-11-29","American","none","440","6cyl","unknown","none","6672484","$1400","none","none"),
("BLK280","1975-11-29","Rambler","1967","none","none","unknown","none","512754","$850","none","none"),
("AUQ084","1975-11-29","Hornet","1971","none","none","Yellow","Black","7641152","none","none","none"),
("JC531","1975-11-29","Hornet","none","none","232","unknown","none","6394898","none","none","none"),
("GGQ445","1975-11-29","Javelin","1973","none","none","unknown","none","3374242","$6250","none","none"),
("DGQ054","1975-11-29","Matador","none","none","360","Dec 71","none","4282271","none","none","June"),
("H0X181","1975-11-29","Matador","none","none","360","unknown","none","6672484","$3250","none","none"),
("AQA558","1975-11-29","Rebel","1971","none","none","Wagon 8-seat","none","934643","none","none","none"),
      ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3756
    for column in ads:
        print column
        print column[0], column[11]
        master_index1 += 1


        sql = '''insert into adverts (master_index, rego_plate, jurisdiction, iso_advert_date, item_number, publication,
                 car_make, car_model, model_year, capacity, colour, phone1, phone2, dealers_licence, who, interior_trim,
                  body_style, trim_level, price, milage, month)
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{trim_level}", "{price}", "{milage}", "{month}")'''

        sql = sql.format(master_index=master_index1, rego_plate=column[0],
                        jurisdiction="NSW",
                        iso_advert_date=column[1],
                        item_number=1, publication="smh",
                        car_make="Rambler", car_model=column[2], model_year=column[3],
                        capacity=column[5],
                        colour=column[6], phone1=column[8], phone2="none",
                        dealers_licence="none", who="WW", interior_trim=column[7],
                        body_style="none",
                        trim_level=column[4], price=column[9], milage=column[10], month=column[11])
        print sql
        try:
            cursor.execute(sql)
        except:
            print ("failed to add data")
            pass


def open_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn



def main():

    conn = open_database('advertisements_indexed.db')
    cursor = conn.cursor()

    ads = get_rambler_1()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
