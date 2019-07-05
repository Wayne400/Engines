





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("AG567","1981-09-05","Matador","1972","none","none","White","none","4192814","$2950","52500mis","none"),
("LJJ540","1981-09-05","Matador","1973","none","none","Winter Brown","Parchment","590241","$3990","68000mis","none"),
("LKF926","1981-09-12","Javelin","none","none","401","unknown","none","6674460","none","70000mis","August"),
("JKA974","1981-09-12","Matador","1977","none","none","unknown","none","6246352","$4900","none","September"),
("LJJ540","1981-09-12","Matador","1973","none","none","Winter Brown","Parchment","590241","$3990","68000mis","none"),
("LPG487","1981-09-12","Matador","1977","none","none","Bamboo Wagon 9-seat","none","6674460","none","64000kms","none"),
("LKF826","1981-09-26","Javelin","7273","none","401","unknown","none","6674460","$8950","none","none"),
("LPG487","1981-09-26","Matador","1977","none","none","Bamboo Wagon 9-seat","none","6674460","$5950","none","none"),
("HLX836","1981-09-26","Matador","1972","none","none","Wagon 9-seat","none","6672484","$3850","none","none"),
("BEW000","1981-10-03","Matador","7273","none","none","unknown","none","6217002","$2200","none","none"),
("DQM614","1981-10-10","Hornet","none","none","none","Red","Black","3312895","$2250","none","none"),
("KAW567","1981-10-24","Matador","1972","none","V8","Green Vinyl Top","none","7992155","$1150","none","none"),
("DTH121","1981-10-31","Classic","1964","660","none","unknown","none","3999497","$350","none","none"),
("LHN939","1981-10-31","Rebel","none","none","none","unknown","none","6465537","$1500","none","none"),

     ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3410
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
