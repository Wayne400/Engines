
import sqlite3

def get_rover():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("EIL212","1974-01-12","3500","XX","1972","Auto","unknown","none","7474792","none","none","June"),
("AKQ680","1974-05-11","3500","XX","1970","Auto","unknown","none","903341","$4500","none","none"),
("EFB076","1974-12-21","2000","XX","1967","none","Dark Green","Fawn","9081604","$2200","none","July"),
("AKM903","1974-12-21","90","XX","1957","none","unknown","none","9692842","$225","none","April"),
("CNV462","1974-05-18","100","XX","1962","none","unknown","none","6397480","$900","none","December"),
("DSR864","1974-05-18","90","XX","none","none","unknown","none","4986889","$350","none","March"),
("AQB791","1974-05-18","P5Bcoupe","coupe","1969","Auto","unknown","none","6375781","$1695","none","none"),
("CBY411","1974-05-18","3L","XX","none","Auto","Grey","Red","4763970","$675","none","none"),
("EFV410","1975-12-13","2000","XX","1966","Man","unknown","none","956117","$1750","none","February"),
("AMP822","1975-12-","2000","XX","1969","none","unknown","none","463382","$2695","none","May"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2571
    for row in ads:
        print row
        master_index1 += 1


        sql = '''insert into adverts (master_index, rego_plate, jurisdiction, iso_advert_date, item_number, publication,
                 car_make, car_model, model_year, capacity, colour, phone1, phone2, dealers_licence, who, interior_trim,
                  body_style, transmission, trim_level, price, milage, month)
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{transmission}", "{trim_level}","{price}", "{milage}", "{month}")'''

        sql = sql.format(master_index=master_index1, rego_plate=row[0],
                        jurisdiction="NSW",
                        iso_advert_date=row[1],
                        item_number=1, publication="smh",
                        car_make="Rover", car_model=row[2], model_year=row[4],
                        capacity="none",
                        colour=row[6], phone1=row[8], phone2="none",
                        dealers_licence="none", who="WW", interior_trim=row[7],
                        body_style="none", trim_level=row[3],
                        transmission=row[5], price=row[9], milage=row[10],month=row[11])
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

    ads = get_rover()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
