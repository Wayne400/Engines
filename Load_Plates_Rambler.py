





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("DWI365","1979-06-02","American","1964","none","none","Green","Tan","6375024","$995","none","September"),
("EFU848","1979-06-02","Classic","1966","770","V8","White","Bone","6372625","$1050","none","December"),
("Classic","1979-06-02","Classic","1967","770","none","unknown","none","812281","$1025","none","none"),
("HOW667","1979-06-02","Classic","none","none","none","unknown","none","6657239","$1100","none","December"),
("GB135","1979-06-02","Hornet","1973","none","4.2","Blue","Bone","5271113","$3500","none","none"),
("RC128","1979-06-02","Hornet","1973","none","4.2","Brown","Beige","9292847","none","42000mis","none"),
("HJQ788","1979-06-02","Hornet","1975","none","4.2","Bamboo","White","3573631","$4500","42000mis","none"),
("KAJ781","1979-06-02","Javelin","none","none","343","unknown","none","6375781","$4500","none","none"),
("HND414","1979-06-02","Matador","1974","none","360","Wagom","none","7273966","none","none","none"),
("JZB328","1979-06-02","Matador","1974","none","none","unknown","none","8161133","$3995","none","none"),
("RT467","1979-06-02","Matador","1976","none","none","unknown","none","4494437","$5950","none","none"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2839
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
