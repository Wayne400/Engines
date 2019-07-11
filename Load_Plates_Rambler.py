





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("BD486","1982-04-02","Hornet","1974","none","none","air-con","none","3872968","$3500","none","none"),
("Matador","1982-04-02","Matador","none","none","none","Cream","Red","(049)468616","$4800","47000mis","none"),
("BIW994","1982-04-02","Rebel","none","none","none","unknown","none","3447797","$1400","none","none"),
("FSR166","1982-04-10","Matador","1974","none","none","unknown","none","7266594","nonee","none","none"),
("NYX448","1982-04-10","Rebel","1969","none","none","unknown","none","465992","none","none","none"),
("LME919","1982-04-10","X-Coupe","1977","none","V8","unknown","none","9183705","$6750","none","none"),
("GAD870","1982-04-17","Javelin","none","none","290","Needs work","none","862794","$2400","none","none"),
("JME108","1982-04-17","Rebel","1969","none","none","Wagon","none","(047)363716","$2200","none","November"),
("LME919","1982-04-17","X-Coupe","1977","none","none","unknown","none","9183705","$6700","none","April"),
("HPN843","1982-05-18","Hornet","none","none","4.2","unknown","none","5870218","$1499","none","April"),
("HZF497","1997-11-01","Hornet","1975","none","4.2","White","none","(049)661352","$4500","none","October"),
("LZY981","1990-09-01","Hornet","1975","none","4.2","unknown","none","6531589","$4000","none","October"),
("PXA932","1997-11-01","Hornet","1975","none","327","Chev motor wild stripes","none","(047(218010","$7999","none","none"),
("PYN840","1992-08-01","Hornet","1975","none","360","Red ex-HRY380 ","none","7724304","$4500","none","October"),
      ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3458
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
