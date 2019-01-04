import sqlite3
from Load_Plates_SQL_Test import get_adverts_test




def add_adverts(db_name,ads):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    sql = '''create table adverts ( 
                 master_index integer,
                 rego_plate text,
                 jurisdiction text)'''
    print sql
    try:
        cursor.execute(sql)
    except:
        pass

    master_index1 = 0
    for row in ads:
        print row
        master_index1 += 1
        sql = '''insert into adverts (master_index, rego_plate, jurisdiction) values ({master_index}, "{rego_plate}", "{jurisdiction}")'''

        sql = sql.format(master_index=master_index1, rego_plate=row[0],jurisdiction=row[1])
        print sql
        try:
            cursor.execute(sql)
            print("added")
        except:
            print ("failed to add data")
            pass
    conn.commit()
    conn.close()


def main():

    ads = get_adverts_test()
    add_adverts("advertisements_test.db", ads)


if __name__ == '__main__':
    main()
