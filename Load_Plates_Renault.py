





import sqlite3

def get_renault_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("GDM215","1974-07-13","R12","1972","XX","White","Tan","805009","$2650","22000mis","November"),
("GBG849","1974-07-13","R16","1971","TS","unknown","none","316488","$1850","41000mis","none"),
("EPU675","1974-07-13","R10","1968","XX","unknown","none","6329835","$500","none","none"),
("EQL648","1974-07-13","R16","1971","TS","Blue","Black","422183","$2650","none","July"),
("ETH848","1974-07-20","R10","1969","XX","Blue","Black","5229831","$975","none","July"),
("CTR212","1974-07-20","R4","1963","XX","unknown","none","9299735","$150","none","none"),
("EQL648","1974-07-20","R16","1971","TS","Blue","Black","422183","$2495","none","July"),
("ELD845","1974-07-20","R10","1967","XX","unknown","none","9602472","$750","none","June"),
("EUP366","1974-07-20","R10","1969","XX","Blue","none","3372219","$1075","none","none"),
("DVI943","1974-07-20","R16","1971","TL","Brown","none","8691124","$2000","31000mis","December"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1927
    for row in ads:
        print "wally", row
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
                        iso_advert_date=row[1],
                        item_number=1, publication="smh",
                        car_make="Renault", car_model=row[2], model_year=row[3],
                        capacity="none",
                        colour=row[5], phone1=row[7], phone2="none",
                        dealers_licence="none", who="WW", interior_trim=row[6],
                        body_style="none",
                        trim_level=row[4], price=row[8], milage=row[9],month=row[10])
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

    ads = get_renault_1()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
