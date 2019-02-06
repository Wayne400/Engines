





import sqlite3

def get_renault_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("GQX017","1976-01-31","R17","1973","TL","Diamond White","Black","5991122","$4990","18000mis","December"),
("AHH930","1976-01-31","R16","1969","XX","unknown","none","553909","none","$1350","none"),
("EEQ846","1976-01-31","R12","1972","TL","unknown","none","926397","$2200","38000mis","none"),
("EID236","1976-01-31","R10","1970","XX","unknown","none","5249574","$700","none","none"),
("HAV218","1976-01-31","R16","1974","TS","unknown","none","855226","$3495","22000","September"),
("HMD165","1976-01-31","R16","1974","TS","unknown","none","855226","$5195","19000kms","none"),
("GGL436","1976-01-31","R12","1973","GL","Sun Gold","none","855226","$3495","none","none"),
("GJO010","1976-01-31","R12","1973","TL","waggon","none","855226","$3495","26000mis","none"),
("AKO712","1976-01-31","R10","1967","XX","unknown","none","6672906","$400","none","none"),
("CLI331","1976-01-31","R12","1971","TL","White","Pale Green","7976825","$1795","none","none"),
("EWN399","1976-01-31","R10","1969","XX","unknown","none","6451993","$1095","none","none"),
("EIC877","1976-01-31","R12","none","TL","Yellow","Green","6332714","$2295","40000mis","May"),
("AWC209","1976-01-31","R10","none","XX","unknown","none","5466105","$1100","none","December"),
("BBW533","1976-01-31","R16","1971","TS","White","Red","5879678","$2395","46000mis","none"),
("GOP159","1976-01-31","R16","1973","TS","Green","Brown","766988","none","none","November"),
("ERG039","1976-01-31","R10","1968","XX","unknown","none","5285894","$850","none","none"),
("CEI210","1976-01-31","R16","1971","TS","unknown","none","8072473","$3499","none","none"),
("HJZ163","1976-01-31","R16","1972","TS","Sky Blue","Parchment","7985616","$2999","33000mis","none"),
("GFJ243","1976-01-31","R12","1973","XX","unknown","none","6897051","$2900","none","January"),
("GCI165","1976-01-31","R12","1972","GL","unknown","none","426061","$2600","none","none"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1655
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
