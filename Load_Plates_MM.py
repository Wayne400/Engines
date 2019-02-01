





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("HHA699","4","Hornet","1971","4.2","none","yes"),
("HRZ014","12","Matador","none","360","wagon","no"),
("HRP364","8","Hornet","none","3.8","none","no"),
("DIM261","9","Hornet","none","4.2","none","no"),
("BDI258","13","Rebel","1970","360","none","no"),
("BHC255","2","Hornet","none","3.8","none","no"),
("DBQ596","14","Rebel","1971","none","none","no"),
("MM347","3","Hornet","1972","4.2","none","no"),
("AIT947","5","Hornet","1970","3.8","none","no"),
("HPS714","6","Hornet","none","none","none","yes"),
("HJO665","10","Matador","none","360","none","none"),
("GHZ670","11","Matador","none","360","wagon","yes"),
("GAX418","7","Hornet","1972","4.2","none","yes"),
("BQV731","1","Javelin","1971","390","none","no"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1580
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
                        iso_advert_date="1976-05-08",
                        item_number=row[1], publication="smh",
                        car_make="Rambler", car_model=row[2], model_year=row[3],
                        capacity=row[4],
                        colour="unknown", phone1="6672484", phone2="6674460",
                        dealers_licence="MM", who="Jim", interior_trim="none",
                        body_style="none",
                        trim_level="none", price=row[5], milage="none",month="none", air=row[6])
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
