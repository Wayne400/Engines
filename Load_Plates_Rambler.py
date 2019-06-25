





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("DUY155","1980-05-03","Classic","none","660","none","unknown","none","4522833","$500","none","none"),
("GZV666","1980-05-03","Hornet","1974","none","none","unknown","none","Dunedoo 320","$4000","none","none"),
("GEO459","1980-05-03","Matador","1972","none","none","unknown","none","5285279","$1500","none","none"),
("KQO320","1980-05-03","Matador","1976","none","none","Wagon","none","812281","none","none","none"),
("KIY304","1980-05-03","Rebel","1969","none","none","Wagon","none","4873932","$450","none","August"),
("Hornet","1980-05-10","Hornet","1976","none","none","unknown","none","6427579","$2995","55000kms","none"),
("GEO459","1980-05-10","Matador","1972","none","none","unknown","none","5285279","$1500","none","none"),
("VZQ999","1980-05-10","Rebel","1968","none","V8","unknown","none","7991555","$590","none","none"),
("EHO205","1980-05-17","Classic","1966","none","none","unknown","none","302953","$400","none","none"),
("JNO072","1980-05-17","Javelin","none","AMX","none","unknown","none","6375781","none","none","none"),
("YJJ015","1980-05-17","Javelin","none","none","none","unknown","none","6375781","none","none","none"),
("BTQ613","1980-05-17","Classic","1965","none","V8","unknown","none","506780","$750","none","none"),
("KAE076","1980-05-17","Classic","1965","none","none","unknown","none","445708","$575","none","none"),
("DNB980","1980-04-12","Rebel","1976","none","none","Wagon","none","748957","$450","none","none"),
("JNO072","1980-04-19","Javelin","none","AMX","none","unknown","none","6378008","none","none","none"),
("KGX973","1980-04-19","Rambler","1963","none","none","unknown","none","7362429","$380","none","April"),
("KQO320","1980-04-19","Matador","1976","none","none","Wagon","none","812281","$7950","none","none"),
("ASH935","1980-04-19","Rebel","1970","none","V8","unknown","none","4986918","$350","none","none"),
("EPH857","1980-04-19","Rebel","none","none","none","unknown","none","9776938","$1500","52000mis","none"),
("HRP364","1980-04-12","Hornet","1970","none","none","unknown","none","6488211","auction","none","none"),
("KQH256","1980-04-26","Hornet","1974","none","none","Bamboo","none","5229108","$3690","none","none"),
("HNH802","1980-04-26","Hornet","1975","none","4.2","unknown","none","6375024","$4998","none","none"),
("PA412","1980-04-26","Hornet","none","none","none","unknown","none","6672484","$1990","none","none"),
("GAU613","1980-04-26","Javelin","none","none","343","Yellow","none","843187","$3500","none","none"),
("KPR815","1980-04-26","Matador","1976","none","none","Wagon 9-seat","none","6674460","$6600","none","none"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3094
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
