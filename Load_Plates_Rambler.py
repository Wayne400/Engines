





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("KVA717","1980-11-01","Javelin","1970","none","none","unknown","none","812281","$5995","none","none"),
("KDE610","1980-11-01","Rebel","none","none","360","unknown","none","6254926","$1200","none","February"),

("KLG780","1980-11-08","Hornet","none","none","none","unknown","none","6288193","$1100","none","none"),
("KVA717","1980-11-08","Javelin","1970","none","none","unknown","none","812281","$5995","none","none"),
("Javelin","1980-11-08","Javelin","none","none","none","wanted","none","7453881","$wanted","none","none"),
("HGX646","1980-11-08","Matador","1972","none","360","unknown","none","6313130","$2225","none","November"),
("JCF700","1980-11-08","Matador","1977","none","none","White","Burgundy","9382255","$4700","none","none"),
("KIW480","1980-11-08","Matador","1976","none","none","Wagon","none","6381823","none","none","none"),
("HRT051","1980-11-08","Matador","1970","none","none","Wagom 8-seat","none","5875971","$500","none","March"),
("Classic","1980-11-15","Classic","none","none","none","unknown","none","734251","$650","none","none"),
("KIW480","1980-11-15","Matador","1976","none","none","Wagon 9-seat","none","6381823","none","none","none"),
("KAE076","1980-11-15","Classic","1966","none","none","unknown","none","446942","$395","none","September"),
("KYH099","1980-11-22","Javelin","1970","none","none","ex-KVA717","none","812281","$4995","none","none"),
("JCF700","1980-11-22","Matador","1977","none","none","White","Burgundy","9382255","$4950","none","none"),
("KIW480","1980-11-22","Matador","1976","none","none","Wagon 9-seat","none","6381823","$4995","none","none"),
("KVW245","1980-11-22","X-Coupe","none","none","none","Bronze","Black","6672484","none","60000kms","none"),
("WJ302","1980-11-29","Hornet","1975","none","none","Bamboo","Buckskin","5204502","$3600","none","none"),
("KYH099","1980-11-29","Javelin","1970","none","none","ex-KVA717","none","812281","$5795","none","none"),
("GZZ399","1980-11-29","Matador","1974","none","none","Cream","Saddle","5229108","$2990","58000mis","August"),
("JCF700","1980-11-29","Matador","1977","none","none","White","Burgundy","9382255","$4900","none","none"),
("AQU789","1980-12-06","Hornet","1971","none","6cyl","some body damage","none","5197471","none","none","none"),
("EXQ275","1980-12-06","Javelin","none","none","none","unknown","none","6051397","$400","none","November"),
("GAU613","1980-12-06","Javelin","none","none","343","unknown","none","4072711","$3000","none","June"),
("KWE403","1980-12-06","Javelin","none","none","390","unknown","none","6674460","none","55000mis","none"),
("GNS256","1980-12-06","Matador","1972","none","none","unknown","none","5344508","$2500","none","none"),
("JCF700","1980-12-06","Matador","1977","none","none","White","Burgundy","9382255","$4900","none","none"),
("KUY245","1980-12-06","X-Coupe","none","none","none","unknown","none","6672484","none","none","none"),
("APU968","1980-12-13","Rebel","1968","none","none","unknown","none","538579","$995","none","September"),
("CQD263","1980-12-20","Hornet","1971","none","none","unknown","none","6381823","$895","none","none"),
("KYH099","1980-12-20","Javelin","none","none","343","White ex-KVA717","Blue","812281","$4495","none","none"),
("KWE403","1980-12-20","Javelin","none","none","390","unknown","none","6672484","none","none","none"),
("HUW275","1980-12-20","Javelin","none","none","390","unknown","none","6672484","none","none","none"),
("JCF700","1980-12-20","Matador","1977","none","none","White","Burgundy","9382255","$3900","none","none"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3284
    for column in ads:
        print column
        print column[0], column[11]
        master_index1 += 1


        sql = '''insert into adverts (master_index, rego_plate, jurisdiction, iso_advert_date, item_number, publication,
                 car_make, car_model, model_year, capacity, colour, phone1, phone2, dealers_licence, who, interior_trim,
                  body_style, trim_level, price, milage, month)
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{trim_level}", "{price}", "{milage}", "{month}")'''

        sql = sql.format(master_index=master_index1, rego_plate=column[0],
                        jurisdiction="NSW",
                        iso_advert_date=column[1],
                        item_number=1, publication="smh",
                        car_make="Rambler", car_model=column[2], model_year=column[3],
                        capacity=column[5],
                        colour=column[6], phone1=column[8], phone2="none",
                        dealers_licence="none", who="WW", interior_trim=column[7],
                        body_style="none",
                        trim_level=column[4], price=column[9], milage=column[10], month=column[11])
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

    ads = get_rambler_1()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
