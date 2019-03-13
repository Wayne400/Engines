
import sqlite3

def get_valiant():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("DZZ161","1974-07-13","AP6","none","none","225","Auto","Wagon","none","518760","$275","none","none"),
("APX067","1974-07-13","VF","Regal","none","225","none","Wagon","none","5286004","$1895","none","none"),
("ENG623","1974-07-13","none","Regal","1967","225","Auto","unknown","none","5286859","$1700","14000mis","none"),
("DUP961","1974-07-13","AP6","Regal","6566","225","Auto","unknown","none","6311431","$695","none","none"),
("DJM017","1974-07-13","VC","none","6667","273","Auto","unknown","none","5257724","none","none","none"),
("BHZ940","1974-07-13","VG","none","1970","245","Auto","unknown","none","7278325","none","38000mis","none"),
("AGJ095","1974-07-13","VE","Regal","1969","225","Auto","Vinyl Top","none","345509","$1400","none","none"),
("DTW795","1974-07-13","AP6","none","none","225","none","unknown","none","6451219","$650","none","July"),
("AOO005","1974-07-13","VF","none","1970","225","Man","unknown","none","954955","$980","none","none"),
("DRH165","1974-07-13","AP5","none","1965","225","none","unknown","none","942813","$600","none","none"),
("EFL885","1974-07-13","VC","Regal","1967","225","Auto","White","none","4672399","none","none","none"),
("COQ035","1974-07-13","VH","Ranger","1972","245","Auto","Vinyl Top","none","8698506","none","none","none"),
("EBJ435","1974-07-13","AP6","Regal","none","273","Auto","Vinyl Top","none","5876511","$950","none","May"),
("AVN149","1974-07-13","VF","Regal 770","none","273","Auto","Vinyl Top","none","6241093","$1950","none","none"),
("EYO064","1974-07-13","VE","VIP","1968","273","Auto","unknown","none","4517697","$1475","none","none"),
("AUG595","1974-07-13","VF","Regal","1970","160HP","none","unknown","none","East Ryde","$2090","none","January"),
("GMP021","1974-07-13","VJ","E55","1973","340","Auto","unknown","none","295244","none","none","October"),
("EUX134","1974-07-13","VE","VIP","1969","273","Auto","Blue","none","333757","$1750","27000mis","January"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2049
    for row in ads:
        print row
        master_index1 += 1


        sql = '''insert into adverts (master_index, rego_plate, jurisdiction, iso_advert_date, item_number, publication,
                 car_make, car_model, model_code, model_year, capacity, colour, phone1, phone2, dealers_licence, who, interior_trim,
                  body_style, transmission, trim_level, price, milage, month)
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_code}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{transmission}", "{trim_level}","{price}", "{milage}", "{month}")'''

        sql = sql.format(master_index=master_index1, rego_plate=row[0],
                        jurisdiction="NSW",
                        iso_advert_date=row[1],
                        item_number=1, publication="smh",
                        car_make="Chrysler",model_code= row[2], car_model="Valiant", model_year=row[4],
                        capacity=row[5],
                        colour=row[7], phone1=row[9], phone2="none",
                        dealers_licence="none", who="WW", interior_trim=row[8],
                        body_style="none", trim_level=row[3],
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

    ads = get_valiant()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
