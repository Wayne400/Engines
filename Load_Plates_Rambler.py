





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("Hornet","1971-02-06","Hornet","1970","none","none","Safety Wattle, new 12/70","Black","700187","none","none","none"),
("American","1971-02-06","American","1967","none","232","Turquoise","Bone","700271","$1990","none","none"),
("American","1971-02-06","American","1968","440","none","White","Black","700271","$1990","none","none"),
("Rebel","1971-02-06","Rebel","1969","none","290","Sky Blue","Black","7899000","none","none","none"),


("MQE683","1984-01-14","Matador","1974","none","none","Wagon","none","9382022","$4990","none","none"),
("HEX756","1984-01-14","Rambler","1970","none","none","unknown","none","6488211","auction","none","none"),
("HQY411","1984-01-21","Classic","1965","none","none","unknown","none","765469","$500","none","March"),
("HCT420","1984-01-21","Hornet","1972","none","none","unknown","none","5972966","auction","none","none"),
("MQE683","1984-01-21","Matador","1974","none","none","Wagon","none","9382022","$4990","none","none"),
("HEX756","1984-01-21","Rambler","1970","none","none","unknown","none","6488211","auction","none","none"),
("MQE683","1984-02-04","Matador","1974","none","none","Wagon","none","9382022","$4990","none","none"),
("MQE683","1984-02-11","Matador","1974","none","none","Wagon","none","9382022","$4990","none","none"),
("ABM952","1984-02-11","Rebel","1969","none","343","unknown","none","4271259","$1200","none","none"),
("MQE683","1984-02-18","Matador","1974","none","none","Wagon","none","9382022","$3990","none","none"),
("HAN159","1984-02-25","Rambler","1972","none","none","unknown","none","5693211","auction","none","none"),
("KMH887","1984-03-03","American","1967","none","none","unknown","none","985905","$1990","none","January"),
("MQC076","1984-03-03","Classic","none","770","none","Damaged","none","4193171","none","none","none"),
("JIK852","1984-03-03","Matador","1972","none","none","Vinyl Top","none","6674460","none","none","none"),
("KMH887","1984-03-10","American","none","none","none","unknown","none","985905","$1990","none","January"),
("KMH887","1984-03-17","American","none","none","none","unknown","none","985905","$1990","none","January"),
("HST022","1984-03-17","Matador","1976","none","360","2 Tone Wagon","none","7980000","$7995","none","none"),
("KMH887","1984-03-24","American","none","none","none","unknown","none","985905","$1990","none","January"),
("GIL814","1984-03-24","Hornet","none","none","none","unknown","none","6484000","$1490","none","none"),
("HST022","1984-03-24","Matador","1976","none","360","2 Tone Wagon","none","7980000","none","none","none"),
("GIL814","1984-03-31","Hornet","none","none","none","unknown","none","6484000","$1490","none","none"),

      ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3651
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
