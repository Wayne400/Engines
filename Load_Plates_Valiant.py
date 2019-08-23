
import sqlite3


def get_valiant():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
# model_code = row[2], model_year = row[3], model_level = row[4], trim_level = row[5],
# body_style= row[6], capacity = row[7], transmission = row[8], colour = row[9],
# phone1 = row[10], price = row[11], milage = row[12], month = row[13])
("AJJ379","1976-01-24","none","1968","Safari","none","Wagon","none","none","unknown","6606738","$500","none","September"),
("DBV506","1976-01-24","AP5","none","Regal","none","Sedan","none","Auto","unknown", "432169","$695","none","November"),
("DFD799","1976-01-24","AP5","none","none","none","Sedan","none","Auto","unknown","6601115","$450","none","none"),
("EHX691","1976-01-24","AP6","1966","Regal","none","Sedan","none","none","unknown","7983040","$995","none","November"),
("AVI149","1976-01-24","none","1970","Regal","770","Coupe","V8","Auto","unknown","750598","$1995","none","none"),


   ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3840
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
