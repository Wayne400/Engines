
import sqlite3

def get_rover():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("APO981","1979-04-28","3L","MkIII","XX","none","Auto","unknown","Bone Leather","3986287","$3500","none","none"),
("DGT553","1979-04-28","3L","none","XX","1967","Auto","unknown","none","4501524","$2450","55000mis","none"),
("EJO608","1979-04-28","3L","none","XX","1966","Auto","unknown","none","9976675","$1100","none","January"),
("ETP103","1979-04-28","3L","none","XX","none","Auto","unknown","none","3874513","$1500","none","none"),
("GHN861","1979-04-28","3500","none","S","1973","Man","unknown","none","7988652","$5600","none","none"),
("AHY817","1979-05-05","P5B","none","XX","1969","Auto","White","Burgundy","361266","none","58000mis","none"),
("EGJ680","1979-05-05","3L","MkIII","XX","none","Auto","White","Red Leather","9092594","$1650","none","January"),
("EJO698","1979-05-05","3L","MkII","XX","1966","none","unknown","none","9976675","$1100","none","January"),
("AIB891","1979-05-05","P5B","none","XX","1971","Auto","Light Grey","Red Leather","5229108","$4990","52000mis","none"),
("DYC270","1979-05-05","2000","none","XX","1965","Man","unknown","none","6375024","none","none","none"),
("DYK999","1979-05-05","2000","none","XX","1965","Man","unknown","none","5215811","$499","none","January"),
("BBZ296","1979-05-05","90","none","XX","1956","none","Black","none","6307229","none","none","none"),
("CTA626","1979-05-05","105","none","S","none","Man","unknown","none","4499480","$700","none","June"),



    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3987
    for row in ads:
        print row
        master_index1 += 1


        sql = '''insert into adverts (master_index, rego_plate, jurisdiction, iso_advert_date, item_number, publication,
                 car_make, car_model, model_year, capacity, colour, phone1, phone2, dealers_licence, who, interior_trim,
                  body_style, transmission, model_code, trim_level, price, milage, month)
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{transmission}", "{model_code}", "{trim_level}","{price}", "{milage}", "{month}")'''

        sql = sql.format(master_index=master_index1, rego_plate=row[0],
                        jurisdiction="NSW",
                        iso_advert_date=row[1],
                        item_number=1, publication="smh",
                        car_make="Rover", car_model=row[2], model_year=row[5],
                        capacity="none",
                        colour=row[7], phone1=row[9], phone2="none",
                        dealers_licence="none", who="WW", interior_trim=row[8],
                        body_style="none", model_code=row[3], trim_level=row[4],
                        transmission=row[6], price=row[10], milage=row[11],month=row[12])
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

    ads = get_rover()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
