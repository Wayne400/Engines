





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("HEJ853","1977-06-11","Matador","1974","none","none","Yellow","410377","$5250","20000"),
("DBQ295","1977-06-11","Matador","1971","none","none","unknown","465450","$3600","December"),
("EIR826","1977-06-11","Hornet","1972","SST","4.2","White","6363905","$3500","73000"),
("GLV854","1977-06-04","Hornet","1973","SST","4.2","unknown","994879","$4350","none"),
("CEI833","1977-06-04","Rebel","1967","SST","V8","unknown","421942","$550","none"),
("BXQ023","1976-06-04","Hornet","1970","SST","none","unknown","854320","$5000","38000"),
("DEI087","1977-05-28","Hornet","1971","SST","4.2","unknown","324487","$3700","none"),
("BJ341","1977-05-28","Hornet","none","SST","4.2","unknown","5286493","$3750","47000"),
("JIL532","1977-05-28","Rebel","1967","none","none","unknown","984180","$1500","none"),
("HUE618","1977-05-28","Rebel","1969","none","none","unknown","5994295","$1750","May"),
("HVI953","1977-05-28","Rebel","1969","none","none","Lemon Green","9973983","$2850","none"),
("HUQ947","1977-05-14","Classic","1965","none","none","Wagon","Cabramatta","$200","none"),
("GWI403","1977-02-05","Rebel","1969","none","none","White","7983501","$1700","none"),
("HUR216","1977-02-05","Hornet","1970","none","none","unknown","6605411","$1350","December"),
("GZE200","1977-02-05","Matador","1972","none","none","White","6399659","$3900","none"),
("HHM576","1977-02-05","Classic","none","none","none","Dark Green","Auburn","$none","May"),
("GOC668","1977-02-05","Matador","1971","none","360","White","5253804","$2950","November"),
("HYH355","1977-02-05","Classic","1965","none","none","unknown","6070868","$450","none"),
("Hornet","1977-01-29","Hornet","1970","none","none","Damaged","881257","$900","none"),
("PA412","1977-01-22","Hornet","1971","none","none","unknown","(043)321950","$2150","none"),
("AMC543","1977-01-22","Rebel","1969","none","none","White","7644308","$1980","none"),
("GWI403","1977-01-22","Rebel","1969","none","none","unknown","8311635","$1900","none"),
("JAE623","1977-01-22","Rebel","1968","none","none","Black","6256241","$1700","December"),
("JAF669","1977-01-22","Matador","1973","none","360","unknown","7597291","none","none"),
("APD641","1977-01-15","Rebel","1968","none","none","Wagon","4562160","$2500","none"),
("Hornet","1977-01-08","Hornet","1971","none","none","Mustard","6481980","$3499","none"),
("APD641","1977-01-08","Rebel","1968","none","none","Wagon","4562160","$2750","none"),
("HZS514","1977-01-01","Rebel","1968","none","none","unknown","Hunters Hill","$650","none"),
("IQQ717","1977-02-09","Gremlin","none","none","4.2","Red","2110367","$5850","none"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1172
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
                        iso_advert_date=row[1],
                        item_number=1, publication="smh",
                        car_make="Rambler", car_model=row[2], model_year=row[3],
                        capacity="none",
                        colour=row[6], phone1=row[7], phone2="none",
                        dealers_licence="none", who="WW", interior_trim="none",
                        body_style="none",
                        trim_level=row[4], price=row[8], milage=row[9],month="none")
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
