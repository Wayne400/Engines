
import sqlite3

def get_rover():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("CYS519","1979-05-19","3L","MkI","XX","none","none","unknown","none","9187080","$500","none","none"),
("CQW327","1979-05-19","2000","none","XX","1970","Auto","unknown","none","3448786","$3150","none","none"),
("DWE575","1979-05-19","2000","none","XX","none","none","Grey","Champagne","9189968","$795","none","August"),
("EDQ495","1979-05-19","2000","none","XX","none","Auto","unknown","none","334420","none","53000mis","none"),
("BJV104","1979-05-19","3500","none","XX","none","Auto","unknown","none","9696873","$3750","none","October"),
("EGU555","1979-05-26","3L","MkIII","XX","none","none","unknown","none","474960","$2950","57000mis","October"),
("EQW270","1979-05-26","2000","none","TC","none","none","unknown","none","7993969","$3975","none","none"),
("BEB084","1979-05-26","3500","none","XX","1970","none","unknown","none","3286830","$3300","59000mis","May"),
("CTZ077","1979-05-26","90","none","XX","1953","none","unknown","none","Glebe","$750","none","April"),
("CYF519","1979-06-02","3L","none","XX","none","none","unknown","none","9187080","$300","none","May"),
("AHY817","1979-06-02","3.5L","none","Sedan","1969","Auto","unknown","none","361266","$3750","58000mis","none"),
("AQJ342","1979-06-02","2000","none","TC","1970","none","unknown","none","9601371","$2390","none","none"),
("DYC270","1979-06-02","2000","none","XX","1965","4spd","Cream","Black","6375024","$1250","none","none"),
("EQN270","1979-06-02","2000","none","TC","1971","none","unknown","none","7993969","$3975","none","none"),
("ERH961","1979-06-02","2000","none","XX","1968","none","unknown","none","5256621","$2350","none","none"),
("BEB084","1979-06-02","3500","none","XX","none","none","White","Beige","3286320","$3300","none","May"),
("BQH842","1979-06-02","3500","none","XX","1970","Auto","unknown","none","4493458","$4250","none","none"),
("CQW327","1979-06-02","2000","none","XX","none","none","unknown","none","3448786","$2850","none","none"),



    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 4000
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
