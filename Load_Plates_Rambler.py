


import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("Javelin","1976-02-14","Javelin","1973","none","none","unknown","none","7977311","$7500","none","none"),
("Javelin","1976-03-13","Javelin","1973","none","none","unknown","none","7977311","$7950","none","none"),
("AQG106","1976-05-29","Javelin","none","SST","304","Lime Green","Black","7476666","none","25000mis","March"),
("Javelin","1976-08-21","Javelin","none","none","301","Zircon Green","Black","7984088","$6490","none","none"),
("Javelin","1976-08-21","Javelin","1971","none","390","unknown","none","7977311","$5500","none","none"),
("Javelin","1976-09-25","Javelin","1968","none","390","4-speed","none","6314539","none","none","none"),
("AQG106","1976-10-09","Javelin","none","SST","304","unknown","none","7472112","none","26000mis","none"),
("Javelin","1976-11-06","Javelin","none","SST","390","Needs minor repair","none","6689038","$2500","none","none"),
("AQG106","1977-03-19","Javelin","1971","SST","304","1/2 Vinyl roof","none","5694963","none","none","none"),
("HQC623","1977-04-16","Javelin","1972","none","none","unknown","none","5296220","none","38000mis","none"),
("Javelin","1977-05-21","Javelin","none","none","343","Bronze Metallic","Black","Flemington","$2850","none","none"),
("Javelin","1977-06-18","Javelin","none","none","343","unknown","none","7599151","$2995","none","none"),
("GTF917","1977-06-18","Javelin","1970","SST","343","unknown","none","3873828","$3750","none","April"),
("GTF917","1977-07-16","Javelin","1970","SST","343","unknown","none","3873828","$3700","none","April"),
("JEW423","1977-08-27","Javelin","none","none","401","Red 4-speed","Black","7977919","$4999","none","none"),
("Javelin","1977-10-29","Javelin","none","none","390","Manual, needs work","none","843187","$1600","none","none"),
("CIA064","1978-01-07","AMX","none","none","none","Red white stripe","none","416908","$2200","none","none"),
("DW195","1978-01-28","AMX","none","none","V8","4-speed","none","8162322","$4250","none","none"),
("MM902","1978-04-15","Javelin","1973","none","none","unknown","none","3719886","$7500","none","none"),
("JRP941","1978-06-03","Javelin","none","none","401","unknown","none","6672484","none","22000mis","none"),
("GPC133","1978-08-12","Javelin","none","none","401","unknown","none","6672484","none","none","none"),

      ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3819
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
