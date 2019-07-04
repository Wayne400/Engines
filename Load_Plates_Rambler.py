





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("JYE609","1981-04-04","Hornet","1971","none","none","unknown","none","6488211","auction","none","none"),
("Hornet","1981-04-04","Hornet","1975","none","none","unknown","none","894880","$4500","none","none"),
("Rambler","1981-04-11","Rambler","1967","none","none","Red Convertible","none","069211565","$2750","none","none"),
("KBP897","1981-04-11","Rambler","none","none","360","Convertible","none","6367814","$3000","none","none"),
("JCF700","1981-04-11","Matador","1977","none","none","White","Burgundy","9382255","$3950","none","March"),
("GAU623","1981-04-18","Javelin","none","none","343","Yellow","none","4072711","$2600","none","none"),
("JCF700","1981-04-18","Matador","1977","none","none","White","Burgundy","9382255","$3790","none","March"),
("Rebel","1981-04-18","Rebel","1970","none","none","unknown","none","8885835","$1950","none","none"),
("BDD063","1981-04-18","Rebel","1968","none","none","goes but needs work","none","5196932","$350","none","none"),
("Matador","1981-04-25","Matador","none","none","none","Green wth Vinyl Top","none","5462343","$4750","58716mis","none"),
("HLY911","1981-05-02","Hornet","1970","none","none","unknown","none","4983244","$1250","none","September"),
("CIK304","1981-05-02","Hornet","1971","SST","none","air-con","none","6383484","$2600","none","none"),
("JCF700","1981-05-02","Matador","1977","none","none","White","none","9382255","$3900","none","March"),
("BDV004","1981-05-09","Javelin","none","none","343","Recaro Seats","none","9406648","$4200","none","April"),
("American","1981-05-16","American","none","none","none","unknown","none","6994596","$200","none","none"),
("KWO075","1981-05-16","Matador","1976","none","none","Wagon 8-seat","none","760202","none","63000mis","none"),
("HDL233","1981-05-16","Rebel","1970","none","none","unknown","none","3374731","$1525","none","none"),
("DDB972","1981-05-23","Ambassador","1963","none","287","unknown","none","069592002","none","51000mis","none"),
("JYE609","1981-05-23","Rebel","none","none","none","unknown","none","6398919","$200","none","none"),
("AFR876","1981-05-30","Rambler","1969","none","none","unknown","none","6369858","$200","none","none"),
("GYE012","1981-05-30","Matador","1974","none","none","unknown","none","6422482","$4100","41000mis","none"),
("LGP487","1981-05-30","Matador","1976","none","none","Mustard Wagon 8-seat","Bone","760202","none","63000kms","none"),
("EVA172","1981-05-30","Hornet","none","none","none","White","Tan","5699595","$2400","none","none"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3361
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
