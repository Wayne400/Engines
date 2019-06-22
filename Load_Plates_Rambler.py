





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("JRZ132","1980-01-12","American","none","6cyl","none","unknown","none","5971695","none","37734mis","none"),
("HPR775","1980-01-19","Hornet","1975","none","none","unknown","none","760202","$3995","none","none"),
("HGI230","1980-01-19","Rebel","none","none","none","unknown","none","6521648","$1250","none","none"),
("JK574","1980-01-26","Rambler","1971","none","none","unknown","none","6488211","Auction","none","none"),
("JUT179","1980-01-26","Rebel","none","none","none","Wagon 8-seat","none","5272194","$1999","none","none"),
("GGM425","1980-01-26","Rebel","none","none","none","unknown","none","5871154","$690","none","none"),
("Classic","1980-02-02","Classic","none","none","none","unknown","none","4522833","$700","none","none"),
("JRD950","1980-02-02","Hornet","1973","none","4.2","unknown","none","6375781","$3600","none","none"),
("AYU563","1980-02-02","Rebel","1967","none","none","unknown","none","842832","$900","none","none"),
("ADK690","1980-02-02","American","none","none","none","unknown","none","4579947","$450","none","March"),
("JYK217","1980-02-09","Matador","1977","none","none","Blood Red","White","7993969","$7499","16000kms","none"),
("GCH604","1980-02-09","Rambler","1972","none","none","unknown","none","7979011","Auction","none","none"),
("AYU563","1980-02-09","Rebel","1967","none","none","unknown","none","842832","$750","none","none"),
("GGM425","1980-02-09","Rebel","none","none","none","unknown","none","5871154","$795","none","none"),
("JT506","1980-02-09","Rebel","none","none","none","unknown","none","6398919","$500","none","none"),
("DBE421","1980-02-16","Classic","none","770","none","unknown","none","6650683","$175","93000mis","none"),
("Hornet","1980-02-16","Hornet","1970","none","none","unknown","none","7599159","$895","none","none"),
("KMK673","1980-02-16","Matador","none","none","none","Wagon","none","862866","$2850","none","none"),
("Classic","1980-02-23","Classic","1966","none","V8","unknown","none","5463521","$1290","none","none"),
("JYK217","1980-02-23","Matador","1977","none","none","Red","White","7993969","$5999","none","none"),
("American","1980-03-01","American","1968","none","6cyl","unknown","none","9297630","$760","none","none"),
("HHX049","1980-03-01","American","1964","330","none","unknown","none","507104","$300","none","May"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3054
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
