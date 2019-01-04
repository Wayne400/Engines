import sqlite3


def open_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(cursor):
    sql = '''create table hornets (
                 body text,
                 date text,
                 vin text,
                 colour text,
                 engine_date text,
                 engine_serial text,
                 rego text,
                 state text,
                 who text)
           '''
    try:
         cursor.execute(sql)
    except:
         pass

def add_hornets(cursor):
    names = ['body','date', 'vin', 'colour', 'engine_date', 'engine_serial', 'rego','state','who']
    values = ['H09-136', '7-70', 'GK14972', 'Red', '212G01', 'L4115H', 'Full', 'VIC', 'RP']
    car = dict(zip(names, values))
    body = car['body']
    date = car['date']
    vin = car['vin']
    colour = car['colour']
    engine_date = car['engine_date']
    engine_serial = car['engine_serial']
    rego = car['rego']
    state = car['state']
    who = car['who']
    print "wally2\n"
    sql = '''insert into hornets
        (body, date, vin, colour, engine_date, engine_serial, rego, state, who)
        values
        (:body, :date, :vin, :colour, :engine_date, :engine_serial, :rego, :state, :who)'''
        
    cursor.execute(sql,{'body':body, 'date':date, 'vin':vin, 'colour':colour, 'engine_date':engine_date, 'engine_serial':engine_serial, 'rego':rego, 'state':state, 'who':who })
    print "Added!" 

def main():
    conn = open_database('hornet_register.db')
    cursor = conn.cursor()
    create_table(cursor)
    add_hornets(cursor)
    print 'wally\n'
    conn.commit()
    conn.close()
	
if __name__ == '__main__':
	main()
	

