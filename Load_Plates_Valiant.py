
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

("DUT832","1977-01-15","none","1966","Valiant","none","Sedan","none","none","unknown","6312424","$845","none","June"),
("ERP462","1977-01-15","none","1966","Valiant","none","Sedan","none","Auto","unknown","6632868","$375","none","March"),
("AQZ328","1977-01-15","none","1971","Pacer","none","Sedan","none","none","unknown","5697514","$1900","none","none"),
("HEY246","1977-01-15","VH","none","Pacer","none","Sedan","none","none","unknown","7474601","$1695","none","February"),
("AUL238","1977-01-15","none","1968","Valiant","none","Wagon","none","none","unknown","3894142","$750","49500mis","none"),
("AUW728","1977-01-15","VF","1969","Safari","none","Wagon","none","Auto","Green with Camel Trim","2112100","$2290","56000mis","October"),
("EVR576","1977-01-15","none","1966","Valiant","none","Wagon","none","none","unknown","5795763","$690","none","July"),
("DCI832","1977-01-15","none","1972","Valiant","none","Utility","none","none","unknown","8273658","$1995","40000mis","October"),
("AGB977","1977-01-15","VE","none","Regal","none","Sedan","none","none","unknown","5607774","$785","68000mis","none"),
("APR600","1977-01-15","VE","none","Regal","none","Sedan","none","Auto","unknown","5873288","$1690","none","none"),
("AYL596","1977-01-15","VE","none","Valiant","none","Sedan","none","Auto","Ivory with Tan Trim","5796333","$1295","none","none"),
("AUC576","1977-01-15","VF","none","Valiant","none","Sedan","none","none","unknown","504857","none","none","none"),
("AIR148","1977-01-15","VG","1971","Pacer","none","Coupe","245","none","unknown","5243194","$1695","none","none"),
("AHY187","1977-01-15","VE","1969","VIP","none","Sedan","V8","Auto","unknown","2112100","none","none","none"),
("AJE546","1977-01-15","none","1969","VIP","none","Sedan","none","none","unknown","6243681","$2200","none","March"),
("GJL945","1977-01-15","VJ","1973","Regal","none","Sedan","265","Auto","unknown","Lane Cove","$3300","none","none"),
("GZF532","1977-01-15","VJ","1974","Ranger","none","Sedan","none","Auto","unknown","5258526","$2995","none","none"),
("HEJ832","1977-01-15","VJ","1975","Ranger","none","Sedan","none","none","unknown","702166","none","none","none"),

   ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3887
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
