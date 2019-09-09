
import sqlite3


def get_valiant():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
# rego_plate = row[0], ad_date = row[1], model_code = row[2], model_year = row[2],
# model_level = row[4], trim_level = row[5], body_style= row[6], capacity = row[7]
# transmission = row[8], colour = row[9], phone1 = row[10], price = row[11], milage = row[12], month = row[13])
("EIX994","1980-02-02","VH","none","Charger","none","Coupe","none","none","unknown","6359920","$`800","none","August"),
("GKG019","1980-02-01","none","1974","Charger","none","Coupe","245","Auto","unknown","7244122","$1600","none","none"),
("GTR575","1980-02-02","none","1974","Charger","none","Coupe","none","4spd","White","5272194","$1690","none","none"),
("ASF510","1980-02-02","VF","1969","Valiant","none","Coupe","160HP","Auto","unknown","5161410","$650","none","none"),
("GBK817","1980-02-02","none","none","Charger","RT","Coupe","E49","4spd","unknown","6319785","$2200","none","December"),
("DXM592","1980-02-02","none","1967","Regal","none","Sedan","none","Auto","unknown","935029","$375","none","none"),
("EUO669","1980-02-02","none","1969","Regal","none","Sedan","none","Auto","unknown","3576627","$150","none","none"),
("EXX508","1980-02-02","none","1968","Regal","none","Sedan","none","Auto","unknown","7892084","$1100","none","none"),
("EEH994","1980-02-02","VC","1967","Valiant","none","Sedan","none","Man","unknown","418434","$1195","48560mis","none"),
("ENU513","1980-02-02","VC","1967","Valiant","none","Sedan","none","Auto","unknown","418434","$1195","80000mis","none"),
("EOZ328","1980-02-02","VC","1967","Valiant","none","Sedan","none","none","unknown","7804559","$450","none","none"),
("BOB002","1980-02-02","VE","none","VIP","none","Sedan","V8","none","unknown","5463495","$750","none","none"),
("EQG287","1980-02-02","none","1972","Valiant","none","Wagon","6cyl","Auto","unknown","4492392","$750","100000mis","none"),
("GGZ408","1980-04-19","none","1972","Charger","RT","Coupe","none","none","unknown","8722947","$1850","none","October"),
("CIS793","1980-05-17","VH","1971","Charger","XL","Coupe","none","Man","unknown","7509079","$1395","none","September"),
("KQX941","1980-05-17","none","none","Charger","none","Coupe","E48","4spd","unknown","741705","$3300","none","none"),

   ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3986
    for row in ads:
        print (row)
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
        print (sql)
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
