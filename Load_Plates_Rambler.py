





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("HZG682","1979-06-09","Hornet","1973","none","none","unknown","none","6488211","none","none","none"),
("GAU466","1979-06-09","Hornet","none","none","none","unknown","none","6053611","$2800","none","June"),
("KEX940","1979-06-09","Matador","1974","none","none","Wagon","none","6672484","$4950","47000kms","none"),
("KFA378","1979-06-09","Javelin","1973","none","401","unknown","none","6672484","none","37000mis","May"),
("GAU613","1979-06-09","Javelin","none","none","343","unknown","none","843187","$4950","none","May"),
("RC128","1979-06-09","Hornet","1973","none","4.2","unknown","none","9292847","none","none","none"),
("GAA630","1979-06-09","Matador","1972","none","none","unknown","none","8162370","$1600","none","none"),
("HJQ788","1979-06-09","Hornet","1975","none","4.2","Bamboo","Bone","3573631","$4500","42000kms","none"),
("HEX812","1979-05-26","Matador","1975","none","none","White Brown Vinyl","none","3895222","$5700","57000mis","none"),
("HOG094","1979-05-26","Hornet","1975","none","none","Red","none","365273","$4500","none","none"),
("RT467","1979-05-26","Matador","1976","none","none","unknown","none","4494437","$7450","50000kms","none"),
("DQM014","1979-05-26","Hornet","1972","none","4.2","Orange","none","Flem. Markets","none","none","none"),
("EMG888","1979-05-26","Classic","none","770","none","unknown","none","5235551","$500","none","none"),
("HRJ853","1979-05-19","Matador","1974","none","none","unknown","none","6672484","none","31000mis","none"),
("JZB328","1979-05-19","Matador","1974","none","none","unknown","none","8161133","$3995","none","none"),
("JUT182","1979-05-19","Hornet","1975","none","none","unknown","none","6674460","none","32000kms","none"),
("JAJ781","1979-05-19","Javelin","none","none","343","unknown","none","6375781","$4995","none","none"),
("BW223","1979-05-12","Hornet","1975","none","none","unknown","none","8161182","$5000","none","none"),
("EWI365","1979-05-12","American","1964","none","none","Green","Saddle","6376024","$850","none","September"),
("JBT868","1979-05-12","Matador","1977","none","none","unknown","none","4871435","$5400","4000kms","none"),
("KCD540","1979-05-05","X-Coupe","1976","none","none","Safron Tan","Houndstooth","7476666","none","none","none"),
("KEX564","1979-05-05","AMX","none","none","V8","unknown","none","6674460","none","none","none"),
("BW223","1979-06-02","Hornet","1975","none","none","unknown","none","8161182","$5000","none","none"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2797
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
