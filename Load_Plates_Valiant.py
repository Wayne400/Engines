
import sqlite3


def get_valiant():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
# rego_plate = row[0], ad_date = row[1], model_code = row[2], model_year = row[2],
# model_level = row[4], trim_level = row[5], body_style= row[6], capacity = row[7]
# transmission = row[8], colour = row[9], phone1 = row[10], price = row[11], milage = row[12], month = row[13])
("BKZ238","1978-04-15","none","none","VIP","none","Sedan","none","none","unknown","6372780","$1500","none","none"),
("BMM067","1978-04-15","VG","1970","Valiant","none","Wagon","none","Auto","unknwn","3871585","none","none","none"),
("JPJ398","1978-04-15","none","1976","Ranger","none","Wagon","none","none","unknown","441098","$4980","12000kms","April"),
("EBD444","1978-04-15","none","1970","Pacer","none","Sedan","none","none","unknown","5259027","$1350","none","none"),
("EZU389","1978-04-15","VF","none","Pacer","none","Sedan","none","none","unknown","6076186","$700","none","none"),
("BID922","1978-04-15","VH","1971","Ranger","none","Sedan","none","Auto","unknown","6393541","$2250","none","none"),
("GSL591","1978-04-15","none","1974","Ranger","Sportsman","Sedan","none","none","Metallic Blue","6306327","$2850","none","March"),
("CWG509","1978-04-15","S","1963","Valiant","none","none","Sedan","Auto","unknown","4988866","none","55400mis","none"),
("AJX348","1978-04-15","VE","none","Regal","none","Sedan","V8","none","unknown","5256694","$1600","none","April"),
("EVD283","1978-04-15","VE","1968","Valiant","none","Sedan","none","none","unknown","6448985","$850","none","August"),
("EXD191","1978-04-15","VE","1968","Valiant","none","Sedan","none","none","unknown","3495632","$500","none","none"),
("ARX182","1978-04-15","VF","1969","Valiant","none","Sedan","none","none","unknown","304129","$1325","none","September"),
("BII866","1978-04-15","VG","1971","Valiant","none","Sedan","none","Auto","unknown","9295010","$1950","none","April"),
("BIY170","1978-04-15","none","none","Ranger","XL","Sedan","none","none","unknown","7474601","$1690","none","none"),
("GBI837","1978-04-15","none","1972","Regal","none","Sedan","none","Auto","unknown","7506940","$1950","none","none"),
("BCL881","1978-04-15","none","1970","VIP","none","Sedan","V8","Auto","unknown","364550","$2150","43300mis","none"),
("GOT334","1978-04-15","VJ","none","Regal","none","Sedan","none","Auto","Amber Metallic","8886513","$2900","none","December"),
("GSC114","1978-04-15","VJ","1972","Ranger","none","Wagon","6cyl","Auto","Blue","6256406","$1850","none","August"),
("JFO822","1978-04-15","CL","none","Valiant","Drifter","Van","V8","4spd","Yellow","7452677","none","none","April"),
("JDJ657","1978-04-15","CL","none","Valiant","none","Van","6cyl","none","unknown","591802","$3995","30200kms","March"),

   ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3943
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
