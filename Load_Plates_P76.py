
import sqlite3

def get_P76():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("GZG491","1977-11-05","P76","none","1974","V8","Auto","White","none","6496253","$3000","none","none"),
("HBC749","1977-11-05","P76","Targa Florio","1974","none","none","Metallic Blue","Parchment","4495497","$5500","31000kms","November"),
("HDH200","1978-08-26","P76","none","none","V8","Auto","unknown","none","986394","$2500","none","none"),
("GSQ340","1978-08-26","P76","Deluxe","none","V8","Auto","unknown","none","4514795","$2250","none","none"),
("GKI419","1978-08-19","P76","Executive","1973","V8","Auto","unknown","none","9293220","$1500","none","none"),
("GKV810","1978-08-19","P76","none","1973","6cyl","Auto","unknown","none","8697366","$1950","none","July"),
("GNO832","1975-08-09","P76","Super","1973","6cyl","Auto","Green","Tan","6029911","$2690","none","none"),
("GQS358","1975-08-09","P76","none","1973","V8","Man","unknown","none","6615432","$2150","11000kms","December"),
("GNT190","1975-08-02","P76","none","1973","none","none","unknown","none","573408","$2250","300mis","none"),


    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2526
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
