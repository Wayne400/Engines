





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
("EQL880","1975-07-05","R12","1972","GL","Brilliant Yellow","none","4523422","none","none","none"),
("GFD926","1975-07-05","R16","1973","TS","White","none","4871438","$3250","none","none"),
("GRN935","1975-07-05","R12","1974","GL","unknown","none","(047)536488","$3100","none","February"),
("AKN921","1975-07-05","R16","6970","TS","unknown","none","9602737","$1650","none","none"),
("GDD225","1975-07-05","R12","1972","GL","Sunburst Yellow","none","417093","$2300","26000","November"),
("AEN064","1975-07-05","R10","6970","XX","unknown","none","317131","$800","none","January"),
("AVQ788","1975-06-28","R10S","6970","XX","unknown","none","432956","$1150","none","May"),
("GTT633","1975-06-28","R12","1974","GL","unknown","none","Punchbowl","$3200","28000mis","December"),
("AKN921","1975-06-28","R16","6970","TS","unknown","none","9602737","$1800","none","none"),
("EXY318","1975-06-28","R10","1968","XX","unknown","none","556933","$950","60000mis","June"),
("BHL847","1975-06-28","R16","1970","XX","unknown","none","5249970","$1550","none","February"),
("GAT283","1975-06-21","R12","1972","GL","unknown","none","5214459","$2000","35000mis","none"),
("EJS518","1975-06-21","R10","1967","XX","unknown","none","5464045","$850","none","February"),
("AMH097","1975-06-21","R16","1970","PS","Barossa Red","Black","(042)847432","none","none","June"),
("BIL037","1975-06-21","R16","1971","TS","unknown","none","6047351","$1730","none","nne"),
("BHL347","1975-06-21","R16","1970","XX","unknown","none","5240672","$1650","none","none"),
("BEJ899","1975-06-21","R10S","1970","XX","Sunburst Gold","Black","Rozelle","$1175","none","none"),
("EJN601","1975-06-14","R10","1967","XX","Green","Black","Rozelle","none","none","March"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 1275
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
