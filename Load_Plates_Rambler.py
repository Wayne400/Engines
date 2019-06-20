





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("ATO313","1974-12-14","Rebel","1968","none","none","unknown","none","7599327","$1400","none","none"),
("EOA215","1974-12-14","Classic","1968","none","none","unknown","none","513518","$690","none","none"),
("Rebel","1974-12-07","Rebel","6970","none","343","White","Beige","598433","$2250","34000mis","none"),
("Rebel","1974-12-07","Rebel","none","none","none","Wagon 9-seat","none","6674460","none","33000mis","none"),
("EOA125","1974-12-07","Rebel","1967","none","none","unknown","none","513518","$845","none","none"),
("Rebel","1974-12-07","Rebel","none","none","none","Red","Bone","741618","$1990","none","none"),
("GOS598","1974-11-30","Rebel","1968","770","V8","Red","Bone","305974","$1550","none","none"),
("BMI839","1974-11-30","Hornet","none","none","none","unknown","none","6695828","$2800","none","August"),
("GHY675","1974-11-30","Classic","none","none","none","unknown","none","none","$995","none","none"),
("CTJ846","1974-11-30","Ambassador","none","none","V8","unknown","none","842371","$390","none","March"),
("ASJ258","1974-11-23","Rebel","1969","none","none","Wagon 9 Seat","none","6375781","$2695","none","none"),
("AJV098","1974-11-23","Rebel","none","none","none","unknown","none","5245274","$1000","none","none"),
("GKZ214","1974-11-23","Rebel","1971","none","360","unknown","none","6212758","$3500","none","none"),
("Rebel","1974-11-23","Rebel","1969","none","none","Turquoise","Parchment","7093235","$2390","none","none"),
("Classic","1974-11-23","Classic","1967","770","V8","unknown","none","3286000","$1450","none","none"),
("DOY285","1974-11-23","Classic","none","660","none","unknown","none","6213170","$150","none","December"),
("ETF578","1974-11-23","Classic","1966","770","none","unknown","none","9139159","$1000","none","none"),
("EGJ156","1974-11-16","Classic","none","none","V8","Wagon","none","9976204","$950","none","none"),
("Rebel","1974-11-16","Rebel","6869","none","V8","Green","Bone","6483681","$1990","none","none"),
("Javelin","1974-11-16","Javelin","none","none","V8","unknown","none","9195450","none","none","none"),
("DPI586","1974-11-16","Rebel","7071","none","360","White","Red","6271528","$3000","none","none"),
("ATO313","1974-11-16","Rebel","1968","none","none","Maroon","none","7599327","$1500","none","none"),
("Rebel","1974-11-16","Rebel","1970","none","none","unknown","none","8488222","$2995","none","none"),
("EDK201","1974-11-09","Classic","1966","none","V8","White Wagon","Blue","6245993","$1150","none","none"),
("DMZ917","1974-11-09","Amercian","1965","330","none","unknown","none","7506962","$550","none","none"),
("Javelin","1974-11-02","Javelin","1973","SST","401","Iridium Bronze 1/2 Vinyl","Bone","6672484","none","none","none"),
("GRR115","1974-11-02","Rebel","1968","none","none","unknown","none","5258526","$1750","none","none"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3027
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
