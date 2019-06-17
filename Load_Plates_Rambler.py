





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("KIW480","1979-10-06","Matador","1976","none","none","Wagon 9-seat Navajo","Navajo","812231","$7950","none","none"),
("GZS719","1979-10-13","Hornet","1973","none","6cyl","Vinyl Roof","none","6079607","$2750","none","October"),
("DIW224","1979-10-13","Matador","1972","none","none","unknown","none","740536","$1495","none","none"),
("KIW337","1979-10-13","Matador","1976","none","none","Wagon 9-seat Navajo","Navajo","812281","$7450","none","none"),
("HOC242","1979-10-13","Rebel","1968","none","none","Wagon","none","6311656","$700","none","December"),
("DJY886","1979-10-20","Ambassador","1964","none","none","White","none","273446","none","none","none"),
("Classic","1979-10-20","Classic","1965","none","Wagon","unknown","none","5602976","$595","none","none"),
("Hornet","1979-10-20","Hornet","1972","none","none","Damaged in Mindarie","none","702200","none","none","none"),
("KGA417","1979-10-20","Hornet","1973","none","none","unknown","none","7979011","Auction","none","none"),
("HIW859","1979-10-20","Matador","1974","none","none","Silver","Red","6521455","$3500","none","May"),
("JZB328","1979-10-20","Matador","1974","none","360","unknown","none","8161133","$3495","none","none"),
("KIW337","1979-10-20","Matador","1976","none","none","Wagon 9-seat","none","812281","$7750","none","none"),
("KEW777","1979-10-20","Rebel","1967","none","none","unknown","none","6488211","Auction","none","none"),
("AEN207","1979-10-20","Rebel","1970","none","none","unknown","none","6488211","Auction","none","none"),
("KGI248","1979-10-20","X-Coupe","1977","none","none","unknown","none","6674460","$7950","none","none"),
("AHQ607","1979-10-27","Rambler","1970","none","none","unknown","none","7597482","$2050","none","May"),
("DJY886","1979-10-27","Ambassador","1964","none","none","White","none","273446","none","none","none"),
("KKF060","1979-10-27","Hornet","none","none","none","unknown","none","6672484","none","none","none"),
("GGM849","1979-10-27","Hornet","none","none","none","unknown","none","6672484","none","none","none"),
("AQT834","1979-10-27","Hornet","none","none","none","unknown","none","6672484","none","none","none"),
("CQO273","1979-10-27","Hornet","none","none","none","unknown","none","6672484","none","none","none"),
("HDI448","1979-10-27","Matador","none","none","none","unknown","none","4773355","$3100","none","none"),
("KIW480","1979-10-27","Matador","1976","none","none","Wagon 9-seat Navajo","Navajo","812231","$7950","none","none"),
("JJL260","1979-10-27","X-Coupe","1977","none","none","Bronze","none","6672484","$9950","none","none"),
("KIG060","1979-10-27","X-Coupe","1977","none","none","Red","none","6672484","$8950","none","none"),
("KGI248","1979-10-27","X-Coupe","1977","none","none","Bright Green","none","6672484","$7950","none","none"),
("KKL312","1979-19-27","X-Coupe","1977","none","none","Bronze","none","6672484","$6750","none","none"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2961
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
