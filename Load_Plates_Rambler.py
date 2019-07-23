





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [

("GLG533","1983-04-02","Hornet","1970","none","none","White","Black","4762640","$1700","none","none"),
("SN986","1983-04-02","Javelin","none","none","nne","unknown","none","303861","$3500","none","none"),
("ABF328","1983-04-02","Rebel","none","none","V8","Yellow","Black","4579462","$1800","none","September"),
("ELG778","1983-04-09","Classic","none","none","V8","One Owner","none","760202","$2990","none","October"),
("ERH233","1983-04-09","Rambler","1967","none","none","unknown","none","5693211","auction","none","none"),
("KDS396","1983-04-09","Javelin","none","none","304","Apple Green","Black","3999206","$6990","none","none"),
("SM986","1983-04-09","Javelin","none","none","nne","unknown","none","303861","$3500","none","none"),
("HRT942","1983-04-16","Rambler","1969","none","none","unknown","none","5792966","auction","none","none"),
("IBL849","1983-04-23","Javelin","none","SST","V8","unknown","none","6619047","$9500","none","none"),
("KDS396","1983-04-23","Javelin","1971","none","304","unknown","none","3999206","$3500","42000mis","none"),
("MGJ923","1983-04-23","Javelin","1969","none","none","Red","Black","5229108","$4995","74000","none"),
("HTU706","1983-04-23","Matador","none","none","none","Wagon","none","6672484","none","none","none"),
("AMX014","1983-04-23","AMX","none","none","none","AMX#7","none","6672484","none","none","none"),
("HLG780","1983-04-30","Hornet","1970","none","none","unknown","none","5244003","$2000","none","none"),
("AZO167","1983-04-30","Rebel","none","none","289","unknown","none","6941940","$700","none","none"),
("DS949","1983-04-30","X-Coupe","none","none","none","unknown","none","9183706","$6000","none","none"),

      ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3569
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
