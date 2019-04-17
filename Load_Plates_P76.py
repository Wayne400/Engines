
import sqlite3

def get_P76():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("GKV932","1974-04-20","P76","Super Six","none","6cyl","Auto","unknown","none","464319","$3500","5000mis","none"),
("GKI291","1974-04-20","P76","Executive","1973","none","none","unknown","none","5244563","$3950","none","July"),
("GKP599","1974-04-20","P76","Deluxe","1974","V8","3spd","Orange","Saddle","6356395","$2895","4000mis","July"),
("GNC803","1975-11-22","P76","Super","1973","V8","Man","unknown","none","480213","none","14000ms","none"),
("GPU651","1975-11-08","P76","none","none","V8","Man","unknown","none","4515523","$1800","none","November"),
("GLM234","1975-11-08","P76","none","none","V8","4spd","Green","Tan","5796721","$2995","25000ms","none"),
("HMK922","1975-11-08","P76","Executive","none","none","none","White","Black","3893233","$3595","none","none"),
("GML946","1975-11-01","P76","Super De Luxe","1973","V8","Auto","Corinthian Blue","Bone","6375024","$3698","none","August"),
("GRY577","1975-11-01","P76","Super","none","V8","Auto","OK Fudge","Brown","3494411","none","15640mis","none"),
("GL0819","1976-02-21","P76","Super","1973","none","Auto","unknown","none","430231","none","none","none"),
("GWS604","1976-02-21","P76","De Luxe","1974","6cyl","Auto","Pittar Apricot","Parchment","7891177","none","25000kms","none"),
("GYE935","1976-02-21","P76","Executive","1974","none","none","Nutmeg","none","7891177","none","11000kms","none"),
("GMU305","1976-02-21","P76","none","1973","none","none","unknown","none","9381955","none","14000mis","none"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2371
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
