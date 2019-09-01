
import sqlite3


def get_valiant():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
# rego_plate = row[0], ad_date = row[1], model_code = row[2], model_year = row[2],
# model_level = row[4], trim_level = row[5], body_style= row[6], capacity = row[7]
# transmission = row[8], colour = row[9], phone1 = row[10], price = row[11], milage = row[12], month = row[13])
("EUJ389","1977-01-29","AP5","none","Valiant","none","Sedan","none","Man","unknown","6241047","$690","none","none"),
("RFJ247","1977-01-29","VH","1971","Charger","770","Coupe","6pack","none","Iridescent Bronze","043692189","$2950","none","October"),
("DOQ399","1977-01-29","VH","1972","Charger","770","Coupe","none","Auto","unknown","924545","none","43000mis","none"),
("GPX077","1977-01-29","none","1973","Charger","none","Coupe","none","Auto","unknown","6381823","none","34000kms","none"),
("HSY322","1977-01-29","VJ","1973","Charger","none","Coupe","215","Man","Yellow with Tan Trim","7592583","$2100","none","none"),
("GWX367","1977-01-29","none","1974","Charger","none","Coupe","none","floor","unknown","6381823","38000kms","none","none"),
("EDI774","1977-01-29","none","none","Charger","770","Coupe","none","none","Gold","7591266","$3290","none","April"),
("HWO250","1977-01-29","none","none","Regal","770","Coupe","none","Auto","unknown","5691165","$1850","none","none"),
("DAQ537","1977-01-29","none","1972","Valiant","none","Sedan","none","Auto","unknown","6666650","$2400","none","none"),
("DLK924","1977-01-29","none","1965","Valiant","none","Sedan","none","none","Green","6256816","$650","none","June"),
("AQZ328","1977-01-29","none","1971","Pacer","none","Sedan","none","none","unknown","5697514","$1650","none","none"),
("AXV827","1977-01-29","none","1969","Pacer","none","Sedan","none","none","unknown","6601045","$900","none","January"),
("DEQ641","1977-01-29","VH","1971","Ranger","XL","Sedan","265","Auto","Dark Green with Beige","4492970","$2600","23000mis","December"),
("HHN836","1977-01-29","none","1975","Regal","none","Sedan","none","none","Vinyl Roof","4497641","$4200","none","none"),
("ELX261","1977-01-29","none","1967","none","none","Sedan","none","Auto","unknown","5972873","none","none","none"),
("ENW134","1977-01-29","VC","none","Regal","none","Sedan","none","Auto","unknown","4872044","none","none","none"),
("EVA323","1977-01-29","VC","none","Valiant","none","Sedan","none","Auto","unknown","6238831","$850","none","none"),
("EWI377","1977-01-29","VC","none","Valiant","none","Sedan","none","none","unknown","Arncliffe","$499","none","none"),
("AUY388","1977-01-29","VE","1969","Valiant","none","Sedan","225","Man","unknown","6235337","$1295","none","January"),
("EUE865","1977-01-29","VE","none","Regal","none","Sedan","none","none","unknown","591802","$1000","none","none"),
("EVY894","1977-01-29","VE","1968","Valiant","none","Sedan","none","none","unknown","577744","$1250","none","none"),
("BJN315","1977-01-29","VF","1970","Valiant","none","Sedan","none","Man","unknown","5285300","$1100","none","none"),
("BIK996","1977-01-29","VG","1970","Valiant","none","Coupe","none","Auto","unknown","8887046","$1800","none","September"),
("CQU222","1977-01-29","none","1972","Regal","none","Sedan","none","Auto","unknown","442213","$2750","none","January"),
("EQH363","1977-01-29","VH","1972","Ranger","none","Sedan","none","none","unknown","6373800","$1799","none","none"),
("GDN086","1977-01-29","none","1973","Valiant","none","Sedan","none","none","unknown","6346236","$2495","20000mis","December"),
("GKZ398","1977-01-29","VJ","none","Valiant","none","Coupe","none","Auto","Vinyl Roof","6484000","none","none","none"),
("HAP966","1977-01-29","VJ","none","Valiant","none","Wagon","265","Auto","Mahogany","8887866","$4290","44000kms","October"),
("HKJ303","1977-01-29","VJ","1974","Regal","none","Wagon","V8","none","unknown","4498149","$3600","none","none"),
("HYC389","1977-01-29","VJ","1973","Regal","none","Sedan","none","none","White","485054","$2250","none","none"),
("HZW668","1977-01-29","none","1975","Valiant","none","Sedan","none","Auto","White with Vinyl Top","7985666","$3690","December","none"),
("HKN820","1977-01-29","none","1973","Valiant","none","Wagon","V8","Auto","unknown","6381823","none","none","none"),

   ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3911
    for row in ads:
        print row
        master_index1 += 1


        sql = '''insert into adverts (master_index, rego_plate, jurisdiction, iso_advert_date, item_number, publication,
                 car_make, car_model, model_code, model_year, capacity, colour, phone1, phone2, dealers_licence, who, interior_trim,
                  body_style, transmission, model_level, trim_level, price, milage, month)
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_code}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{transmission}", "{model_level}", "{trim_level}","{price}", "{milage}", "{month}")'''

        sql = sql.format(master_index=master_index1, rego_plate=row[0],
                        jurisdiction="NSW",
                        iso_advert_date=row[1],
                        item_number=1, publication="smh",
                        car_make="Chrysler",model_code= row[2], car_model="Valiant", model_year=row[3],
                        capacity=row[7], body_style=row[6],
                        colour=row[9], phone1=row[10], phone2="none",
                        dealers_licence="none", who="WW", interior_trim="none",
                        model_level=row[4], trim_level=row[5],
                        transmission=row[8], price=row[11], milage=row[12],month=row[13])
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

    ads = get_valiant()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
