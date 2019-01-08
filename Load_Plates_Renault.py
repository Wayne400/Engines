





import sqlite3

def get_renault_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("GBF655","1975-08-09","R16","1972","TS","Alpine White","none","362527","$2800","29000mis","none"),
("GJM482","1975-08-09","R16","1973","TS","White","none","6691103","$2800","36000mis","none"),
("GEY185","1975-08-09","R12","1973","GL","Burnt Bronze","none","434701","none","25000mis","none"),
("GOS892","1975-08-09","R12","1973","TL","unknown","none","Woollahra","$2650","23000mis","November"),
("EXN055","1975-08-09","R10","1968","XX","unknown","none","6672484","$980","none","none"),
("ABQ109","1975-08-09","R16","1970","TS","Sunburst","none","444329","none","none","December"),
("ALX089","1975-08-09","R10","1970","XX","Yellow","Black","9698504","$1200","none","July"),
("HDD589","1975-08-09","R12","1974","GL","unknown","none","312040","$3500","9000kms","December"),
("AUN368","1975-08-09","R16","6970","TS","White","Red","7451255","$1590","none","none"),
("DJQ742","1975-08-09","R16","1971","TS","unknown","none","486867","$1600","none","January"),
("GSJ580","1975-08-09","R12","1973","GL","unknown","none","6491113","none","38000mis","none"),
("GFR528","1975-08-09","R16","1973","TS","Polar White","Green","766988","none","29000mis","none"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1310
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
