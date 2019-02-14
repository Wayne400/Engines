





import sqlite3

def get_renault_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("GYU548","1975-09-20","R16","1974","TS","unknown","none","7508373","$4180","17000kms","none"),
("DQM910","1975-09-20","R12","1972","XX","unknown","none","9581294","none","24000mis","none"),
("BMG776","1975-08-30","R16","1970","XX","unknown","none","4984704","$1650","none","none"),
("HEJ157","1975-08-30","R12","1975","GL","White","Havana","855226","$4695","none","none"),
("GED765","1975-08-30","R16","1974","TS","Sun Gold","none","855226","$4495","28000kms","none"),
("ECQ654","1975-08-30","R16","1972","TS","unknown","none","855226","$3495","39000mis","June"),
("GHA807","1975-08-30","R16","1972","TL","unknown","none","855226","$2195","none","March"),
("GLO245","1975-08-30","R12","1973","GL","Yellow","Tan","418434","$2990","none","none"),
("ERN266","1975-08-30","R10","1967","XX","Black","none","5971711","$590","none","November"),
("GPD567","1975-08-30","R12","1973","GL","unknown","none","4551256","$2800","17000mis","November"),
("GET653","1975-08-16","R16","1973","TS","Red","Black","2125630","$3250","21000mis","February"),
("BAZ204","1975-08-16","R10","1970","XX","unknown","none","6636328","$850","none","none"),
("GYR709","1975-08-16","R12","1974","TL","unknown","none","6481870","$3690","17000kms","none"),
("DLQ050","1975-08-16","R12","none","TL","Flame Orange","none","6027522","$1850","none","none"),
("GFR528","1975-08-16","R16","1973","TS","unknown","none","766988","$3399","29000mis","none"),
("EIR681","1975-08-16","R12","1972","TL","Blue","none","3286186","$2000","23000mis","August"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1784
    for row in ads:
        print "wally", row
        master_index1 += 1


        sql = '''insert into adverts (master_index, rego_plate, jurisdiction, iso_advert_date, item_number, publication,
                 car_make, car_model, model_year, capacity, colour, phone1, phone2, dealers_licence, who, interior_trim,
                  body_style, trim_level, price, milage, month)
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{trim_level}", "{price}", "{milage}", "{month}")'''

        sql = sql.format(master_index=master_index1, rego_plate=row[0],
                        jurisdiction="NSW",
                        iso_advert_date=row[1],
                        item_number=1, publication="smh",
                        car_make="Renault", car_model=row[2], model_year=row[3],
                        capacity="none",
                        colour=row[5], phone1=row[7], phone2="none",
                        dealers_licence="none", who="WW", interior_trim=row[6],
                        body_style="none",
                        trim_level=row[4], price=row[8], milage=row[9],month=row[10])
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

    ads = get_renault_1()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
