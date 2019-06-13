





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("EPH239","1977-04-16","Rebel","1967","none","V8","unknown","none","779355","$1000","none","August"),
("JEA838","1977-04-23","Rambler","1968","none","none","unknown","none","6656408","action","none","April"),
("KEK096","1979-09-01","Matador","none","none","none","unknown","none","046327275","$3150","none","none"),
("GPC136","1979-08-18","Matador","1973","none","none","unknown","none","7979011","auction","none","none"),
("BHF760","1979-08-18","Hornet","1970","none","none","unknown","none","7979011","auction","none","none"),
("GBB623","1979-08-18","Hornet","1971","none","none","unknown","none","6672484","$1995","none","none"),
("KEX564","1979-08-18","Javelin","none","SST","none","unknown","none","6674460","$4250","none","none"),
("KEH816","1979-08-18","Matador","1974","none","none","unknown","none","6674460","$4950","none","none"),
("JRY839","1979-08-18","Matador","1976","none","none","unknown","none","6672484","$4950","none","none"),
("KEX940","1979-08-18","Matador","1974","none","none","Wagon","none","6672484","$4950","none","May"),
("BQO003","1979-08-25","Hornet","1971","none","none","unknown","none","8698557","$2200","74000mis","August"),
("Hornet","1979-08-25","Hornet","1972","none","none","unknown","none","5235942","$3400","48000","none"),
("JQP190","1979-08-25","Hornet","7273","none","none","New Paint","none","733053","none","none","none"),
("HQF400","1979-08-25","Hornet","1975","none","none","unknown","none","6674460","$4250","none","April"),
("MM507","1979-08-25","Javelin","none","none","401","unknown","none","6672484","none","none","none"),
("JRY839","1979-08-25","Matador","1976","none","none","unknown","none","6672484","$5450","none","none"),
("JCQ218","1979-08-25","Matador","1976","none","none","unknown","none","6672484","none","16000kms","none"),
("ETC217","1979-08-25","Rebel","1967","none","none","unknown","none","5256307","$1600","none","none"),
("JIK885","1979-08-25","Rebel","none","none","V8","unknown","none","6375024","$1490","none","December"),
("KIG060","1979-08-25","X-Coupe","1977","none","none","Red","none","6674460","none","none","none"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2909
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
