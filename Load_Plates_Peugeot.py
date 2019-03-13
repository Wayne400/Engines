





import sqlite3

def get_peugeot():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("ASJ813","1974-07-20","404","6667","unknown","3996387","$880","none","none"),
("AHM502","1975-11-22","404","1969","unknown","7980900","$1995","none","June"),
("HEU678","1975-11-22","504","1974","unknown","7981111","$6490","16000kms","none"),
("HFU537","1975-11-22","504","1975","unknown","7991111","none","14000kms","none"),
("EWZ404","1975-11-08","404","1968","White-Black","8713910","$1400","none","none"),
("HFV537","1975-11-01","504","1975","Liquid Amber","8488976","$6700","none","March"),
("DCD183","1975-11-01","404","1968","unknown","323820","$825","none","none"),
("BYI946","1975-11-01","504","1971","Light Green","6603959","none","none","June"),
("AGW391","1975-10-18","404","1969","White-Brown Upholstery","4112460","$1400","none","none"),
("DIV193","1976-02-21","504","1971","Sage","279065","$3750","none","November"),
("CQH132","1976-02-21","504","1971","unknown","7361871","none","none","November"),
("GTD792","1976-02-21","504","none","unknown","7472112","none","23000kms","none"),
("EDO274","1975-10-11","404","1966","White","6390930","$1500","none","July"),
("HKY066","1975-10-11","504","1975","Trak Yellow","5796333","$8250","4000kms","September"),
("AFF060","1975-10-11","404","1968","White","735193","none","none","none"),
("HGM837","1975-10-11","504","1974","White","2114677","$6750","25000kms","none"),
("EIA250","1975-10-11","504","1970","Maroon","6371025","none","none","none"),
("GUM222","1975-10-11","504","1974","unknown","8717670","$6100","none","April"),
("AMH502","1975-10-11","404","1969","unknown","7980900","$2195","none","none"),
("GHD443","1975-10-11","504","1973","unknown","7991111","none","21000mis","none"),
("EBD641","1975-09-20","404","1967","unknown","4073138","$700","none","March"),
("GEB678","1975-09-20","504","1972","unknown","7361871","none","24900mis","December"),
("HFA066","1975-09-20","504","1975","White","7361871","none","6000kms","February"),
("DOQ251","1976-08-21","504","1972","unknown","893688","$4750","48000mis","none"),
("BQD493","1976-08-21","504","1972","unknown","8161133","$4995","none","none"),
("HMX432","1976-08-21","504","1975","Trak Yellow","765666","none","1924kms","none"),
("HHP627","1978-02-25","504","1976","White","6308222","$7598","39000kms","February"),
("HDJ468","1978-02-25","504","1974","White","6308222","$7298","36000kms","December"),
("JFG832","1978-02-25","504","1974","Dry Leaf","6308222","$6090","none","none"),
("JAG823","1978-02-25","504","1974","White","6308222","$5798","none","none"),
("GGX803","1978-02-25","504","1973","White","6308222","$5490","none","April"),
("ECP533","1976-05-15","404","1966","unknown","6989195","$875","none","none"),
("HNC178","1976-02-07","504","1975","Silver","7361871","none","12000kms","none"),
("HNC327","1976-02-07","504","1973","unknown","7361871","none","26000mis","none"),
("HIJ547","1976-02-07","504","1975","unknown","7361871","none","17000mis","none"),
("HAN347","1976-02-07","504","1974","unknown","7361871","none","12500kms","March"),
("GNA716","1976-02-07","504","1973","unknown","7591672","$4750","none","October"),
("EEQ798","1976-02-07","504","1972","Saltbush Green","Alec Mildren","none","31249mis","none"),
("EDF602","1976-02-07","404","1966","Green","7976011","$995","none","August"),
("EKA602","1976-01-17","404","1967","Wagon","6541517","$1100","none","none"),
("GCC453","1976-01-17","504","1972","White","6483277","none","33000mis","October"),
("EDF602","1976-01-17","404","1966","Green","7976011","$1195","none","August"),
("GIP223","1976-01-17","504","1973","Bronze","7976011","$5595","none","none"),
("EEQ798","1976-01-17","504","1972","Saltbush Green","Alec Mildren","none","31249mis","none"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2005
    for row in ads:
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
                        trim_level="none", price=row[6], milage=row[7],month=row[8])
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
