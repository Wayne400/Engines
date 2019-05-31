





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("JMF369","1978-01-07","Matador","none","none","360","wagon","none","7977919","$5499","none","none"),
("JIS975","1978-01-07","Rebel","none","770","V8","White","Black","7993555","$1990","none","none"),
("HRE244","1978-01-14","Hornet","1972","none","4.2","Sunroof","none","991837","$3950","none","none"),
("EAO351","1978-01-14","Rambler","none","none","none","White","none","3873987","none","none","none"),
("AOR650","1978-08-05","Classic","none","660","V8","unknown","none","3375192","$390","none","none"),
("EDY950","1978-08-05","American","1966","none","6cyl","unknown","none","(046)461548","none","none","August"),
("AOR650","1978-07-29","Classic","660","660","V8","unknown","none","3375192","$550","none","none"),
("JGP567","1978-07-29","Classic","770","770","V8","unknown","none","9381836","$750","none","none"),
("BLC906","1978-07-29","Hornet","1970","none","none","unknown","none","7093380","$1700","none","none"),
("GDQ810","1978-07-22","Rebel","none","none","none","unknown","none","7644308","$685","none","December"),
("HPU449","1978-07-22","Ambassador","1963","none","none","unknown","none","4983758","none","none","none"),
("JBP714","1978-07-22","Matador","1973","none","360","unknown","none","5236285","$4000","33000mis","July"),
("RL092","1978-07-22","Hornet","1971","SST","none","Sun Roof","none","6876933","$3000","none","none"),
("EBK821","1978-07-22","Classic","1966","770","287","unknown","none","6211136","$1300","none","July"),
("GLY898","1978-07-22","Matador","1973","none","360","unknown","none","512060","$4400","none","July"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2749
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
