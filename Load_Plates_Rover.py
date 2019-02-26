
import sqlite3

def get_rover():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("GUT160","1974-07-13","3500","XX","none","none","Red","Tan","4283501","$6300","none","November"),
("AAB294","1975-11-22","2000","XX","none","Auto","unknown","none","7991111","$1990","none","none"),
("EZR580","1975-11-22","2000","XX","1968","Auto","unknown","none","4981414","none","none","September"),
("BGE260","1975-11-22","2000","XX","1970","Auto","unknown","none","313244","none","29000mis","none"),
("BME983","1975-11-22","3500","XX","1970","Auto","British Racing Green","none","5257351","$4890","none","October"),
("EWS600","1975-11-22","2000","TC","1969","none","unknown","none","4493776","$2500","none","none"),
("DLA423","1975-11-15","2000","XX","1967","Man","White","Cinnamon","430231","none","34000mis","none"),
("AJD933","1975-11-15","3L","XX","1961","White","unknown","none","8692036","$600","none","June"),
("EIC144","1975-11-08","3500","XX","1970","Auto","White","Red","(047)213179","none","none","none"),
("EDY033","1975-11-01","2000","TC","1967","none","unknown","none","766141","$1095","none","July"),
("EEU478","1975-11-01","2000","XX","1966","Man","unknown","none","7641152","none","none","August"),
("AFN287","1975-01-11","3500","XX","1971","Auto","unknown","none","802281","none","none","none"),
("EFB076","1975-01-25","2000","XX","1967","none","Dark Green","none","903693","$2000","none","none"),
("ETX524","1975-01-25","2000","XX","1968","none","unknown","none","8718187","$1685","none","none"),
("DUH939","1975-02-08","2000","XX","6566","none","Light Blue","none","7451255","none","none","none"),
("AKF123","1975-03-08","2000","XX","1967","none","unknown","none","7642603","$1600","none","none"),
("EFB420","1975-03-08","2000","XX","1967","none","unknown","none","4071358","$1450","none","August"),
("BEC286","1975-03-29","2000","XX","1968","none","unknown","none","4395081","$2100","none","January"),
("DUH939","1975-03-29","2000","XX","1966","Man","Light Blue","none","7451255","$795","none","none"),
("DZL457","1975-03-29","3Litre","XX","1966","Auto","unknown","none","6346316","$1190","none","January"),
("CJU902","1975-04-22","none","XX","1962","Man","unknown","none","5208884","$1100","none","none"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1275
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
                        car_make="Rover", car_model=row[3], model_year=row[4],
                        capacity="none",
                        colour=row[6], phone1=row[8], phone2="none",
                        dealers_licence="none", who="WW", interior_trim=row[7],
                        body_style="none", trim_level=row[2],
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
