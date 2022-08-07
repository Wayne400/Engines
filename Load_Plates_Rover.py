
import sqlite3

def get_rover():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("CWE193","1985-06-01","3L","MkII","XX","1963","none","unknown","none","901268","$2000","none","none"),
("DXE503","1985-06-01","3L","none","XX","1965","Auto","unknown","none","465241","$2300","none","March"),
("ABW847","1985-06-01","2000","none","XX","1968","none","Off-White","Black","6344679","$2800","none","October"),
("BMI968","1985-06-01","2000","none","XX","1969","Man","unknown","none","(043)257360","$1050","none","April"),
("GAS528","1985-06-01","2000","none","TC","1971","Man","unknown","none","4981375","$2500","none","none"),
("GQR792","1985-06-01","2000","none","XX","1970","none","unknown","none","955860","$1750","none","none"),
("A0A264","1984-03-10","3.5","none","XX","1969","none","unknown","none","3272329","$3200","40000mis","none"),
("AGI101","1984-03-10","3500","none","XX","1970","none","unknown","none","8181153","none","none","none"),
("A0A273","1984-03-10","P5Bcoupe","none","XX","1969","none","unknown","none","3272329","$3200","40000mis","none"),
("KMG348","1984-03-17","3500","SDI","XX","1979","Auto","Deep Blue","none","5023522","$10250","none","November"),
("CDL973","1984-05-05","3L","none","XX","1961","none","unknown","none","3575407","none","none","none"),
("DUH642","1984-05-12","3L","MKII","XX","none","none","unknown","none","9293347","$2600","none","none"),
("AWQ416","1984-10-27","2000","none","XX","none","Auto","unknown","none","484001","$2800","none","none"),
("ERX360","1984-10-27","2000","none","XX","none","Auto","unknown","none","3985546","$300","none","November"),
("DYC883","1984-11-03","P5coupe","MKII","XX","1965","Auto","unknown","none","4873576","$3000","57000mis","November"),
("CTQ023","1984-11-17","2000","none","XX","1972","Auto","B.R.G.","Tan","6626536","$3200","40000mis","none"),
("BBJ058","1984-12-01","2000","MKII","TC","1971","Auto","unknown","none","4498649","$950","none","July"),
("HHN648","1984-12-01","3500","none","XX","1974","Auto","White","none","4672941","$4300","82000mis","April"),
("DAI158","1984-12-08","3500","none","XX","none","none","unknown","none","4985039","$4250","none","none"),

    ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 4105
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
GAA


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
