
import sqlite3


def get_engines():

    engines = {'L4004H' : ("209'G'11", "H09-015", "unknown", "KR"),
'L4115H' : ("212'G'01", "H09-135", "unknown", "MWh"),
'L4116H' : ("212'G'08", "L4116H", "unknown", "MWh"),
'L4183H' : ("302'G'05", "H09-190", "3190808", "BP"),
'L4184H' : ("302'G'05", "H09-202", "3190808", "AR"),
'L4254H' : ("302'G'03", "H09-272", "unknown" , "GOC"),
'L4285H' : ("302'G'09", "H09-294", "unknown", "RS"),
'L4412H' : ("304'G'02", "L4412H", "3190808", "WW"),
'L4501H' : ("304'G'02", "L4501H", "3190808", "MD"),
'L4512H' : ("304'G'07", "L4512H", "3190808", "WW"),
'L4556H' : ("304'G'07", "H09-554", "3190808", "DM"),
'L4557H' : ("304'G'07", "H09-562", "3190808", "WS"),
'L4589H' : ("303'G'30", "L4589H", "3190808", "WW"),
'L4603H' : ("305'G'18", "H09-611", "unknown", "CG"),
'L4610H' : ("303'G'30", "L4610H", "unknown", "CM"),
'L4666H' : ("305'G'26", "L4666H", "unknown", "EBAY"),
'L4709H' : ("306'G'01", "H09-701", "unknown", "CC"),
'K4979H' : ("402'A'25", "K4979H", "unknown", "Tony"),
'K4986H' : ("402'A'24", "H19-141", "3199962", "WS"),
'K5086H' : ("402'A'24", "H19-224", "3199962", "BMp"),
'K5172H' : ("404'A'29", "H29-289", "3199962", "DG"),
'K5193H' : ("405'A'14", "H29-312", "unknown", "GF"),
'K5202H' : ("405'A'13", "K5202H", "unknown", "Danny"),
'K5305H' : ("406'A'01", "H29-436", "3199962", "RM"),
'K5321H' : ("404'A'27", "H29-519", "3199962", "CT"),
'K5474H' : ("412'A'10", "AK13174", "3213867", "GP"),
'K5503H' : ("412'A'08", "K5503H", "unknown", "SG"),
'K5524H' : ("501'A'31", "H39-085", "3213867", "MWh"),
'K5529H' : ("501'A'31", "H39-086", "unknown", "RM"),
'K5551H' : ("502'A'01", "H39-090", "unknown", "MWh"),
'K5601H' : ("502'A'01", "H39-159", "unknown", "TJ"),
'K5619H' : ("503'A'20", "H39-175", "3213867", "JC"),
'K5640H' : ("503'A'20", "H39-217", "3213867", "WW"),
'K5660H' : ("412'A'10", "H39-237", "3213867", "SW"),
'K5664H' : ("501'A'31", "H39-197", "3213867", "AR"),
'K5670H' : ("501'A'31", "H39-227", "unknown", "RT"),
'A036H' : ("708'A'05", "H59-044", "unknown", "DN"),
'A040H' : ("707'A'30", "H59-040", "unknown", "BB"),
'A081H' : ("704'A'25", "H59-087", "unknown", "MP"),
'A095H' : ("704'A'24", "H59-095", "unknown", "CM"),
'A109H' : ("704'A'23", "H59-103", "unknown", "KS"),
'A099H' : ("704'A'25", "H59-115", "unknown", "SF"),
'A123H' : ("704'A'13", "H59-127", "unknown", "AJ"),
'A129H' : ("704'A'23" , "H59-129", "3218618", "SW"),
'A138H' : ("608'A'20" , "H59-140", "unknown", "AJ"),
}
    return engines


def open_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(cursor):
    sql = '''create table engine_table (
                 serial text,
                 amc_code text,
                 body_no text,
                 casting_no text,
                 contact text)
           '''
    try:
        cursor.execute(sql)
    except:
        pass


def add_engines(cursor, engine_nos):

    for key in engine_nos:
        engine_data = engine_nos[key]  # this is an array or tuple
        # 'L4183H': ("302'G'05", "H09-190", "3190808", "BP")
        sql = '''insert into engine_table (serial, amc_code, body_no, casting_no, contact)
                  values
         ( "{serial}", "{amc_code}", "{body_no}", "{casting_no}", "{contact}")'''

        sql = sql.format( serial=key,
                        amc_code=engine_data[0],
                        body_no=engine_data[1],
                        casting_no=engine_data[2], contact=engine_data[3])
        print sql
        try:
            cursor.execute(sql)
        except:
            print ("failed to add data")
            pass

def get_sql_data_all(cursor, connectstring):
    #  print kwargs

    sql = "select * from engine_table"

    print sql
    try:
        results = cursor.execute(sql)
        ads = results.fetchall()
        return ads

    except:
        print "I am unable to connect to the database"




def main():

    engine_nos = get_engines()
    conn = open_database('engines_hornet.db')
    cursor = conn.cursor()
    create_table(cursor)
    engine_table = get_sql_data_all(cursor, connectstring="engines_hornet.db")
    for engine_record in engine_table:
        print engine_record
    add_engines(cursor, engine_nos)
    conn.commit()
    conn.close()




if __name__ == '__main__':
    main()


