





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("KAJ647","1979-01-06","American","1968","none","none","unknown","none","7715125","$1400","none","December"),
("EQF757","1979-01-06","Hornet","1972","SST","258","White","Tan","6531352","none","none","none"),
("AUJ141","1979-01-06","Rebel","1967","770","none","unknown","none","5591604","$900","none","November"),
("GGQ252","1979-01-06","Rebel","6869","770","none","unknown","none","Randwick","$1200","none","August"),
("DJF468","1979-01-13","American","1967","none","none","unknown","none","(046)256637","$1200","none","April"),
("EFU848","1979-01-13","Classic","1966","none","none","unknown","none","864972","$1150","none","December"),
("GF092","1979-01-13","Hornet","197071","SST","232","unknown","none","7995770","$3000","none","none"),
("HPH593","1979-01-13","Matador","1973","none","360","unknown","none","Punchbowl","$220","none","none"),
("JZB328","1979-01-13","Matador","1974","none","360","unknown","none","8161133","$4295","none","none"),
("HMI492","1979-01-13","Matador","1975","none","360","unknown","none","6316039","$6250","none","none"),
("JTN439","1979-01-13","Rebel","none","none","290","White","none","903055","$1850","none","July"),
("APC913","1979-01-13","Rebel","none","none","V8","Wagon","none","3494655","$2200","none","July"),
("EIR754","1979-01-20","Hornet","1972","SST","4.2","Sienna Brown","none","3261382","$3200","none","none"),
("JWC312","1979-01-20","Matador","1972","none","360","Cream Wagon","Tan","5206808","$4995","none","none"),
("ADK690","1979-01-27","American","1968","440","232","unknown","none","6920815","$500","none","none"),
("DNF054","1979-01-27","Hornet","1971","none","4.2","unknown","none","9821697","$3175","none","none"),
("EIR754","1979-01-27","Hornet","1972","SST","4.2","Sienna Brown","none","3261382","$3200","none","none"),
("JZM385","1979-05-27","Hornet","1975","none","4.2","unknown","none","6669046","$4500","none","none"),
("HMI492","1979-01-27","Matador","1975","none","360","unknown","none","6316039","$6250","none","none"),
("CIF652","1979-01-27","Rebel","1971","none","290","unknown","none","9828291","$2290","none","none"),
("JZB238","1979-01-27","Matador","1974","none","360","Bamboo","Beige","8161133","$3995","none","none"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2581
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
