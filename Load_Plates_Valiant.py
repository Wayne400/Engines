
import sqlite3

def get_valiant():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("ADE008","1975-10-18","VE","VIP","none","1968","273","Auto","unknown","none","2112100","nne","none","none"),
("HAP088","1975-10-18","VJ","Charger","Sportsman","1974","none","none","Red and White","Tartan","7976333","none","14700kms","October"),
("DTO408","1976-02-21","none","Valiant","none","none","225","nne","unknown","none","5196765","$290","none","May"),
("AZD532","1976-02-21","VF","Valiant","none","1969","none","Auto","Alabaster","none","7985666","$1550","42070mis","none"),
("AWF177","1976-02-21","VF","Safari","none","1969","225","Auto","Alpine White","Tan","7985666","$1750","65000mis","none"),
("AAJ736","1976-02-21","VF","Valiant","Regal","1969","318","Auto","unknown","none","4515438","$1100","none","August"),
("GJM130","1976-02-21","VJ","Charger","XL","1973","none","none","Red","none","4982186","$2250","42000mis","none"),
("EXY758","1976-02-21","VC","Valiant","Regal","none","225","none","unknown","none","6480475","$1095","none","none"),
("AUF774","1976-02-21","VF","Valiant","VIP","1969","none","none","unknown","none","4985867","$2450","none","October"),
("DZW798","1976-02-21","AP6","Valiant","none","1966","none","Man","unknown","none","6211220","$600","none","April"),
("GNY029","1976-02-21","VJ","Charger","XL","1973","245","none","Silver","none","(048)711242","$2500","52000mis","November"),
("EHK937","1976-02-21","VC","Valiant","Regal","1967","225","Auto","unknown","none","953540","$900","none","none"),
("CIW255","1976-02-21","VH","Charger","XL","none","245","Auto","unknown","none","7715237","$2250","none","November"),
("EIF798","1976-02-21","VH","Charger","none","1972","215","none","Gold","none","6653591","$2390","25000mis","June"),
("CCQ411","1976-02-21","VH","Charger","E38","1971","265","3spd","Sun Roof","none","7591679","$3350","none","none"),
("GSQ099","1976-02-21","VJ","Charger","none","1974","none","Man","Limelight Black Vinyl","none","5993887","$3500","none","none"),
("HLC276","1975-10-11","VJ","Charger","none","1974","265","4spd","unknown","none","8489360","$2750","none","none"),
("GEJ511","1975-10-11","VJ","Charger","none","1973","245","Auto","unknown","none","5879727","$2950","17000mis","none"),
("GPA103","1975-10-11","VJ","Charger","none","7374","none","none","unknown","none","703339","$2600","none","none"),
("GAH806","1975-10-11","VJ","Charger","770","1973","none","Autp","unknown","none","7278737","none","none","October"),
("EDI591","1975-10-11","VH","Charger","770","1972","318","Auto","unknown","none","7474186","$2590","none","March"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2100
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
