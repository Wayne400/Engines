
import sqlite3

def get_rover():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("AYV792","1975-08-23","3500","XX","1969","Auto","unknown","none","7985616","$3450","27000mis","none"),
("AXT187","1975-08-23","3500","XX","1969","none","Gun metal Grey","Red","2114677","$3990","27000mis","none"),
("BMH176","1975-08-23","105R","XX","1958","none","unknown","none","4985808","$280","none","February"),
("BGZ457","1975-08-23","90","XX","1957","none","unknown","none","513823","none","none","none"),
("GTX150","1975-08-23","3500","XX","1974","none","unknown","none","7991111","none","9000mis","none"),
("CPO239","1975-08-09","3L","XX","none","none","unknown","none","944591","$1995","51000mis","none"),
("AYV702","1975-08-09","3500","XX","1970","none","unknown","none","7985616","$3450","27000mis","none"),
("CHZ423","1975-08-09","3L","XX","1963","Auto","unknown","none","9132015","$795","none","August"),
("ATY575","1975-08-09","3500","XX","1969","Auto","unknown","none","7986644","none","40000mis","none"),
("BMH176","1975-08-09","105R","XX","1958","none","unknown","none","4985808","$300","none","none"),
("AGI956","1975-07-26","P5B","XX","1971","Auto","unknown","none","7987447","none","59000","none"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1994
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
