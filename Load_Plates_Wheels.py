





import sqlite3

def get_wheels_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("BFY905","NSW","1970-11-01","AMSA""Chrysler","Valiant","1970"),
("RNW122","SA","1970-11-01","AMSA","Holden","Torana","1970"),
("KRA604","VIC","1970-11-01","AMSA","Ford","Falcon","1970"),
("BFY021","NSW","1970-11-01","Wheels","Chrysler","Valiant","1970"),
("AGI181","NSW","1971-02-01","Wheels","Honda","unknown","1970"),
("BME516","NSW","1971-02-01","Wheels","Austin","Kimberly","1970"),
("BME519","NSW","1971-02-01","Wheels","Austin","Tasman","1970"),
("GNL796","1974-09-07","R16","1973","TS","Cherry Red","4985640","$3200","October"),
("BAQ248","1974-09-07","RXX","1971","TL","unknown","5240666","$1890","none"),
("AAD465","1975-02-08","R10","1967","XX","unknown","596100","$700","October"),
("AUH823","1975-02-08","R10","1967","XX","White","6235354","$600","none"),
("AAJ873","1975-02-08","R10","1968","XX","Dark Blue","6671598","$850","August"),
("DIO155","1975-02-08","R16","1969","XX","unknown","6366086","$795","September"),
("ESF802","1975-02-22","R10","1969","XX","unknown","9601655","$650","none"),
("BJL503","1975-05-17","R10","1970","XX","unknown","6372979","$1000","none"),
("ESK523","1975-05-17","R10","1967","XX","White","3373307","$1150","December"),
("BLA043","1975-05-17","R12","1971","TL","unknown","5879037","$1500","none"),
("CGQ148","1975-05-17","R16","1969","TS","unknown","8074305","$1700","January"),
("EQF084","1975-05-17","R16","1972","TS","unknown","6241694","$2300","none"),
("EPX382","1975-05-24","R10","1967","XX","unknown","8073957","$650","September"),
("ARK106","1975-05-24","R10","1970","XX","Yellow","6022790","$600","none"),
("CIK812","1975-05-24","R12","1971","TL","unknown","none","$1550","October"),
("GAT283","1975-05-24","R12","1972","GL","unknown","5214459","$2200","none"),
("GXF052","1975-05-24","R12","1973","TL","unknown","825542","$2200","none"),
("GCS558","1975-05-24","R12","1972","XX","unknown","414334","none","November"),
("GFI889","1975-05-24","R16","1973","TL","unknown","3893390","$2300","January"),
("CGW148","1975-05-24","R16","1969","TS","unknown","8074395","$1600","none"),
("GDC953","1975-05-24","R16","1972","TS","Teal Blue","466338","$2590","September"),
("AZC899","1975-05-31","R10","1970","XX","unknown","3491608","$1100","March"),
("CYP844","1975-05-31","R12","1972","TL","unknown","3714388","$2100","none")]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 0
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

    ads = get_wheels_1()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
