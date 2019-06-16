





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("EPH239","1977-04-16","Rebel","1967","none","V8","unknown","none","779355","$1000","none","August"),
("JEA838","1977-04-23","Rambler","1968","none","none","unknown","none","6656408","action","none","April"),
("KEK096","1979-09-01","Matador","none","none","none","unknown","none","046327275","$3150","none","none"),
("ETC217","1979-09-01","Rebel","1967","none","none","unknown","none","5256307","none","none","December"),
("EWI365","1979-09-08","American","1966","none","6cyl","unknown","none","6376463","$300","none","September"),
("KGY715","1979-09-08","Hornet","1973","SST","none","unknown","none","6672484","none","none","July"),
("HND414","1979-09-08","Matador","1974","none","Wagon","unknown","none","7273966","$3590","none","June"),
("GHN657","1979-09-08","Matador","none","none","none","unknown","none","5250843","none","none","April"),
("HNP119","1979-09-08","Matador","none","none","none","White","none","992716","$3950","none","none"),
("JRY839","1979-09-08","Matador","1976","none","none","unknown","none","6674460","$5450","none","August"),
("KEX940","1979-09-08","Matador","1974","none","none","Wagon","none","6672484","$4950","none","none"),
("KIG060","1979-09-08","X-Coupe","1977","none","none","unknown","none","6674460","none","none","none"),
("HQT090","1979-09-15","Hornet","1976","none","none","unknown","none","6993002","$3950","48000kms","none"),
("HQT090","1979-09-22","Hornet","1976","none","none","unknown","none","6993002","$3600","30000mis","none"),
("GHZ290","1979-09-22","Matador","1973","none","none","Wagon 9-seat","none","7993969","$7995","none","none"),
("KIW476","1979-09-22","Matador","1976","none","none","Wagon 9-seat Navajoe","none","812281","$6950","none","none"),
("YIL860","1979-09-22","Matador","1973","none","none","Wagon","none","862866","$2850","57000mis","none"),
("GBB623","1979-09-29","Hornet","none","SST","none","unknown","none","6672484","$1495","none","February"),
("HQT090","1979-09-29","Hornet","1975","none","none","unknown","none","6993002","$3500","30000mis","none"),
("Matador","1979-09-29","Matador","1975","none","none","unknown","none","7983080","$4695","none","none"),
("JCQ218","1979-09-29","Matador","1976","none","none","unknown","none","6674460","none","16000kms","March"),
("KGI248","1979-09-29","X-Coupe","1977","none","none","unknown","none","6672484","$7950","none","none"),        ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2929
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
