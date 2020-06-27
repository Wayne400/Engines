





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("HQB163","1","Hornet","1975","none","unknown","none","no"),
("HGY203","2","Hornet","none","4.2","unknown","none","yes"),
("DIM261","3","Hornet","none","none","unknown","none","no"),
("HVF097","4","Matador","none","none","Wagon","none","no"),
("GOF194","5","Matador","none","none","unknown","19000mis","no"),
("HXV754","6","Matador","1974","none","unknown","none","yes"),
("GDR412","7","Matador","none","none","unknown","none","yes"),
("GBF500","8","Matador","none","360","unknown","none","no"),
("GLH524","9","Matador","none","none","unknown","none","yes"),
("GAX724","10","Matador","none","none","unknown","none","yes"),
("HDS432","11","Javelin","none","none","imported","none","no"),
("MM806","12","Javelin","1971","390","unknown","none","no"),
("BJR857","13","Rebel","1970","360","unknown","none","no"),
("DA1153","14","Rebel","1969","343","unknown","none","no"),
("AGG853","15","Rebel","1968","290","unknown","none","no"),
("GEZ762","16","Rebel","none","none","Wagon","none","no"),
("HXU178","17","Classic","none","none","Wagon","none","no"),
("EFU83","18","Classic","1966","770","unknown","none","no"),

   ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3951
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
                        iso_advert_date="1976-10-16",
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
