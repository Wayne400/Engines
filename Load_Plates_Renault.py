





import sqlite3

def get_renault_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("GXM176","1975-08-23","R12","1974","GL","unknown","none","7980900","$3795","8900mis","July"),
("GLO245","1975-08-23","R12","1973","GL","Yellow","none","418434","$2990","none","none"),
("CQA899","1975-08-23","R12","1971","TL","unknown","none","943311","$2100","29000mis","none"),
("DIW540","1975-08-23","1972","1972","XX","unknown","none","9692086","none","40000mis","March"),
("GBS015","1975-08-23","R16","1972","TS","unknown","none","7597291","none","none","none"),
("ESS561","1975-08-23","1968","1968","XX","White","Black","434411","$1050","none","January"),
("ALF869","1975-08-23","R16","1969","XX","unknown","none","486341","$1100","none","none"),
("HCJ394","1975-08-23","R12","1974","GL","Track Yellow","none","866727","none","none","none"),
("GTD847","1975-08-23","R12","1974","TL","White","none","866727","none","none","April"),
("GEO547","1975-08-23","R12","1972","TL","unknown","none","855226","$2495","none","none"),
("AQR465","1975-08-23","R16","1971","TS","Sunburst","none","855226","$2895","41000mis","none"),
("GVD785","1975-08-23","R16","1974","TS","Sun Gold","none","855226","$4495","26000mis","April"),
("EIX507","1975-08-23","R12","1972","TL","Sun Gold","none","855226","$2895","none","July"),
("GSI716","1975-08-23","R12","1974","TL","Green","Brown","930461","none","29000mis","none"),
("GHC356","1975-08-23","R12","1973","GL","Green","none","9973470","none","28000mis","none"),
("GZN071","1975-08-23","R12","1974","TL","unknown","none","6355593","none","none","none"),
("EHZ726","1975-08-23","R10","1966","XX","White","none","6444381","$450","none","May"),
("HEJ157","1975-08-23","R12","1975","GL","White","none","302441","$3800","none","February"),
("BJJ396","1975-08-23","R10S","1970","XX","unknown","none","7985616","$1499","none","none"),
("GLB000","1975-08-23","R12","none","TL","Ivory","Tan","7985616","$3999","none","none"),
("ERN266","1975-08-23","R10","1967","XX","Black","none","none","$590","none","November"),
("GHN768","1975-08-23","R12","1973","XX","unknown","none","7991111","$2890","none","none"),


    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1322
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
