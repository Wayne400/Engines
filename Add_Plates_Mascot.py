import sqlite3

def create_table():

    conn = sqlite3.connect('advertisements_mascot.db')
    cursor = conn.cursor()
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
                 trim text,
                 body_style text,
                 trim_level text,
                 price text,
                 milage text)'''
    print sql
    try:
        cursor.execute(sql)
    except:
        print ("failed to create table")
        pass



def get_adverts():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
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
         "none", "WW", "none", "none", "none", "none", "none"),
        (
        "HCN396", "NSW", "1977-01-01", 10, "smh", "Rambler", "Matador", "none", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "none", "none", "none", "none"),
        (
        "ELI190", "NSW", "1977-01-01", 11, "smh", "Rambler", "Matador", "none", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "none", "none", "none", "none"),
        (
        "GAX724", "NSW", "1977-01-01", 12, "smh", "Rambler", "Matador", "none", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "Wagon", "none", "none", "none"),
        ("GBF500", "NSW", "1977-01-01", 13, "smh", "Rambler", "Matador", "none", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "none", "none", "none", "none"),
        (
        "HDS432", "NSW", "1977-01-01", 14, "smh", "Rambler", "Javelin", "none", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "Coupe", "none", "none", "none"),
        (
        "HFJ677", "NSW", "1977-01-01", 15, "smh", "Rambler", "Javelin", "none", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "Coupe", "none", "none", "none"),
        ("EVO277", "NSW", "1977-01-01", 16, "smh", "Rambler", "American", "none", "6 cyl", "unknown", "6672484",
         "6674460",
         "none", "WW", "none", "none", "440", "none", "none"),
        ("EIR754", "NSW", "1977-01-01", 17, "smh", "Rambler", "Hornet", "none", "4.2", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("BMZ329", "NSW", "1977-01-01", 18, "smh", "Rambler", "Hornet", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "Red", "none", "none", "none", "none"),
        ("GZQ779", "NSW", "1977-01-01", 19, "smh", "Rambler", "Hornet", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("DIA925", "NSW", "1977-01-01", 20, "smh", "Rambler", "Hornet", "none", "4.2", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("HZG682", "NSW", "1977-01-01", 21, "smh", "Rambler", "Hornet", "1973", "4.2", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("BFJ871", "NSW", "1977-01-01", 22, "smh", "Rambler", "Rebel", "1970", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("BJR857", "NSW", "1977-01-01", 23, "smh", "Rambler", "Rebel", "1970", "360", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("AXF128", "NSW", "1977-01-01", 24, "smh", "Rambler", "Rebel", "none", "290", "unknown", "6672484", "6674460",
         "none", "WW", "vinyl", "none", "none", "none", "none"),
        ("GEZ762", "NSW", "1977-01-01", 25, "smh", "Rambler", "Rebel", "1972", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "Wagon", "none", "none", "none"),
        ("AHY052", "NSW", "1977-01-01", 26, "smh", "Rambler", "Rebel", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "Wagon", "none", "none", "none"),
        (
        "DYP313", "NSW", "1977-01-01", 27, "smh", "Rambler", "Classic", "1965", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "none", "660", "none", "none"),

        ("HFJ677", "NSW", "1977-01-08", 1, "smh", "Rambler", "Javelin", "none", "390", "unknown", "6672484", "6674460",
         "none", "WW", "none", "Coupe", "none", "none", "none"),
        (
        "GAX724", "NSW", "1977-01-08", 2, "smh", "Rambler", "Matador", "1974", "none", "Burgundy", "6672484", "6674460",
        "none", "WW", "none", "none", "none", "none", "none"),
        ("BJR857", "NSW", "1977-01-08", 3, "smh", "Rambler", "Rebel", "1970", "none", "Blue", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("GLH524", "NSW", "1977-01-08", 4, "smh", "Rambler", "Matador", "1972", "none", "White", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("GEZ762", "NSW", "1977-01-08", 5, "smh", "Rambler", "Rebel", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "Wagon", "none", "none", "none"),
        ("GZQ779", "NSW", "1977-01-08", 6, "smh", "Rambler", "Hornet", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("ELI190", "NSW", "1977-01-08", 7, "smh", "Rambler", "Matador", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("DIA925", "NSW", "1977-01-08", 8, "smh", "Rambler", "Hornet", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("HCN396", "NSW", "1977-01-08", 9, "smh", "Rambler", "Matador", "1972", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("JAG756", "NSW", "1977-01-08", 10, "smh", "Rambler", "Hornet", "1975", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("JAN891", "NSW", "1977-01-08", 11, "smh", "Rambler", "Matador", "none", "none", "White", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("GGG095", "NSW", "1977-01-08", 12, "smh", "Rambler", "Matador", "1972", "none", "Blue", "6672484", "6674460",
         "none", "WW", "none", "Wagon", "none", "none", "none"),
        ("HDD558", "NSW", "1977-01-08", 13, "smh", "Rambler", "Matador", "1972", "none", "Brown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("EVO277", "NSW", "1977-01-08", 14, "smh", "Rambler", "American", "1968", "6-cyl", "unknown", "6672484",
         "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("HZG682", "NSW", "1977-01-08", 15, "smh", "Rambler", "Hornet", "1973", "none", "Red", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("AHY052", "NSW", "1977-01-08", 16, "smh", "Rambler", "Rebel", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "Wagon", "none", "none", "none"),
        (
        "HWM080", "NSW", "1977-01-08", 17, "smh", "Rambler", "Matador", "1976", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "none", "none", "none", "none"),
        ("AVQ155", "NSW", "1977-01-08", 18, "smh", "Rambler", "American", "1968", "none", "White", "6672484", "6674460",
         "none", "WW", "Red", "none", "none", "none", "none"),
        (
        "MM 806", "NSW", "1977-01-08", 19, "smh", "Rambler", "Matador", "7475", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "none", "none", "none", "none"),
        (
        "HZI652", "NSW", "1977-01-08", 20, "smh", "Rambler", "Matador", "1974", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "none", "none", "none", "none"),
        ("AXF128", "NSW", "1977-01-08", 21, "smh", "Rambler", "Rebel", "1968", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        (
        "JBH340", "NSW", "1977-01-08", 22, "smh", "Rambler", "Matador", "7475", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "none", "none", "none", "none"),
        ("BMZ329", "NSW", "1977-01-08", 23, "smh", "Rambler", "Hornet", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        (
        "GOP309", "NSW", "1977-01-08", 24, "smh", "Rambler", "Matador", "none", "none", "unknown", "6672484", "6674460",
        "none", "WW", "vinyl", "none", "none", "none", "none"),
        ("EIR754", "NSW", "1977-01-08", 25, "smh", "Rambler", "Hornet", "1972", "none", "Sienna Brown", "6672484",
         "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),

        ("HFJ677", "NSW", "1977-01-15", 1, "smh", "Rambler", "Javelin", "none", "390", "unknown", "6672484", "6674460",
         "none", "WW", "none", "Coupe", "none", "none", "none"),
        (
        "GAX724", "NSW", "1977-01-15", 2, "smh", "Rambler", "Matador", "1974", "none", "Burgundy", "6672484", "6674460",
        "none", "WW", "none", "none", "none", "none", "none"),
        ("BJR857", "NSW", "1977-01-15", 3, "smh", "Rambler", "Rebel", "1970", "none", "Blue", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("GLH524", "NSW", "1977-01-15", 4, "smh", "Rambler", "Matador", "1972", "none", "White", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("GEZ762", "NSW", "1977-01-15", 5, "smh", "Rambler", "Rebel", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "Wagon", "none", "none", "none"),
        ("GZQ779", "NSW", "1977-01-15", 6, "smh", "Rambler", "Hornet", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("ELI190", "NSW", "1977-01-15", 7, "smh", "Rambler", "Matador", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("DIA925", "NSW", "1977-01-15", 8, "smh", "Rambler", "Hornet", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("HCN396", "NSW", "1977-01-15", 9, "smh", "Rambler", "Matador", "1972", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("JAG756", "NSW", "1977-01-15", 10, "smh", "Rambler", "Hornet", "1975", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("JAN891", "NSW", "1977-01-15", 11, "smh", "Rambler", "Matador", "none", "none", "White", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("GGG095", "NSW", "1977-01-15", 12, "smh", "Rambler", "Matador", "1972", "none", "Blue", "6672484", "6674460",
         "none", "WW", "none", "Wagon", "none", "none", "24000 mis"),
        ("HDD558", "NSW", "1977-01-15", 13, "smh", "Rambler", "Matador", "1972", "none", "Brown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("EVO277", "NSW", "1977-01-15", 14, "smh", "Rambler", "American", "1968", "6-cyl", "unknown", "6672484",
         "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        ("HZG682", "NSW", "1977-01-15", 15, "smh", "Rambler", "Hornet", "1973", "none", "White", "6672484", "6674460",
         "none", "WW", "Red", "none", "none", "none", "none"),
        ("AHY052", "NSW", "1977-01-15", 16, "smh", "Rambler", "Rebel", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "Wagon", "none", "none", "none"),
        (
        "HWM080", "NSW", "1977-01-15", 17, "smh", "Rambler", "Matador", "1976", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "none", "none", "none", "3000 kms"),
        ("AVO155", "NSW", "1977-01-15", 18, "smh", "Rambler", "American", "1968", "none", "White", "6672484", "6674460",
         "none", "WW", "Red", "none", "none", "none", "26000 mis"),
        (
        "MM 806", "NSW", "1977-01-15", 19, "smh", "Rambler", "Matador", "7475", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "none", "none", "none", "8000 kms"),
        (
        "HZI652", "NSW", "1977-01-15", 20, "smh", "Rambler", "Matador", "1974", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "none", "none", "none", "27000 mis"),
        ("AXF128", "NSW", "1977-01-15", 21, "smh", "Rambler", "Rebel", "1968", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        (
        "JBH340", "NSW", "1977-01-15", 22, "smh", "Rambler", "Matador", "7475", "none", "unknown", "6672484", "6674460",
        "none", "WW", "none", "none", "none", "none", "none"),
        ("BMZ329", "NSW", "1977-01-15", 23, "smh", "Rambler", "Hornet", "none", "none", "unknown", "6672484", "6674460",
         "none", "WW", "none", "none", "none", "none", "none"),
        (
        "GOP309", "NSW", "1977-01-15", 24, "smh", "Rambler", "Matador", "none", "none", "unknown", "6672484", "6674460",
        "none", "WW", "vinyl", "none", "none", "none", "none"),
        ("EIR754", "NSW", "1977-01-15", 25, "smh", "Rambler", "Hornet", "1972", "none", "Sienna Brown", "6672484",
         "6674460", "none", "WW", "none", "none", "none", "none", "none")
              ]
    return adverts


def add_adverts(ads):
    db_name = 'advertisements_mascot.db'
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

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
       milage = row[18]
       sql = '''insert into adverts
        (rego_plate, jurisdiction, iso_advert_date, item_number, publication, car_make, car_model, model_year, capacity, colour, phone1, phone2, dealers_licence, who, trim, body_style, trim_level, price, milage)
        values
        (:rego_plate, :jurisdiction, :iso_advert_date, :item_number, :publication, :car_make, :car_model, :model_year, :capacity, :colour, :phone1, :phone2, :dealers_licence, :who, :trim, :body_style, :trim_level, :price, :milage )'''

       print sql
       try:
           cursor.execute(sql,
                          {'rego_plate': rego_plate, 'jurisdiction': jurisdiction, 'iso_advert_date': iso_advert_date,
                           'item_number': item_number, 'publication': publication,
                           'car_make': car_make, 'car_model': car_model, 'model_year': model_year, 'capacity': capacity,
                           'colour': colour, 'phone1': phone1, 'phone2': phone2,
                           'dealers_licence': dealers_licence, 'who': who, 'trim': trim, 'body_style': body_style,
                           'trim_level': trim_level, 'price': price, 'milage': milage})
       except:
           print ("failed to add data")
           pass



def main():

    create_table()
    ads = get_adverts()
    add_adverts(ads)





if __name__ == '__main__':
    main()


