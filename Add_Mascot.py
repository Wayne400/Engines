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
                 who text,
                 interior_trim text,
                 body_style text,
                 trim_level text,
                 price text,
                 miles text)
           '''
    try:
        cursor.execute(sql)
    except:
        pass

def get_advertsX():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts =\
        [("GLO068", "NSW", "1974-10-26", 1 , "smh", "Rambler", "Hornet",\
          "1973","none","unknown","9098800","9296125","none","WW", "blue","Sedan","SST", "4990","65000 mis"),
("AIG524", "NSW", "1974-10-26", 1, "smh", "Rambler", "Hornet", "1971",\
 "none","Mustard","6375781","none","none","WW", "red","Sedan","SST", "4990","65000 mis"),
("GJO325", "NSW", "1974-10-26", 1, "smh", "Rambler", "Ambassador","1970",\
 "360", "unknown", "775627", "none", "none", "WW", "yellow","Sedan","SST", "4990","65000 mis"),
("unknwn", "NSW", "1974-10-26", 1, "smh", "Rambler", "Hornet", "1974",\
 "none","Bamboo", "7591672", "none", "none","WW", "green","Sedan","SST", "4990","65000 mis"),
("JBK581", "NSW", "1974-10-26", 1, "smh", "Rambler", "Hornet","1972",\
 "4.2", "Peak White", "7476666", "742332", "DL 198","WW", "bone","Sedan","SST", "4990","65000 mis"),
("unknwn", "NSW", "1973-01-31", 1, "smh", "Rambler", "Hornet", "1972",\
 "none", "Orange", "7976011","none", "RENAULT-ASHFIELD", "WW", "clay","Sedan","SST", "4990","65000 mis"),
("OQR664", "NSW", "1988-01-23", 1, "smh", "Rambler", "Hornet", "none",\
 "none", "none", "8887972","none", "none", "WW", "black","Sedan","SST", "4990","65000 mis"),
("KSF620", "VIC", "1988-01-23", 1, "smh", "Rambler", "Javelin", "1972",\
 "401", "Red", "9083144", "9250893", "none", "WW", "brown","Coupe","SST", "4990","65000 mis"),
("MMM190", "NSW", "1988-01-23", 1, "smh", "Rambler", "Matador", "1976",\
 "none", "none", "3496110","none", "none", "WW", "beige","Wagon","SST", "4990","65000 mis"),
("HWM080", "NSW", "1977-01-01", 1, "smh", "Rambler", "Matador", "1976",\
 "none", "unknown", "6672484","6674460", "none", "WW", "none", "Coupe", "none", "none", "none"),
("MM806", "NSW", "1977-01-01", 2, "smh", "Rambler", "Matador", "7475",\
 "none", "unknown", "6672484", "6674460","none", "WW", "none", "none", "none", "none", "none"),
("JAN981", "NSW", "1977-01-01", 3, "smh", "Rambler", "Matador", "1974",\
 "none", "unknown", "6672484", "6674460","none", "WW", "none", "none", "none", "none", "none"),
("HZI652", "NSW", "1977-01-01", 4, "smh", "Rambler", "Matador", "1974",\
"none", "unknown", "6672484", "6674460","none", "WW", "none", "none", "none", "none", "none"),
("YGD760", "NSW", "1977-01-01", 5, "smh", "Rambler", "Matador", "1974",\
 "none", "unknown", "6672484", "6674460","none", "WW", "none", "none", "none", "none", "none"),
("HDD558", "NSW", "1977-01-01", 6, "smh", "Rambler", "Matador", "none",\
 "none", "unknown", "6672484", "6674460","none", "WW", "none", "none", "none", "none", "none"),
("GOP309", "NSW", "1977-01-01", 7, "smh", "Rambler", "Matador", "none",\
 "none", "unknown", "6672484", "6674460","none", "WW", "none", "none", "none", "none", "none"),
("GGG095", "NSW", "1977-01-01", 8, "smh", "Rambler", "Matador", "none",\
 "none", "unknown", "6672484", "6674460","none", "WW", "none", "Wagon", "none", "none", "none"),
("GLH524", "NSW", "1977-01-01", 9, "smh", "Rambler", "Matador", "none",\
"none", "unknown", "6672484", "6674460","none", "WW", "none", "none", "none", "none", "none"),
("HCN396", "NSW", "1977-01-01", 10, "smh", "Rambler", "Matador", "none",\
"none", "unknown", "6672484","6674460","none", "WW", "none", "none", "none", "none", "none"),
("ELI190", "NSW", "1977-01-01", 11, "smh", "Rambler", "Matador", "none",\
"none", "unknown", "6672484","6674460","none", "WW", "none", "none", "none", "none", "none"),
("GAX724", "NSW", "1977-01-01", 12, "smh", "Rambler", "Matador", "none",\
 "none", "unknown", "6672484","6674460","none", "WW", "none", "Wagon", "none", "none", "none"),
("GBF500", "NSW", "1977-01-01", 13, "smh", "Rambler", "Matador", "none",\
"none", "unknown", "6672484","6674460","none", "WW", "none", "none", "none", "none", "none"),
("HDS432", "NSW", "1977-01-01", 14, "smh", "Rambler", "Javelin", "none",\
"none", "unknown", "6672484","6674460","none", "WW", "none", "Coupe", "none", "none", "none"),
("HFJ677", "NSW", "1977-01-01", 15, "smh", "Rambler", "Javelin", "none",\
"none", "unknown", "6672484","6674460","none", "WW", "none", "Coupe", "none", "none", "none"),
("EVO277", "NSW", "1977-01-01", 16, "smh", "Rambler", "American", "none",\
"6 cyl", "unknown", "6672484","6674460","none", "WW", "none", "none", "440", "none", "none"),
("EIR754", "NSW", "1977-01-01", 17, "smh", "Rambler", "Hornet", "none",\
 "4.2", "unknown", "6672484", "6674460","none", "WW", "none", "none", "none", "none", "none"),
("BMZ329", "NSW", "1977-01-01", 18, "smh", "Rambler", "Hornet", "none",\
"none", "unknown", "6672484", "6674460","none", "WW", "Red", "none", "none", "none", "none"),
("GZQ779", "NSW", "1977-01-01", 19, "smh", "Rambler", "Hornet", "none",\
 "none", "unknown", "6672484", "6674460","none", "WW", "none", "none", "none", "none", "none"),
("DIA925", "NSW", "1977-01-01", 20, "smh", "Rambler", "Hornet", "none",\
 "4.2", "unknown", "6672484", "6674460","none", "WW", "none", "none", "none", "none", "none"),
("HZG682", "NSW", "1977-01-01", 21, "smh", "Rambler", "Hornet", "1973",\
"4.2", "unknown", "6672484", "6674460","none", "WW", "none", "none", "none", "none", "none"),
("BFJ871", "NSW", "1977-01-01", 22, "smh", "Rambler", "Rebel", "1970",\
"none", "unknown", "6672484", "6674460","none", "WW", "none", "none", "none", "none", "none"),
("BJR857", "NSW", "1977-01-01", 23, "smh", "Rambler", "Rebel", "1970",\
"360", "unknown", "6672484", "6674460","none", "WW", "none", "none", "none", "none", "none"),
("AXF128", "NSW", "1977-01-01", 24, "smh", "Rambler", "Rebel", "none",\
"290", "unknown", "6672484", "6674460","none", "WW", "vinyl", "none", "none", "none", "none"),
("GEZ762", "NSW", "1977-01-01", 25, "smh", "Rambler", "Rebel", "none",\
"none", "unknown", "6672484", "6674460","none", "WW", "none", "Wagon", "none", "none", "none"),
("AHY052", "NSW", "1977-01-01", 26, "smh", "Rambler", "Rebel", "none",\
"none", "unknown", "6672484", "6674460","none", "WW", "none", "Wagon", "none", "none", "none"),
("DYP313", "NSW", "1977-01-01", 27, "smh", "Rambler", "Classic", "1965",\
"none", "unknown", "6672484","6674460","none", "WW", "none", "none", "660", "none", "none"),

         ]
    return adverts


def get_adverts():  # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [

        ("HWM080", "NSW", "1977-01-01", 1, "smh", "Rambler", "Matador", "1976", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "Coupe", "none", "none", "none"),
        ("MM806", "NSW", "1977-01-01", 2, "smh", "Rambler", "Matador", "7475", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("JAN981", "NSW", "1977-01-01", 3, "smh", "Rambler", "Matador", "1974", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("HZI652", "NSW", "1977-01-01", 4, "smh", "Rambler", "Matador", "1974", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("YGD760", "NSW", "1977-01-01", 5, "smh", "Rambler", "Matador", "1974", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("HDD558", "NSW", "1977-01-01", 6, "smh", "Rambler", "Matador", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("GOP309", "NSW", "1977-01-01", 7, "smh", "Rambler", "Matador", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("GGG095", "NSW", "1977-01-01", 8, "smh", "Rambler", "Matador", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "Wagon", "none", "none", "none"),
        ("GLH524", "NSW", "1977-01-01", 9, "smh", "Rambler", "Matador", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none")




    ]
    return adverts

def add_adverts(cursor):
    ads = get_advertsX()
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
       interior_trim = row[14]
       body_style = row[15]
       trim_level = row[16]
       price = row[17]
       miles = row[18]
       sql = '''insert into adverts
        (rego_plate, jurisdiction, iso_advert_date, item_number, publication, car_make, car_model, model_year, \
         capacity, colour, phone1, phone2, dealers_licence, who, interior_trim, body_style, trim_level, price, miles)
        values
        (:rego_plate, :jurisdiction, :iso_advert_date, :item_number, :publication, :car_make, :car_model, :model_year,\
         :capacity, :colour, :phone1, :phone2, :dealers_licence, :who, :interior_trim, :body_style, :trim_level,\
          :price, :miles)'''


       cursor.execute(sql, {'rego_plate': rego_plate, 'jurisdiction': jurisdiction, 'iso_advert_date': iso_advert_date,\
                            'item_number': item_number, 'publication':publication, 'car_make':car_make,\
                            'car_model':car_model, 'model_year':model_year, 'capacity':capacity, 'colour':colour,\
                            'phone1':phone1, 'phone2':phone2, 'dealers_licence':dealers_licence, 'who': who,\
                            'interior_trim':interior_trim, 'body_style':body_style, 'trim_level':trim_level,\
                            'price':price, 'miles':miles})
       print sql, 'Added!'


def main():
    conn = open_database('advertisements_mascot.db')
    cursor = conn.cursor()
    create_table(cursor)
    add_adverts(cursor)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()


