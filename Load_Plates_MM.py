





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("JCJ506","1","Rebel","none","none","Wagon","37000mis","yes"),
("MM347","2","Matador","1974","none","Black/Bone","27000mis","yes"),
("GTL935","3","Hornet","7374","none","unknown","22000mis","no"),
("JDF081","4","Matador","none","none","Carribean","none","yes"),
("ACI771","5","American","none","6cyl","unknown","none","no"),
("XX116","6","Hornet","1975","none","unknown","none","no"),
("HEX812","7","Matador","7475","none","unknown","none","yes"),
("HHA699","8","Hornet","none","none","unknown","none","yes"),
("GQZ536","9","Javelin","none","390","unknown","none","no"),
("HDD558","10","Matador","1973","none","brown/bone","none","yes"),
("EIR754","11","Hornet","none","4.2","unknown","34000mis","no"),
("CKN622","12","Rebel","1970","360","unknown","none","no"),
("JBH340","13","Matador","7475","none","green/green vinyl","none","no"),
("DIA925","14","Hornet","none","4.2","unknown","none","no"),
("CCC095","15","Matador","none","none","Wagon","24000mis","no"),
("GFC061","16","Hornet","7273","none","unknown","none","yes"),
("COP309","17","Matador","none","none","unknown","none","no"),
("CBE988","18","Hornet","none","none","unknown","39000mis","no"),
("CAX724","19","Matador","none","none","unknown","none","yes"),
("BEW925","20","Hornet","none","232","unknown","none","no"),
("JAN981","21","Matador","none","none","unknown","none","yes"),

   ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3911
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
                        iso_advert_date="1977-03-12",
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
