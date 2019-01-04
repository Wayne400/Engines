





import sqlite3

def get_peugeot():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("EHT009","1974-06-08","404","1967","unknown","802281","none","March"),
("YAB286","1974-06-08","404","1967","White","733860","$900","March"),
("EWN421","1974-06-08","404","1965","Light Blue","4763970","$1100","none"),
("AGW975","1974-08-03","404","1969","Burgundy","598486","$1950","none"),
("CZV157","1974-08-31","403B","1963","unknown","Randwick","$150","none"),
("ENH748","1974-08-31","404","1967","unknown","9696935","$1050","June"),
("EGD774","1974-09-21","404","1966","Ivory","7985744","$1280","none"),
("EHT506","1974-09-21","404","1967","unknown","5796617","none","December"),
("DSB816","1974-11-23","404","1965","White","5882628","$600","April"),
("DUD742","1974-11-23","404","1965","unknown","711256","$1095","none"),
("EHL374","1974-11-23","404","1966","unknown","9189931","$800","none"),
("EKH308","1974-11-23","404","1966","unknown","7985981","$490","late 66"),
("DQK176","1974-11-23","504","1972","unknown","483727","none","April"),
("AGS470","1975-02-01","404","1969","Maroon","Rockdale","$1550","none"),
("EJC947","1975-02-15","404","1966","unknown","951853","$850","July"),
("CFI667","1975-04-05","404","1970","unknown","4491248","none","none"),
("AWN061","1975-04-12","404","1969","unknown","484764","$1600","December"),
("ANM060","1975-04-19","404","1969","unknown","9189511","$1650","none"),
("EHT506","1975-04-19","404","1967","unknown","705165","$1300","December"),
("GEE512","1975-04-19","504","1972","unknown","956976","$4200","none"),
("CBQ504","1975-04-19","504","1971","unknown","4072862","none","late 71"),
("BOB933","1975-04-26","403","1958","unknown","801793","$525","none"),
("ERH565","1975-04-26","404","1968","unknown","314786","none","none"),
("BEJ721","1975-04-26","504","1970","unknown","7643917","$2950","none"),
("AZV150","1975-05-03","403","1958","unknown","5288770","$150","February"),
("AGH022","1975-05-03","404","1970","Sunburst Brown","(046)256560","$1800","July"),
("EJC867","1975-05-03","404","1967","Ivory","363130","$700","March"),
("AEN668","1975-05-10","404","1969","unknown","(046)254314","$1750","none"),
("APJ989","1975-06-07","404","1969","unknown","7643917","$975","January"),
("BJW338","1975-06-07","404","1968","unknown","5211195","none","none"),
("GEB678","1975-09-06","504","1972","unknown","7361871","none","December"),
("EHT506","1975-09-07","404","1967","unknown","5796617","$1250","none"),
("BQU487","1975-09-27","404","1968","unknown","481617","$1850","September"),
("GRS782","1975-09-27","504","1972","unknown","7361871","none","none"),
("EEQ798","1976-01-24","504","1972","Saltbush Green","none","none", "none"),
    ]

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
                        car_make="Peugeot", car_model=row[2], model_year=row[3],
                        capacity="none",
                        colour=row[4], phone1=row[5], phone2="none",
                        dealers_licence="none", who="WW", interior_trim="none",
                        body_style="none",
                        trim_level="none", price=row[6], milage="none",month=row[7])
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

    ads = get_peugeot()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
