





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("HMR725","1981-11-07","Rebel","none","none","none","White","none","6308033","$650","none","none"),
("LJS623","1981-11-14","Ambassador","1970","none","V8","unknown","none","6308033","$895","none","none"),
("JJV106","1981-11-21","Hornet","1971","none","none","unknown","none","7132993","$2500","none","September"),
("KWL659","1981-11-21","Matador","1972","none","none","White","none","7095353","none","none","none"),
("Rebel","1981-11-21","Rebel","1970","none","V8","Wagon","none","5195157","$1280","none","none"),
("JJV106","1981-11-28","Hornet","1971","none","none","unknown","none","7132993","$2500","none","September"),
("GAD870","1981-11-28","Javelin","1969","none","V8","Poor Condition","none","3893074","none","none","none"),
("Matador","1981-11-28","Matador","none","none","none","unknown","none","9491660","$2990","none","none"),
("GCH310","1981-12-05","Classic","none","none","none","Red","none","6442462","$350","none","September"),
("ASB704","1981-12-12","Rambler","1969","none","none","unknown","none","5693211","auction","none","none"),
("AUX370","1981-12-12","Rebel","1970","none","343","unknown","none","Bondi","none","none","none"),
("EXZ261","1981-12-12","Rebel","1967","none","V8","unknown","none","4561506","$850","none","none"),
("HYZ242","1981-12-12","Rebel","none","none","289","Aquatic Green","none","857326","$1675","none","July"),
("LME919","1981-12-12","X-Coupe","1977","none","none","Brown","none","9188144","$8000","none","none"),
("AFB704","1981-12-19","Rambler","1969","none","none","unknown","none","5693211","auction","none","none"),

     ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3424
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
