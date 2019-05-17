





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("JCQ221","1979-03-03","Classic","none","none","none","Wagon","none","Darling Point","$750","none","none"),
("JVC312","1979-03-03","Matador","1972","none","360","Wagon","none","5206287","$3995","none","February"),
("JJQ604","1979-03-03","American","none","none","6cyl","unknown","none","6315291","$1485","none","none"),
("KAH552","1979-03-10","Classic","none","none","V8","unknown","none","7984533","$1495","none","none"),
("EUO794","1979-03-10","none","none","none","none","unknown","none","Wiley Park","$950","none","none"),
("DVI526","1979-03-10","Hornet","1971","none","none","unknown","none","882012","$3600","none","none"),
("HRC754","1979-03-10","Rebel","1970","none","360","unknown","none","7722941","$2400","none","none"),
("DNF054","1979-03-10","Hornet","1971","SST","258","unknown","none","9821697","$2900","none","none"),
("JJQ604","1979-03-17","American","none","none","none","Blue","White","6315291","$1470","none","none"),
("HUK570","1979-03-17","Hornet","1971","none","none","unknown","none","6048694","$1900","none","none"),
("JZB328","1979-03-17","Matador","1974","none","360","unknown","none","8161133","none","none","June"),
("CIK096","1979-03-17","Rebel","1971","none","360","Blue Wagon","none","461431","$2400","none","none"),
("HR161","1979-03-17","Matador-X","1976","none","360","Coupe","none","749944","$9500","none","none"),
("KCE540","1979-03-17","Matador-X","1976","none","360","Savanna Bronze","Black","7476666","$10495","none","March"),
("EMP149","1979-03-17","Rebel","1967","none","none","unknown","none","6358966","$1200","none","none"),
("AUG728","1979-03-24","Classic","none","770","V8","unknown","none","6354259","$1150","none","none"),
("HUD227","1979-03-24","Classic","none","none","V8","unknown","none","9601156","$600","none","none"),
("GTO658","1979-03-24","none","7273","none","none","unknown","none","734189","$2495","none","none"),
("KCE540","1979-03-24","Matador-X","1976","none","360","Savanna Bronze","Black","7476666","$10495","none","March"),
("GQQ252","1979-03-24","Rebel","none","770","V8","unknown","none","952781","$550","none","none"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2619
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
