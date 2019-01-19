





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("Matador","1975-07-19","Matador","1972","none","360","Wagon","none","6375024","$4590","none","none"),
("HHZ354","1975-07-19","Classic","none","none","none","unknown","none","6658838","$900","none","none"),
("Hornet","1975-07-19","Hornet","1975","SST","4.2","Iridescent Green","Bone","9382255","$6530","NEW","none"),
("BKF816","1975-07-19","Rebel","1968","none","none","unknown","none","6377194","$650","none","October"),
("BMF010","1975-07-19","Rebel","1969","none","V8","Sunburst Gold Wagon","none","6237439","$2700","none","none"),
("EDD964","1975-07-19","Hornet","1970","none","232","unknown","none","3718162","$1995","none","none"),
("DBG390","1975-07-19","Classic","1963","660","none","Wagon","none","5452748","$350","none","none"),
("Hornet","1975-07-19","Hornet","none","SST","none","Mustard","Black","4476666","none","none","none"),
("Classic","1975-07-26","Classic","none","660","V8","White","Brown and Grey","7985048","$590","none","February"),
("Hornet","1975-07-26","Hornet","1975","SST","4.2","Iridescent Green","Bone","9382255","$6530","NEW","none"),
("Hornet","1975-08-09","Hornet","1972","none","4.2","unknown","none","4517746","$3850","none","none"),
("HFQ139","1975-08-09","Matador","1972","none","360","Dark Blue","none","7476666","$4990","none","none"),
("BLP040","1975-08-09","Rebel","1970","none","360","Turquoise","none","813000","$2750","none","none"),
("BKF163","1975-08-09","Rebel","1967","770","V8","Bronze","Bone","7273665","$1650","none","none"),
("AXV965","1975-08-09","Rebel","none","none","343","Yellow","Black","5609506","$2000","38000","February"),
("Hornet","1975-08-09","Hornet","1973","none","none","unknown","none","4491248","none","12000","none"),
("Hornet","1975-08-23","Hornet","1975","SST","4.2","Fireball Red","Black","760421","$6393","NEW","none"),
("Hornet","1975-08-23","Hornet","1975","SST","4.2","Metallic Green","Buckskin","760421","$6393","NEW","none"),
("HLG780","1975-08-23","Hornet","1975","SST","4.2","Cream","Clay","6371025","none","none","August"),
("CIR891","1975-08-23","Rebel","1967","770","none","unknown","none","5251634","$750","none","none"),
("AVX965","1975-08-23","Rebel","1970","none","343","Yellow","Black","79855616","$2499","38000","February"),
("AQA558","1975-08-23","Rebel","1975","none","360","Wagon","none","6615229","$2950","none","none"),
("BKF163","1975-08-23","Rebel","1967","770","V8","Bronze","Bone","7273665","$1650","none","none"),
("BKB801","1975-08-23","American","1967","none","none","unknown","none","6672484","none","none","none"),
("CIR891","1975-08-16","Rebel","1967","770","none","unknown","none","5251634","$750","none","none"),
("Hornet","1975-08-16","Hornet","1973","none","none","unknown","none","2212633","none","12400","October"),
("Hornet","1975-08-16","Hornet","1973","SST","none","unknown","none","4491248","none","12000","none"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1360
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
