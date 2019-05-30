





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("GSM034","1978-09-30","Rambler","1966","none","none","unknown","none","5606396","$300","none","none"),
("JHV165","1978-09-30","Rebel","1969","none","V8","Ivory","Black","6823692","$1450","none","July"),
("JIK985","1978-09-30","Rebel","none","none","none","White","Blue","6375024","$2750","none","none"),
("Hornet","1978-09-23","Hornet","1973","none","4.2","Wrecking Grafton","none","(066)422069","none","none","none"),
("Hornet","1978-09-23","Hornet","1973","none","none","unknown","none","319174","none","none","none"),
("DHA434","1978-09-23","Classic","none","660","287","Off White","Red","6370407","none","53800mis","May"),
("HLM408","1978-09-23","Matador","1975","none","360","White","Red","740554","$6750","65000kms","none"),
("GF945","1978-09-23","Matador","none","none","none","unknown","none","6672484","none","none","none"),
("CQD263","1978-09-16","Hornet","1972","none","4.2","unknown","none","9384250","$3450","none","none"),
("HLM408","1978-09-16","Matador","1975","none","360","White","Red","740554","$6995","65000kms","none"),
("EST844","1978-09-16","American","none","440","6cyl","unknown","none","9777373","$1400","none","January"),
("ACQ557","1978-09-09","Hornet","1970","SST","232","unknown","none","6374715","$2250","none","none"),
("JGZ821","1978-09-09","Rebel","1969","none","V8","Cream","Black","4765068","$1500","none","none"),
("American","1978-09-02","American","1966","none","6cyl","unknown","none","5257151","$690","none","none"),
("Rebel","1978-09-02","Rebel","1971","SST","V8","Light Blue Wagon","Bone","5229108","$4990","none","none"),
("Matador","1978-09-02","Matador","1977","none","360","Yellow","Cloth","5229108","$8990","19000kms","none"),
("GKZ716","1978-09-02","Hornet","1973","none","4.2","Irridescent Grey","none","321820","none","21000mis","June"),
("JWO104","1978-09-02","Hornet","1975","none","4.2","unknown","none","3584644","$4999","none","August"),
("JN230","1978-09-02","Hornet","1972","none","4.2","White","Red","6511375","$3250","none","July"),
("HXX678","1978-09-02","Hornet","1975","none","4.2","unknown","none","461828","$4850","none","August"),
    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2729
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
