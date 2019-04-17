
import sqlite3

def get_valiant():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("EKQ845","1973-12-22","VH","Valiant","XL","none","none","Auto","Green","beige Vinyl roof","(047)391326","$3250","15000mis","July"),
("BEW947","1973-12-22","VG","Valiant","Regal","1970","none","265","Light Blue","none","5220785","$2000","none","none"),
("DLY983","1973-12-22","AP5","Valiant","none","none","225","none","unknown","none","9292434","$325","none","September"),
("DKZ798","1973-12-22","AP6","Valiant","none","none","225","Auto","unknown","none","9292434","$650","none","September"),
("BCJ651","1973-12-22","none","Valiant","Regal","1970","none","Auto","White","Beige","4408857","$1850","26000mis","none"),
("EJH564","1973-12-22","none","Safari","none","1964","none","Auto","unknown","none","5592360","$400","none","April"),
("EUW730","1973-12-22","none","Valiant","none","1968","none","none","unknown","none","393979","$1800","none","none"),
("BCF168","1973-12-22","VG","Safari","Regal","1970","318","none","unknown","none","5992207","$2000","none","none"),
("AWR475","1973-12-22","none","Hardtop","none","1970","none","Auto","Bronze","none","6250616","$1495","none","none"),
("DFG750","1973-12-22","AP5","Safari","Regal","1964","none","Auto","unknown","none","5879618","$700","none","none"),
("EQH361","1973-12-22","VH","Charger","none","1972","245","Auto","Hot Mustard","none","5464301","$2490","none","none"),
("BGJ409","1973-12-22","VG","Safari","Regal","1970","245","Auto","White","Blue","7715093","$2750","none","none"),
("DLE249","1973-12-22","AP5","Valiant","none","none","225","none","unknown","none","7722514","$450","none","August"),
("EKG440","1973-12-22","VE","Valiant","none","1968","none","none","unknown","none","988916","$1250","54000mis","July"),
("GPS202","1973-12-22","VH","Charger","770","none","none","none","Mustard Black V/R","none","5793173","none","10000mis","none"),
("DYK698","1973-12-22","AP6","Valiant","none","none","225","Auto","unknown","none","9292767","none","none","December"),
("AAJ845","1973-12-22","VC","Valiant","Regal","1967","225","none","unknown","none","7591818","nne","none","none"),
   ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2354
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
                        car_make="Chrysler",model_code= row[2], car_model="Valiant", model_year=row[5],
                        capacity=row[6],
                        colour=row[8], phone1=row[10], phone2="none",
                        dealers_licence="none", who="WW", interior_trim=row[9],
                        body_style="none", model_level=row[3], trim_level=row[4],
                        transmission=row[7], price=row[11], milage=row[12],month=row[13])
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
