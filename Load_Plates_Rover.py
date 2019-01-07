





import sqlite3

def get_rover():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("BGU646","1974-05-25","2000","1970","none","unknown","890697","$2950","none"),
("EWK467","1974-05-05","2000","1968","Auto","unknown","838462","$2150","none"),
("EQZ648","1974-06-01","3500","1972","none","unknown","8488221","none","none"),
("Rover","1974-06-08","2000TC","1970","Man","Zircon Blue","418452","none","February"),
("GKZ492","1974-06-29","3500","1973","Auto","Royal Blue","508057","$6000","none"),
("GUT160","1974-07-06","3500","1973","none","Flaming Red","4283501","$6300","none"),
("DIL819","1974-07-06","3L","1968","Auto","unknown","935253","$1650","February"),
("AMV303","1974-08-10","2000TC","1969","none","unknown","5242294","$2990","none"),
("EWB867","1974-08-10","2000","1968","none","unknown","9493777","none","none"),
("AIB453","1974-08-17","2000","1965","none","unknown","8962551","$400","none"),
("AUX073","1974-08-17","2000","1966","none","unknown","413446","$1100","none"),
("EHO741","1974-08-17","2000","1966","none","Powder Blue","3286000","$1600","none"),
("DVJ063","1974-09-07","2000","1966","none","unknown","989865","$1495","none"),
("AEB660","1974-09-21","3L Coupe","1968","none","unknown","4983482","$2650","none"),
("AVM786","1974-10-19","3500","1970","Auto","unknown","6045401","$3550","none"),
("BGU646","1974-11-02","2000TC","1970","none","Sage Green","890697","$2400","July"),
("CHE596","1974-11-09","100","1962","none","Light Grey","9975672","$1200","none"),
("EFB076","1975-01-11","2000","1967","none","Dark Green","9081604","$2200","September"),
("EPX524","1975-01-11","2000","1968","none","unknown","8718187","$1685","none"),
("DAI158","1975-01-11","3500","1971","Auto","unknown","802281","none","none"),
("EFB076","1975-01-25","2000","1967","none","Dark Green","903693","$2000","none"),
("ETX524","1975-01-25","2000","1968","none","unknown","8718187","$1685","none"),
("DUH939","1975-02-08","2000","6566","none","Light Blue","7451255","none","none"),
("AKF123","1975-03-08","2000","1967","none","unknown","7642603","$1600","none"),
("EFB420","1975-03-08","2000","1967","none","unknown","4071358","$1450","August"),
("BEC286","1975-03-29","2000","1968","none","unknown","4395081","$2100","January"),
("DUH939","1975-03-29","2000","1966","Man","Light Blue","7451255","$795","none"),
("DZL457","1975-03-29","3Litre","1966","Auto","unknown","6346316","$1190","January"),
("CJU902","1975-04-22","none","1962","Man","unknown","5208884","$1100","none"),
("DGI978","1975-05-03","3500","1970","Auto","Maroon","9183766","none","none"),
("EUR062","1975-05-10","2000","1968","Man","none","9493050","$1800","none"),
("EXS576","1975-05-24","2000","1968","none","unknown","4494578","none","none"),
("EOQ147","1975-05-24","3500","1970","Auto","BRG","943851","$4650","none"),
("AGI956","1975-05-24","P5Bcoupe","1971","none","Maroon","7987447","none","November"),
("EFB885","1975-05-31","2000","1968","Man","unknown","8721546","$1850","none"),
("AGI956","1975-05-31","P5B","1971","none","Maroon","7987447","none","November"),
("EFB885","1975-06-07","2000","1968","Man","unknown","8721546","$1750","none"),
("AYV702","1975-08-20","3500","1969","Auto","unknown","7985616","$3450","February"),
("CZV688","1975-09-10","2000","1968","Man","Mid Blue","537894","$2250","none"),
("DQX346","1975-09-27","3500","1971","Auto","unknown","5252277","none","none"),
("EDY033","1975-10-25","2000","1967","none","unknown","766141","$1095","July"),
("DAI982","1975-11-24","2000TC","1967","Man","Red","6488033","$2995","June"),
("BME953","1976-02-24","3500","1970","Auto","unknown","5257351","$3950","none"),
("DQY683","1976-03-13","3500","1972","Auto","White","6392062","$4750","none"),
("HQX812","1976-03-13","3500","1975","Auto","Ice Blue","430231","none","August"),
("DVJ164","1976-03-03","P5coupe","1965","Auto","unknown","7985616","$1999","none"),
("ESV064","1977-08-27","2000TC","1967","none","unknown","946691","$2500","none"),
("DWE575","1981-03-07","2000","1966","none","unknown","6329632","$1600","August"),
("EUX303","1981-03-07","2000","1968","none","unknown","9697600","$1650","March"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1275
    for row in ads:
        print row
        master_index1 += 1


        sql = '''insert into adverts (master_index, rego_plate, jurisdiction, iso_advert_date, item_number, publication,
                 car_make, car_model, model_year, capacity, colour, phone1, phone2, dealers_licence, who, interior_trim,
                  body_style, transmission, price, milage, month)
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{transmission}", "{price}", "{milage}", "{month}")'''

        sql = sql.format(master_index=master_index1, rego_plate=row[0],
                        jurisdiction="NSW",
                        iso_advert_date=row[1],
                        item_number=1, publication="smh",
                        car_make="Rover", car_model=row[2], model_year=row[3],
                        capacity="none",
                        colour=row[5], phone1=row[6], phone2="none",
                        dealers_licence="none", who="WW", interior_trim="none",
                        body_style="none",
                        transmission=row[4], price=row[7], milage="none",month=row[8])
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
