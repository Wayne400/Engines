
import sqlite3

def get_P76():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("GIL175","1976-05-29","P76","none","1974","V8","Auto","unknown","none","6272859","$3200","40000kms","none"),
("HPG420","1976-05-29","P76","none","1973","none","Auto","unknown","none","6370407","$2795","none","none"),
("HTE118","1976-05-29","P76","none","1974","6cyl","Auto","Crystal White","none","7891177","$2095","none","none"),
("HAV426","1976-05-29","P76","Executive","1974","V8","Auto","Apricot","Beige","445003","$3500","22500km","none"),
("GVF494","1976-05-29","P76","none","1974","6cyl","Auto","Orange","Brown","6366642","$2450","12000mis","April"),
("HTE189","1976-05-22","P76","Executive","none","V8","Auto","Teal Blue","Tan","5796721","$3695","45000kms","none"),
("GOO108","1976-05-22","P76","Super","none","V8","Auto","Cream","Tan","5879678","$2995","17200mis","none"),
("HSI728","1976-05-08","P76","Deluxe","1974","6cyl","Auto","unknown","none","8717400","$2750","none","April"),
("GLO243","1976-05-01","P76","none","1973","none","Auto","Blue","Parchment","766988","none","none","none"),
("GOF373","1976-05-01","P76","Executive","1973","none","none","unknown","none","616231","$3100","29000mis","October"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2499
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
                        car_make="Leyland", car_model=row[2], model_year=row[4],
                        capacity=row[5],
                        colour=row[7], phone1=row[9], phone2="none",
                        dealers_licence="none", who="WW", interior_trim=row[8],
                        body_style="none", trim_level=row[3],
                        transmission=row[6], price=row[10], milage=row[11],month=row[12])
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

    ads = get_P76()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
