





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("LDB284","1979-06-30","Hornet","1972","none","none","Canary Yellow","Black","2124436","$3400","none","March"),
("DNF054","1979-06-30","Hornet","none","none","258","Vinyl Roof","none","9821697","$2500","none","none"),
("Hornet","1979-06-30","Hornet","none","none","none","Sunroof","none","6674121","$3750","none","none"),
("GAU613","1979-06-30","Javelin","none","none","343","unknown","none","843187","$4000","none","May"),
("Matador","1979-06-30","Matador","1972","none","none","unknown","none","6381823","none","none","none"),
("Rebel","1979-06-30","Rebel","1968","none","none","unknown","none","7472966","$1100","none","none"),
("HLY911","1979-07-07","Hornet","1970","none","6cyl","Blue","none","4898834","$1990","none","none"),
("HKG584","1979-07-07","Hornet","1975","none","none","unknown","none","6672484","none","none","September"),
("JZB328","1979-07-07","Matador","1974","none","none","unknown","none","8161133","$2995","none","none"),
("JRY839","1979-07-07","Matador","1976","none","none","unknown","none","6674460","$4650","none","none"),
("ENU318","1979-07-07","Rebel","1967","none","V8","unknown","none","Terry Hills","$900","none","none"),
("BFO509","1979-07-07","Rebel","1970","none","none","Burgundy","none","8714188","$1295","none","July"),
("ESI254","1979-07-07","Rebel","1971","none","none","unknown","none","6373036","$2000","none","April"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2861
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
