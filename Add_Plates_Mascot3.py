import sqlite3
from Load_Plates import get_adverts_mascot


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



def add_adverts(cursor, ads):

    for row in ads:
  #     print row
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

    conn = open_database('advertisements_mascot2.db')
    cursor = conn.cursor()

    create_table(cursor)
   # create_table()
    ads = get_adverts_mascot()
    add_adverts(cursor, ads)





if __name__ == '__main__':
    main()


