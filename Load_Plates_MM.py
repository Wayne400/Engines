





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("HWM080","1","Matador","1976","360"),
("HEX812","2","Matador","1975","360"),
("JBH340","3","Matador","7475","360"),
("MM 347","4","Matador","1974","360"),
("JEM145","5","Matador","1974","360"),
("JEM113","6","Matador","1973","360"),
("JDX686","7","Matador","none","360"),
("HCN396","8","Matador","none","360"),
("CCQ756","9","Matador","7273","360"),
("GDH357","10","Matador","none","360"),
("JEM144","11","Hornet","1973","4,2"),
("GFC061","12","Hornet","7273","4.2"),
("HHA699","13","Hornet","none","4.2"),
("EKI718","14","Hornet","none","4.2"),
("BBC276","15","AMX","1969","343")
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 0
    for row in ads:
        print row
        master_index1 += 1


        sql = '''insert into adverts (master_index, rego_plate, jurisdiction, iso_advert_date, item_number, publication,
                 car_make, car_model, model_year, capacity, colour, phone1, phone2, dealers_licence, who, interior_trim,
                  body_style, trim_level, price, milage, month)
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{trim_level}", "{price}", "{milage}", "{month}")'''


        sql = sql.format(master_index=master_index1, rego_plate=row[0],
                        jurisdiction="NSW",
                        iso_advert_date="1977-05-21",
                        item_number=row[1], publication="smh",
                        car_make="Rambler", car_model=row[2], model_year=row[3],
                        capacity=row[4],
                        colour="unknown", phone1="6672484", phone2="6674460",
                        dealers_licence="MM", who="Jim", interior_trim="none",
                        body_style="none",
                        trim_level="none", price="none", milage="none",month="none")
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
