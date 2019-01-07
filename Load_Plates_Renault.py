





import sqlite3

def get_renault_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("GBP627","1975-07-26","R12","1972","GL","Black","Tan","924830","$2499","27000mis","none"),
("DQM539","1975-07-26","R12","1972","TL","Green","Brown","4764936","$1850","33000mis","none"),
("DDQ135","1975-07-26","R16","1972","TS","unknown","none","8714209","$2800","none","none"),
("GJM431","1975-07-26","R12","1973","XX","unknown","none","6341916","$2700","18000mis","June"),
("GFC117","1975-07-26","R12","1973","GL","unknown","none","4394667","none","23000mis","none"),
("AYB900","1975-07-19","R10","1970","XX","unknown","none","865727","none","none","February"),
("GPD736","1975-07-19","R12","1973","GL","Bronze","Corn","9188471","$2250","none","November"),
("ADC237","1975-07-19","R10","1967","XX","unknown","none","472699","$650","none","none"),
("DDQ135","1975-07-19","R16","1972","TS","unknown","none","8714209","$2900","none","none"),
("EIL420","1975-07-12","R16","1972","TL","Green","none","4494794","$2250","33000mis","July"),
("GFD926","1975-07-12","R16","1971","TS","White","none","4871438","$3000","31000mis","January"),
("CUH807","1975-07-12","Gordini","1962","XX","unknown","none","538288","$225","none","none"),
("AEN064","1975-07-12","R10","6970","XX","unknown","none","317131","$775","none","none"),
("AAK082","1975-07-12","R16","1969","XX","unknown","none","946447","$800","none","October"),
("CQW097","1975-07-12","R12","1971","TL","unknown","none","3891493","$1950","none","December"),
("EQL880","1975-07-05","R12","1972","GL","Brilliant Yellow","4523422","none","none","none"),
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
