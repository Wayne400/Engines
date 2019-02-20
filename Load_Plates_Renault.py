





import sqlite3

def get_renault_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("GBS732","1974-07-06","R16","1972","TS","unknown","none","904965","$3500","none","September"),
("CLI329","1974-07-06","R16","1971","TS","unknown","none","6212572","$2300","none","none"),
("ANM507","1974-07-06","R16","1969","TL","unknown","none","946626","$1650","none","July"),
("AXZ594","1974-07-06","R16","1970","XX","unknown","none","895708","$1525","none","none"),
("ENA013","1974-07-06","R10","1967","XX","unknown","none","6381797","$680","none","none"),
("ATX973","1974-07-06","R10","1970","XX","White","none","6634876","$890","none","none"),
("GWX703","1974-07-06","R12","1973","TL","Yellow","none","551326","$2000","none","July"),
("GGT789","1973-12-01","R12","1973","GL","unknown","none","945320","$2490","5000mis","none"),
("GBG654","1973-12-01","R12","1972","TL","unknown","none","9491660","nne","12000mis","none"),
("ELY517","1973-12-01","R10","1969","XX","Blue","none","5254545","$900","45000mis","June"),
("AVQ862","1973-07-28","R16","1971","TS","White","Black","447709","$2100","none","January"),
("EOL286","1973-07-28","R8","none","XX","Green","none","947686","$485","none","March"),
("AGG276","1973-07-28","R10","1970","XX","unknown","none","7277444","$850","none","none"),
("BJU406","1973-07-28","R16","1970","XX","unknown","none","565251","$1600","none","none"),
("BGJ917","1973-07-28","R16","1970","XX","unknown","none","4871983","$1600","29000mis","July"),
("ELI090","1973-07-28","R16","1972","TL","unknown","none","9092679","$2000","none","none"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1870
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
