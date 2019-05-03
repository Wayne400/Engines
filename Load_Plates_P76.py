
import sqlite3

def get_P76():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("HDV572","1977-04-23","P76","none","1974","V8","Auto","unknown","none","9813370","$2900","none","December"),
("HBS469","1977-04-23","P76","Executive","none","V8","none","Orange Vinyl Roof","Beige","$7891177","$3695","29000kms","none"),
("GNH301","1977-03-26","P76","none","none","V8","Auto","unknown","none","7093949","$2580","31000ms","August"),
("GNS086","1977-03-26","P76","Executive","1973","V8","Auto","unknown","none","7500161","$2500","none","April"),
("HAN286","1976-01-24","P76","Super","none","V8","Auto","unknown","none","5249877","$3000","9500mis","October"),
("GNH425","1976-01-24","P76","Deluxe","1973","6cyl","Auto","unknown","none","310444","$3295","26000mis","none"),
("HLK965","1976-06-05","P76","Deluxe","1974","none","Auto","unknown","none","9186653","$2000","none","none"),
("GPS961","1976-06-05","P76","Deluxe","1973","V8","Auto","White","none","Oatley","$2250","none","none"),
("HBO910","1976-06-05","P76","Deluxe","1974","V8","4spd","White","Tan","8488222","$2995","none","November"),
("GZE543","1976-06-05","P76","Targa Florio","1974","none","none","Targa Blue","Parchment","7891177","none","30000kms","February"),
("GOP078","1976-06-05","P76","Super","none","V8","none","Targa Blue","Parchment","7891177","$2695","none","none"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2488
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
