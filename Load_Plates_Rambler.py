





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("BK169","1979-08-04","American","none","none","none","unknown","none","(042)673738","$350","none","none"),
("JOQ365","1979-08-04","Hornet","1975","none","none","Green","Beige","5693211","auction","none","none"),
("KHT585","1979-08-04","Hornet","1976","none","6cyl","Wagon","none","6674460","none","none","none"),
("GBB623","1979-08-04","Hornet","1971","none","none","unknown","none","6672484","$1995","none","February"),
("GAX610","1979-08-04","Matador","none","none","none","unknown","none","6674460","$2990","none","August"),
("JIK885","1979-08-04","Rebel","none","none","none","White","Blue","6375024","$1498","none","December"),
("EKQ741","1979-08-04","Rebel","1971","none","360","Wagon","none","7980000","$3995","none","none"),
("EMP966","1979-08-11","American","none","none","none","unknown","none","6672484","none","31000mis","none"),
("EZZ020","1979-08-11","Classic","1966","none","none","unknown","none","042297849","none","none","November"),
("BHF760","1979-08-11","Hornet","1970","none","none","unknown","none","7979011","auction","none","none"),
("HOF400","1979-08-11","Hornet","1976","none","none","unknown","none","6674460","$4250","none","none"),
("KHT585","1979-08-11","Hornet","1976","none","6cyl","Wagon","none","6674460","none","none","none"),
("JJI754","1979-08-11","Rambler","none","none","none","unknown","none","6029464","$500","none","none"),
("GPC617","1979-08-11","Matador","1973","none","none","Silver","Beige","7476666","$4990","none","none"),
("BKO647","1979-08-11","Rebel","1971","none","360","Wagon","none","7980000","$3995","none","none"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2894
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
