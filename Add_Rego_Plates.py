import sqlite3


def open_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn


def create_table(cursor):
    sql = '''create table adverts (
                 rego_plate text,
                 jurisdiction text,
                 iso_advert_date text,
                 item_number integer,
                 publication text,
                 car_make text,
                 car_model text,
                 model_year text,
                 capacity text,
                 colour text,
                 phone1 text,
                 phone2 text,
                 dealers_licence text,
                 who text)
           '''
    try:
        cursor.execute(sql)
    except:
        pass

def get_adverts():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [("GLO068", "NSW", "1974-10-26", 1 , "smh", "Rambler", "Hornet","1973","none","unknown","9098800","9296125","none","WW"),
("AIG524", "NSW", "1974-10-26", 1, "smh", "Rambler", "Hornet", "1971","none","Mustard","6375781","none","none","WW"),
("GJO325", "NSW", "1974-10-26", 1, "smh", "Rambler", "Ambassador","1970","360", "unknown", "775627", "none", "none", "WW"),
("unknwn", "NSW", "1974-10-26", 1, "smh", "Rambler", "Hornet", "1974","none","Bamboo", "7591672", "none", "none","WW"),
("JBK581", "NSW", "1974-10-26", 1, "smh", "Rambler", "Hornet","1972","4.2", "Peak White", "7476666", "742332", "DL 198","WW"),
("unknwn", "NSW", "1973-01-31", 1, "smh", "Rambler", "Hornet", "1972", "none", "Orange", "7976011","none", "RENAULT-ASHFIELD", "WW"),
("OQR664", "NSW", "1988-01-23", 1, "smh", "Rambler", "Hornet", "none", "none", "none", "8887972","none", "none", "WW"),
("KSF620", "VIC", "1988-01-23", 1, "smh", "Rambler", "Javelin", "1972", "401", "Red", "9083144", "9250893", "none", "WW"),
("MMM190", "NSW", "1988-01-23", 1, "smh", "Rambler", "Matador Wagon", "1976", "none", "none", "3496110","none", "none", "WW")
              ]
    return adverts


def add_adverts(cursor):
    ads = get_adverts()
    for row in ads:
       rego_plate = row[0]
       jurisdiction = row[1]
       iso_advert_date = row[2]
       item_number = row[3]
       publication = row[4]
       car_make = row[5]
       car_model = row[6]
       model_year = row[7]
       capacity = row[8]
       colour = row[9]
       phone1 = row[10]
       phone2 = row[11]
       dealers_licence = row[12]
       who = row[13]
       sql = '''insert into adverts
        (rego_plate, jurisdiction, iso_advert_date, item_number, publication, car_make, car_model, model_year, capacity, colour, phone1, phone2, dealers_licence, who)
        values
        (:rego_plate, :jurisdiction, :iso_advert_date, :item_number, :publication, :car_make, :car_model, :model_year, :capacity, :colour, :phone1, :phone2, :dealers_licence, :who)'''


       cursor.execute(sql, {'rego_plate': rego_plate, 'jurisdiction': jurisdiction, 'iso_advert_date': iso_advert_date, 'item_number': item_number, 'publication':publication, 'car_make':car_make, 'car_model':car_model, 'model_year':model_year, 'capacity':capacity, 'colour':colour, 'phone1':phone1, 'phone2':phone2, 'dealers_licence':dealers_licence, 'who': who})
       print sql, 'Added!'


def main():
    conn = open_database('advertisements.db')
    cursor = conn.cursor()
    create_table(cursor)
    add_adverts(cursor)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()


