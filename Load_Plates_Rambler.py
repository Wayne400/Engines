





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("HEM147","1978-03-04","American","1968","none","none","unknown","none","907151","$650","67000mis","none"),
("HWH998","1978-03-04","Rebel","1968","none","290","unknown","none","701124","$975","none","June"),
("DZW856","1978-04-08","Rambler","none","none","none","unknown","none","Auction","$499","none","none"),
("EXX994","1978-04-08","Rambler","none","none","none","unknown","none","Auction","$499","none","none"),
("Hornet","1978-07-01","Hornet","1973","SST","none","White","Brown","811323","$3890","none","none"),
("JDT498","1978-07-08","American","1968","none","6cyl","unknown","none","Kings Cross","$1200","70000mis","none"),
("Hornet","1978-12-02","Hornet","1973","none","none","unknown","none","311945","$2990","none","none"),
("Hornet","1978-12-02","Hornet","1970","none","none","unknown","none","7599151","$1695","none","none"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2789
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
