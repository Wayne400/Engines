





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("CIA064","1973-08-11","AMX","1969","none","none","unknown","none","4515700","$4175","none","none"),
("GNL704","1975-10-18","AMX","1969","none","343","Red","none","703589","$4490","none","none"),
("AXD241","1976-12-11","AMX","1970","none","none","unknown","none","5466775","$7500","30000mis","none"),
("GLY898","1978-07-15","Matador","1973","SST","none","unknown","none","512060","$4400","none","July"),
("DAX625","1978-07-15","Classc","none","660","none","unknown","none","7711314","$450","none","August"),
("JN230","1978-07-08","Hornet","1972","none","4.2","White","Red","6511375","$3500","none","none"),
("JTN426","1978-07-01","Rebel","none","770","V8","unknown","none","5335362","$1400","none","July"),
("JIL602","1978-07-01","Hornet","1973","SST","4.2","unknown","none","6371025","$4999","29600mis","none"),
("EZF475","1978-06-03","American","1966","440","none","White","none","862870","$850","none","October"),
("BQT177","1978-06-17","Rebel","1971","SST","360","unknown","none","4514098","$2400","75000mis","none"),
("BIO998","1978-06-17","Hornet","none","none","none","unknown","none","5423113","none","none","June"),
("DQD576","1978-06-10","Rebel","1971","none","360","unknown","none","4498166","$2950","none","none"),
("BLC906","1978-05-27","Hornet","1970","SST","232","unknown","none","7093380","$1900","none","none"),
("JBP714","1978-05-27","Matador","1973","none","none","Royal Blue","Bone","5236285","$5000","32000mis","none"),
("GPX321","1978-05-27","Hornet","1973","SST","4.2","Silver Grey","none","4986256","$3950","42000kms","November"),
("GOH959","1978-05-27","Hornet","1973","none","4.2","White","Brown","4192623","$3850","none","October"),
("JN230","1978-05-20","Hornet","1972","none","4.2","White","Red","6511375","$3400","none","none"),
("EAZ588","1978-05-13","Classic","none","none","V8","unknown","none","5237670","$1000","none","June"),
("GF092","1978-05-13","Hornet","1970","none","232","unknown","none","504621","$3100","none","none"),
("BLC906","1978-05-13","Hornet","1970","none","232","Blue and White","none","7093380","$2200","none","October"),
("GPX321","1978-05-06","Hornet","1973","SST","4.2","Silver Grey","none","4986256","$4000","42000kms","November"),
("JQL053","1978-04-29","Matador","1976","none","360","unknown","none","6672484","none","none","none"),
("GCU971","1978-04-29","Hornet","none","SST","4.2","unknown","none","6672484","none","none","none"),
("BLC906","1978-04-29","Hornet","1970","SST","232","Blue and White","none","7093380","$2200","none","October"),
("APC913","1978-04-29","Rebel","1970","none","none","Wagon","none","6614280","$3250","70000mis","none"),
("JMG401","1978-04-22","Matador","none","none","360","Wagon","none","6672484","none","none","none"),
("JQL053","1978-04-22","Matador","1976","none","360","unknown","none","6672484","none","none","none"),
("JRP821","1978-04-22","Hornet","none","SST","4.2","unknown","none","6672484","none","none","none"),
("GME327","1978-04-22","Hornet","1973","SST","4.3","unknown","none","9138077","$4000","none","none"),
("JKQ458","1978-04-22","Rebel","7071","none","360","unknown","none","768711","$2500","none","none"),
("NF303","1978-04-22","Matador","1973","none","360","wagon","none","(047)312049","$5500","none","none"),
("BLC906","1978-04-22","Hornet","1970","SST","none","Blue and White","none","7093380","$2200","none","none"),
("JOF746","1978-04-22","Matador","1976","none","360","Olive","Beige","3494411","none","3785kms","January"),
("EGL334","1978-04-22","American","none","440","none","unknown","none","5257151","$850","none","none"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2425
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
