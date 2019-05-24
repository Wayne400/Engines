





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("JCK541","1","Matador","1976","360","yes"),
("MM347","2","Matador","none","360","yes"),
("JMG401","3","Matador","none","V8","yes"),
("JNC616","4","Matador","1974","360","yes"),
("JKR071","5","Matador","1972","360","yes"),
("GJO325","6","Ambassador","none","360","no"),
("GCL089","7","Rebel","1970","360","no"),
("APW562","8","Rebel","1969","343","yes"),
("EXF326","9","Rebel","1967","none","yes"),
("CQT681","10","Classic","1964","287","no"),
("MM806","11","Hornet","none","none","yes"),
("HKH246","12","Hornet","none","4.2","no"),
("GTK045","13","Hornet","7374","4.2","yes"),
("EBQ220","14","Hornet","1972","4.2","yes"),
("JDD923","15","Hornet","none","4.2","no"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2661
    for row in ads:
        print row
        master_index1 += 1


        sql = '''insert into adverts (master_index, rego_plate, jurisdiction, iso_advert_date, item_number, publication,
                 car_make, car_model, model_year, capacity, colour, phone1, phone2, dealers_licence, who, interior_trim,
                  body_style, trim_level, price, milage, month, air)
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{trim_level}", "{price}", "{milage}", "{month}", "{air}")'''


        sql = sql.format(master_index=master_index1, rego_plate=row[0],
                        jurisdiction="NSW",
                        iso_advert_date="1978-01-28",
                        item_number=row[1], publication="smh",
                        car_make="Rambler", car_model=row[2], model_year=row[3],
                        capacity=row[4],
                        colour="unknown", phone1="6672484", phone2="6674460",
                        dealers_licence="MM", who="Jim", interior_trim="none",
                        body_style="none",
                        trim_level="none", price="none", milage="none",month="none", air=row[5])
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
