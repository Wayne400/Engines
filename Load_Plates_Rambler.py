





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("Classic","1980-09-13","Classic","1962","none","6cyl","side valve","none","6672484","$200","none","none"),
("EWK029","1980-09-13","Rambler","1963","none","none","unknown","none","6488211","auction","none","none"),
("JLT847","1980-09-13","Hornet","1974","none","none","unknown","none","4513307","$2500","55000mis","July"),
("Matador","1980-09-13","Matador","1970","none","360","unknown","none","5162279","$1490","none","none"),
("JNO072","1980-09-20","Javelin","none","AMX","none","Extensive front damage","none","6376781","$1500","none","April"),
("Matador","1980-09-20","Matador","1970","none","360","unknown","none","5162279","$1490","none","none"),
("JPB162","1980-09-27","Classic","none","660","none","unknown","none","5879997","$1250","none","August"),
("JLM339","1980-09-27","Hornet","1976","none","none","unknown","none","5295346","$3700","none","none"),
("KSK805","1980-10-04","Hornet","none","none","6-cyl","unknown","none","6672484","$1495","none","August"),
("KWE403","1980-10-04","Javelin","none","none","390","Red","Black","6672484","none","none","none"),
("GEU732","1980-10-04","Matador","1971","none","none","unknown","none","5162279","$1000","none","October"),
("GUY763","1980-10-04","Matador","1971","none","none","unknown","none","5162279","$1200","none","October"),
("JRZ132","1980-10-11","American","none","none","none","unknown","none","5971695","$1990","38000mis","none"),
("JTO658","1980-10-11","Matador","1972","none","none","unknown","none","4563749","$2000","none","none"),
("JKH208","1980-10-11","Rebel","1969","none","V8","unknown","none","539384","$700","none","January"),
("JPB162","1980-10-18","Classic","none","660","none","unknown","none","5879997","$1250","none","none"),
("KWE403","1980-10-18","Javelin","none","none","390","Red","Black","6672484","$5900","55000mis","none"),
("KYH099","1980-10-18","Javelin","none","none","343","White","Black","812281","$5950","52000mis","none"),
("JCF700","1980-10-18","Matador","1977","none","none","White","Burgundy","9382255","$4700","none","none"),
("JTO658","1980-10-18","Matador","1972","none","none","unknown","none","4563749","$1850","none","none"),
("AGI601","1980-10-25","Ambassador","none","none","360","unknown","none","5871154","$1495","none","March"),
("KVA717","1980-10-25","Javelin","1970","none","none","unknown","none","812281","$6995","none","none"),
("KWE403","1980-10-25","Javelin","none","none","390","Orange","Black","6672484","$5900","55000","none"),
("HCH037","1980-10-25","Matador","none","none","none","Blue","Bone","590501","$3495","none","none"),
("JCF700","1980-10-25","Matador","1977","none","none","White","Burgundy","9382255","$4990","none","none"),
("JTO658","1980-10-25","Matador","1972","none","none","unknown","none","4563749","$1700","none","none"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3224
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
