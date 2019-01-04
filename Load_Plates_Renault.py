





import sqlite3

def get_renault_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("GKG959","1976-09-25","R12","1973","GL","Yellow","5252078","$2800","July"),
("GMT485","1976-09-25","R12","1973","GL","unknown","415237","$2850","August"),
("GXX824","1977-01-29","R12","1974","GL","White","935661","$3200","July"),
("ENQ597","1977-06-18","R12","1972","TL","unknown","3262579","$2250","May"),
("DYM198","1977-07-02","R10","1967","XX","unknown","334461","$550","none"),
("GTD596","1977-07-02","R16","1973","TS","Alpine White","4193640","$3100","April"),
("EYO182","1977-07-02","R10","1969","XX","unknown","5022856","$600","October"),
("EUW768","1977-07-02","R10","1968","XX","unknown","6396318","$1190","March"),
("BQP115","1977-07-02","R16","1971","TS","unknown","7596181","$1475","July"),
("EIR464","1977-07-02","R16","7273","TS","unknown","9223064","$2200","July"),
("BQV507","1977-07-09","R16","1971","TS","unknown","921560","$1800","July"),
("ESI175","1977-07-09","R16","1972","TL","unknown","6222442","$2100","April"),
("GJC462","1977-08-13","R17","1973","TL","unknown","3584644","$4999","May"),
("GQH385","1977-08-20","R12","1973","GL","unknown","4493019","$2690","December"),
("AOD505","1977-08-20","R16","1969","TS","unknown","9098583","$999","July"),
("BQV507","1977-08-20","R16","1971","TS","unknown","921560","$1800","August"),
("GBL016","1977-08-20","R16","1972","TL","unknown","6920448","$2450","September"),
("GTD583","1977-08-20","R16","1974","TS","unknown","4495946","$3550","April"),
("EKE271","1977-08-27","R10","1967","XX","Dark Green","430769","$1100","March"),
("AKI115","1977-08-27","R12","1971","XX","unknown","9601790","$1600","none"),
("EQL533","1977-08-27","R12","1972","GL","unknown","841405","$2680","July"),
("EAQ471","1977-08-27","R16","1972","TS","unknown","5794827","$2400","May"),
("GRL030","1977-09-03","R17","1973","TL","White","4872819","$4200","December"),
("DCQ574","1977-09-10","R12","1972","TL","unknown","517402","$2200","February"),
("CRI310","1977-09-10","R16","1971","TS","unknown","5691918","$2400","September"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1201
    for row in ads:
        print row
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
                        colour=row[5], phone1=row[6], phone2="none",
                        dealers_licence="none", who="WW", interior_trim="none",
                        body_style="none",
                        trim_level=row[4], price=row[7], milage="none",month=row[8])
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
