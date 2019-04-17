





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("TG212","1974-12-21","Rebel","1970","none","343","unknown","none","6305538","$2750","43000mis","none"),
("RR398","1974-12-21","Rebel","1971","none","360","Mocha","none","6375484","$3290","none","none"),
("GKW760","1974-05-18","Matador","1971","none","360","Willow Green","none","6420238","$none","none","none"),
("DDI945","1974-05-18","Hornet","1972","none","258","unknown","none","6358731","$3400","24000mis","none"),
("GJO325","1974-05-18","Ambassador","1970","none","360","unknown","none","775627","$4000","none","May"),
("GLI939","1974-05-18","Rambler","1970","none","none","White","Black","552346","$3000","none","December"),
("EOE427","1974-05-18","Classic","1966","none","none","unknown","none","6246490","$900","none","none"),
("AQQ052","1974-05-18","Rambler","1967","none","V8","unknown","none","8882498","none","none","none"),
("BDF278","1974-05-18","Rambler","1962","none","none","unknown","none","Darlinghurst","$150","none","none"),
("BKQ184","1974-05-18","Hornet","none","SST","none","White","Brown","838986","none","20000mis","none"),
("GBP513","1974-05-18","Hornet","1971","SST","4.2","White","Black","6250646","none","23000","September"),
("BKQ184","1974-04-20","Hornet","none","SST","none","White","Brown","838986","none","20000mis","none"),
("EQE524","1974-04-20","Classic","1966","770","V8","unknown","none","6442717","$800","none","October"),
("EBT652","1974-04-20","Classic","1966","none","V8","unknown","none","324055","$1150","none","April"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2323
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
