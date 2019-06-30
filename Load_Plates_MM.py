





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("JLM338","1","Hornet","1975","none","unknown","none","yes"),
("JBV975","2","Hornet","1973","none","unknown","4.2","no"),
("GBE988","3","Hornet","1972","none","unknown","none","no"),
("JSD965","4","Hornet","none","none","unknown","6-cyl","yes"),
("GCU971","5","Hornet","1972","none","Vinyl Roof","none","no"),
("JRP821","6","Hornet","none","none","unknown","none","yes"),
("DQK578","7","Hornet","none","3.8","unknown","none","no"),
("HRE299","8","Matador","1976","none","unknown","none","yes"),
("JQL053","9","Matador","1976","none","unknown","none","yes"),
("JRX589","10","Matador","1976","360","unknown","none","yes"),
("MM347","11","Matador","7475","none","unknown","16000kms","yes"),
("MM806","12","Matador","1974","none","unknown","29000mis","yes"),
("JOQ808","13","Matador","1974","360","unknown","none","yes"),
("JSD766","14","Matador","1973","none","unknown","none","yes"),
("JKG609","15","Matador","7273","none","unknown","none","yes"),
("JRA775","16","Matador","none","none","unknown","none","none"),
("JRP946","17","Matador","none","none","Wagon 9-seat","none","yes"),
("GLL270","18","Rebel","1971","360","unknown","none","yes"),
("HNZ431","19","Rebel","1969","343","unknown","none","no"),
("AWE977","20","Rebel","none","290","unknown","none","no"),

   ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3264
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
                        iso_advert_date="1978-05-13",
                        item_number=row[1], publication="smh",
                        car_make="Rambler", car_model=row[2], model_year=row[3],
                        capacity=row[4],
                        colour=row[5], phone1="6672484", phone2="6674460",
                        dealers_licence="LD1091", who="Jim", interior_trim="none",
                        body_style="none",
                        trim_level="none", price="none", milage=row[6],month="none", air=row[7])
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
