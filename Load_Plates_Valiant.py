
import sqlite3

def get_valiant():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("HLI854","1975-08-20","VJ","Charger","770","1975","265","Auto","Sienna","beige","8887866","$new","new","August"),
("JKJ864","1979-09-15","VK","Charger","none","1976","none","none","unknown","none","9776047","$2750","none","none"),
("JJO765","1979-09-15","CL","Charger","none","1977","318","Auto","unknown","none","7278544","$4995","none","none"),
("EQA737","1979-09-15","VH","Charger","770","1973","318","Auto","Silver Grey","Black","6304580","$3300","27000mis","September"),
("GOA028","1979-09-15","VJ","Charger","none","1973","none","none","Golden Amber","none","9825010","$2200","none","none"),
("LAC002","1979-08-11","CL","Charger","770","1978","318","4spd","Alpine White","Blue Cloth","4393099","$6490","none","none"),
("JWD516","1979-08-11","CL","Charger","none","1977","318","Auto","unknown","none","5994455","$3990","none","August"),
("JIG879","1979-08-11","none","Charger","none","1976","318","none","unknown","none","3495055","$3500","none","September"),
("GBA428","1979-08-11","VH","Charger","none","1972","none","Auto","unknown","none","6381823","none","none","none"),
("JGR632","1986-20-10","CL","Valiant","none","1976","245","Auto","Turquoise","none","043844207","none","none","none"),
   ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2951
    for row in ads:
        print row
        master_index1 += 1


        sql = '''insert into adverts (master_index, rego_plate, jurisdiction, iso_advert_date, item_number, publication,
                 car_make, car_model, model_code, model_year, capacity, colour, phone1, phone2, dealers_licence, who, interior_trim,
                  body_style, transmission, model_level, trim_level, price, milage, month)
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_code}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{transmission}", "{model_level}", "{trim_level}","{price}", "{milage}", "{month}")'''

        sql = sql.format(master_index=master_index1, rego_plate=row[0],
                        jurisdiction="NSW",
                        iso_advert_date=row[1],
                        item_number=1, publication="smh",
                        car_make="Chrysler",model_code= row[2], car_model="Valiant", model_year=row[5],
                        capacity=row[6],
                        colour=row[8], phone1=row[10], phone2="none",
                        dealers_licence="none", who="WW", interior_trim=row[9],
                        body_style="none", model_level=row[3], trim_level=row[4],
                        transmission=row[7], price=row[11], milage=row[12],month=row[13])
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

    ads = get_valiant()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
