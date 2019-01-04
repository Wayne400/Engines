import sqlite3


def open_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn


def get_adverts():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
("JKQ458", "NSW", "1978-12-02", 1, "smh", "Rambler", "Rebel", "1970", "360", "unknown", "785122", "none", "LD223", "WW", "none", "none", "none", "none"),
("BQH878", "NSW", "1978-12-02", 1, "smh", "Rambler", "Hornet","1971","none","unknown","8480451","none","none","WW","none","none","none","none"),
("GVU672", "NSW", "1978-12-02", 1, "smh", "Rambler", "Hornet","1971","none", "unknown", "4519221", "none", "none", "WW","none","none","none","none"),
("CTJ846", "NSW", "1974-11-09", 1, "smh", "Rambler", "Ambassador", "none","none","unknown", "842371", "none", "none","WW","none","sedan","none","none"),
("KMK673", "NSW", "1980-11-05", 1, "smh", "Rambler", "Matador","1973","unknown", "unknown", "862866", "none", "DL 198","WW","none","wagon","none","none"),
("BKQ184", "NSW", "1974-04-06", 1, "smh", "Rambler", "Hornet", "unknown", "none", "White", "839896","none", "none", "WW","Brown","none","none","none"),
("GKZ716", "NSW", "1977-07-02", 1, "smh", "Rambler", "Hornet", "1973", "none", "Silver Grey Metallic", "321820","2122539", "none", "WW","chamois","Sedan","none", "$5250"),
("HPN843", "NSW", "1976-03-13", 1, "smh", "Rambler", "Hornet", "1973", "4.2", "unknown", "6220743", "6228761", "DL 913", "WW","none","none","none","$3590"),
("DNF054", "NSW", "1979-03-10", 1, "smh", "Rambler", "Hornet", "1971", "258", "none", "9821697","none", "none", "WW","none","none","none","$2900")
              ]
    return adverts


def add_adverts(cursor):
    ads = get_adverts()
    for row in ads:
       print row
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
       trim = row[14]
       body_style = row[15]
       trim_level = row[16]
       price = row[17]
       sql = '''insert into adverts
        (rego_plate, jurisdiction, iso_advert_date, item_number, publication, car_make, car_model, model_year, capacity, colour, phone1, phone2, dealers_licence, who, trim, body_style, trim_level, price)
        values
        (:rego_plate, :jurisdiction, :iso_advert_date, :item_number, :publication, :car_make, :car_model, :model_year, :capacity, :colour, :phone1, :phone2, :dealers_licence, :who, :trim, :body_style, :trim_level, :price )'''

       print sql
       cursor.execute(sql, {'rego_plate': rego_plate, 'jurisdiction': jurisdiction, 'iso_advert_date': iso_advert_date, 'item_number': item_number, 'publication':publication,
                            'car_make':car_make, 'car_model':car_model, 'model_year':model_year, 'capacity':capacity, 'colour':colour, 'phone1':phone1, 'phone2':phone2,
                            'dealers_licence':dealers_licence, 'who': who, 'trim':trim, 'body_style':body_style, 'trim_level':trim_level, 'price':price })
       print sql, 'Added!'


def main():
    conn = open_database('advertisements.db')
    cursor = conn.cursor()
    add_adverts(cursor)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()


