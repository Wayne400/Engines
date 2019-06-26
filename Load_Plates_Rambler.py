





import sqlite3

def get_rambler_1():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("Matador","1980-06-07","Matador","1976","none","none","Wagon 8-seat","none","3561296","$7995","none","none"),
("JCG870","1980-06-07","Matador","none","none","none","Beautiful & Powerful","none","767184","$3000","none","none"),
("HJU539","1980-06-07","Javelin","none","none","401","unknown","none","6672484","none","none","none"),
("KKL312","1980-06-07","X","1977","none","none","unknown","none","6672484","none","none","none"),
("KRL391","1980-06-07","Javelin","none","none","390","unknown","none","6672484","none","none","none"),
("HNH802","1980-06-07","Hornet","1975","none","4.2","Blue","White","6375024","$4995","none","none"),
("American","1980-06-21","American","330","none","none","unknown","none","6471595","$250","none","nne"),
("EVC996","1980-06-21","American","none","none","none","Steel Grey","Red","7989993","$2495","none","May"),
("ERX738","1980-06-21","Classic","1967","none","V8","unknown","none","6602098","$1250","none","October"),
("HRY380","1980-06-21","Hornet","1975","none","4.2","Red Pepper","Black","7278877","$3995","none","April"),
("Hornet","1980-06-21","Hornet","7172","none","none","unknown","none","9493374","none","none","none"),
("QM809","1980-06-21","Javelin","none","none","343","unknown","none","6672484","$3950","none","none"),
("KKL312","1980-06-21","X","1977","none","none","unknown","none","6672484","none","none","none"),
("EVC996","1980-06-28","American","none","none","none","Steel Grey","Red","7989993","$2495","none","May"),
("JSF811","1980-05-28","Hornet","7576","none","none","April Yellow","Bone","7970516","$4950","none","November"),
("HNH802","1980-05-28","Hornet","1975","none","4.2","Blue","White","6375024","$3995","none","none"),
("CQU140","1980-06-28","Matador","none","none","none","unknown","none","7984028","$3950","none","none"),
("JK574","1980-06-28","Matador","1972","none","none","unknown","none","6379495","$1450","none","none"),
("KTE911","1980-06-28","Matador","1976","none","none","Wagon 9-seat","none","812281","$6995","none","none"),
("GBI386","1980-06-28","Rebel","1967","none","290","unknown","none","851554","$1000","none","December"),
("HSI980","1980-06-28","Rebel","1968","none","none","Wagon","none","6012019","$350","none","none"),
("JRZ132","1980-07-05","American","none","none","none","unknown","none","5971695","$1990","37800mis","none"),
("BTQ613","1980-07-05","Classic","1965","none","none","unknown","none","506780","$650","none","June"),
("EOA138","1980-07-05","Rambler","1967","none","none","unknown","none","5693211","auction","none","none"),
("DVS005","1980-07-05","Rambler","1969","none","none","unknown","none","5693211","auction","none","none"),
("HNH802","1980-07-05","Hornet","1975","none","4.2","Blue","White","6375024","$4995","none","none"),
("JBQ160","1980-07-05","Hornet","1976","none","4.2","unknown","none","4223842","$2850","57000kms","none"),
("EXG275","1980-07-05","Javelin","1971","none","390","unknown","none","6051397","$5000","none","none"),
("GUZ275","1980-07-05","Matador","1973","none","none","unknown","none","illegible","none","none","June"),
("HWC987","1980-07-05","Matador","none","none","none","Wagon 9-seat","none","6672484","none","46000kms","July"),
("KQT441","1980-07-05","Matador","none","none","none","Wagon 9-seat","none","7265000","$3990","none","May"),
("KTA911","1980-07-05","Matador","1976","none","none","Wagon 9-seat","none","812281","$6500","none","none"),
("JSF811","1980-07-12","Hornet","7576","none","none","April Yellow","Bone","7970393","$4250","24000kms","November"),
("JK574","1980-07-12","Matador","1972","none","none","unknown","none","6379495","$1100","none","none"),
("KTA911","1980-07-12","Matador","1976","none","none","Wagon 9-seat","none","812281","$6500","none","none"),
("OPL179","1980-07-12","Rebel","1969","none","none","unknown","none","5195157","$430","none","none"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 3149
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
