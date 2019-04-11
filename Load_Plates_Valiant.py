
import sqlite3

def get_valiant():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("CFQ393","1974-06-15","none","Hardtop","none","1971","Hemi","Auto","Vinyl Top","none","Ron Bourke","none","none","none"),
("EEE024","1974-06-15","VC","Safari","none","1967","none","none","unknown","none","5237972","$790","none","none"),
("GLD120","1974-06-15","VJ","Valiant","Ranger","1973","245","Auto","Wagon","none","5228279","$3200","9000kms","July"),
("DBV863","1974-06-15","AP5","Valiant","Regal","none","225","none","unknown","none","9221464","$760","none","none"),
("ASD682","1974-06-15","VF","Hardtop","Regal","none","318","none","unknown","none","5243295","$1975","none","September"),
("AZN532","1974-06-15","VF","Hardtop","770","none","318","Auto","unknown","none","6398886","none","none","February"),
("AJH843","1974-06-15","none","Valiant","Regal","1969","none","none","unknown","none","Liverpool","none","none","none"),
("GDS148","1974-06-15","VH","Valiant","Ranger","1972","245","none","Deep Chartreuse","none","6392013","$2600","none","none"),
("CHO152","1974-06-15","none","VIP","none","1970","318","Auto","unknown","none","Liverpool","none","none","none"),
("GTS332","1974-06-15","none","Charger","none","1973","245","Auto","unknown","none","9292513","$2500","none","April"),
("CNQ941","1974-06-15","VH","Ranger","XL","none","265","Auto","unknown","none","5214275","none","none","none"),
("EWT791","1974-06-15","VE","Valiant","none","none","none","Auto","unknown","none","7506227","$750","none","June"),
("ESL205","1974-06-15","VC","Regal","none","1967","none","Auto","unknown","none","6392582","$1295","none","none"),
("ASU080","1974-06-15","VF","Valiant","none","none","225","Auto","unknown","none","5220241","none","none","none"),
("AVM149","1974-06-15","VF","Regal","770","none","318","Auto","Vinyl Roof","none","6241093","$2150","none","none"),
("EYO024","1974-06-15","VE","VIP","none","none","273","none","Bronze Red","none","4517697","$1500","none","June"),
("ESO218","1974-06-15","AP6","Safari","none","none","none","Auto","unknown","none","485921","$1000","none","none"),
("EGO053","1974-06-15","VC","Regal","none","none","none","Auto","Silver Grey","none","6621327","$1450","none","none"),
("AGT821","1974-06-15","VE","Valiant","none","1969","160HP","Auto","unknown","none","8698506","$1285","none","none"),
("EPM080","1974-08-15","VC","Valiant","none","1967","none","Auto","unknown","none","845728","$1450","37000mis","none"),
("ARR494","1974-08-15","VF","Valiant","none","1969","V8","Auto","unknown","none","7279337","$1150","none","none"),
("CTB476","1974-08-15","S","Valiant","none","1962","225","Auto","unknown","none","5462037","$725","none","none"),
("GHW186","1974-08-15","none","Charger","none","1973","245","Auto","unknown","none","5228018","$2950","12000mis","none"),
   ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 2272
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
