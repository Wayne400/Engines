
import sqlite3
import re

def get_iso_just_cars(ad_ref):
    start_year = 1996
    month_offset = 2
    stuff = re.match("JC#(\d*)p(\d*)", ad_ref)
    number_string = stuff.group(1)
    number = int(number_string)
    new_number = number + month_offset
    month = new_number % 12
    if month == 0:
        month = 12
    add_year = new_number // 12
    year = start_year + add_year
    if month < 10:
        iso_date = str(year) + "-0" + str(month) + "-01"
    else:
        iso_date = str(year) + "-" + str(month) + "-01"
    return iso_date

def get_just_cars():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [

("JC#78p10","Matador","1976","Sedan","NSW","RR398","(02)65548396","location","$4,500","colour","VIN","engine#","body no"),
("JC#79p8","Matador","1974","Sedan","VIC","ICJ328","(03)94605130","location","$10,500","colour","VIN","engine#", "body no"),
("JC#79p17","Matador","1976","Sedan","NSW","HAZZ1","(0412)443802","location","$9,300","Dukes of Hazard","VIN","engine#", "body no"),
("JC#22p6","Matador","1972","Sedan","Jurisdiction","PLATE","(071)582751","Bargara","$1","Sky Blue","VIN","engine#","body no"),
("JC#58p38","X-Coupe","1977","Coupe","Jurisdiction","PLATE","(03)98858675","Location","$price","colour","VIN","engine#","C69-067"),
("JC#81p9","Matador","1972","Sedan","WA","8FL718","(08)93833391","Location","$1","Colour","VIN","engine#","body no"),
("JC#46p46","X-Coupe","1977","Coupe","Jurisdiction","PLATE","(07)55432707","QLD","$price","colour","VIN","705POTA61608P", "body no"),
("JC#41p31","Matador","1976","Sedan","Jurisdiction","PLATE","(02)44218111","South Nowra","$price","colour","VIN","engine#", "body no"),
("JC#109p61","Matador","1973","Sedan","Jurisdiction","PLATE","(0)111","Location","$1","colour","VIN","engine#", "S39-025"),
("JC#109p62","Matador","1973","Sedan","Jurisdiction","PLATE","(0)111","Location","$1","colour","VIN","engine#", "S39-077"),
("JC#113p64","Matador","1977","Sedan","VIC","IMF111","(03)98858675","VIC","$1","colour","VIN","engine#", "body no"),
("JC#117p70","Matador","1976","Sedan","NSW","YMS143","(02)48421098","Location","$1","colour","VIN","engine#", "body no"),
("JC#117p79","Matador","1974","Sedan","Jurisdiction","PLATE","(02)62867612","Canberra","$1","colour","VIN","R739439R", "body no"),
("JC#120p46","Matador","1977","Sedan","Jurisdiction","PLATE","(01)11111111","Victoria","$1","colour","VIN","41267PF", "body no"),
("JC#128p69","X-Coupe","1977","Coupe","WA","BKF816","(08)93566125","Western Australia","$1","colour","VIN","engine#", "body no"),
("JC#124p4","Matador","197X","Wagon","Jurisdiction","PLATE","(0)111","Queensland","$1","custom","VIN","engine#", "body no"),
("JC#133p4","Matador","1977","Sedan","Jurisdiction","PLATE","(03)59775507","Victoria","$1","colour","VIN","R74937R", "body no"),
("JC#133p4","Matador","1973","Sedan","Jurisdiction","PLATE","(07)47790435","Queensland","$1","colour","VIN","engine#","body no"),
("JC#145p98","X-Coupe","1977","Coupe","Jurisdiction","BIGRED","(0)111","Location","$1","Red","A4C167PA040","engine#", "C69-040"),
("JC#145p98","Matador","197X","Sedan","Jurisdiction","PLATE","(03)59714616","Victoria","$1","stripes","VIN","engine#", "body no"),
("JC#148p13","Matador","1976","Sedan","Jurisdiction","SI5252","(07)55432707","QLD","$1","Blue","VIN","engine#", "body no"),
("JC#153p139","Matador","1971","Sedan","SA","RTC727","(0431)011759","South Australi","$1","colour","VIN","engine#", "body no"),
("JC#153p143","Matador","197X","Sedan","VIC","CH9497","(03)59714616","Victoria","$1","colour","VIN","engine#", "body no"),
("JC#154p17","Matador","1976","Sedan","QLD","250IYX","(0)111","QLD","$1","colour","VIN","engine#", "body no"),
("JC#159p106","X-Coupe","1977","Coupe","Jurisdiction","PLATE","(02)62887137","Location","$1","Colour","VIN","engine#","C69-030"),
("JC#61p14","X-Coupe","1977","Coupe","Jurisdiction","PLATE","(03)98858675","Victoria","$1","Colour","VIN","engine#","C69-067"),
("JC#163p104","Matador","1976","Sedan","Jurisdiction","PLATE","(0408)322941","VIC","$4000","White Roof","VIN","engine#","S59-157"),
("JC#164p15","Matador","1973","Sedan","QLD","EZY70","(0404)898408","QLD","$35,000","Black Candy Red","VIN","engine#","body no"),
("JC#165p5","Matador","1974","Sedan","Jurisdiction","PLATE","(07)38231483","Rod McCanns","$1","White","VIN","engine#","body no"),
("JC#166p112","Matador","1972","Sedan","Jurisdiction","PLATE","(0402)159101","Ipswich","$5,000","colour","NK15819","engine#","body no"),
("JC#166p112","Matador","1976","Sedan","Jurisdiction","PLATE","(03)52484070","Victoria","$3,000","colour","VIN","A1221PF","body no"),
("JC#173p89","X-Coupe","1977","Sedan","Jurisdiction","PLATE","(0419)160313","NSW","$7,500","colour","VIN","engine#","body no"),
("JC#174p10","X-Coupe","1977","Sedan","VIC","AMC77","(03)94584776","VIC","$14,850","Red Black Sun Roof","VIN","A1230PF","body no"),
("JC#174p90","Matador","1972","Sedan","Jurisdiction","MM806","(0466)632577","NSW","$10,000","Plum","VIN","R729129R","body no"),

      ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 4018
    for column in ads:
        print column
        print column[0], column[11]
        master_index1 += 1


        sql = '''insert into adverts (master_index, rego_plate, jurisdiction, iso_advert_date, item_number, publication,
                 car_make, car_model, model_year, capacity, colour, phone1, phone2, dealers_licence, who, interior_trim,
                  body_style, trim_level, price, milage, month, VIN, Engine_No, Body_No, Location )
                  values
         ({master_index}, "{rego_plate}", "{jurisdiction}", "{iso_advert_date}", {item_number}, "{publication}", 
        "{car_make}", "{car_model}", "{model_year}", "{capacity}", "{colour}", "{phone1}", "{phone2}",
         "{dealers_licence}", "{who}", "{interior_trim}", "{body_style}", "{trim_level}", "{price}", "{milage}", "{month}",
         "{VIN}", "{Engine_No}", "{Body_No}", "{Location}")'''

        sql = sql.format(master_index=master_index1, rego_plate=column[5],
                        jurisdiction=column[4],
                        iso_advert_date=get_iso_just_cars(column[0]),
                        item_number=1, publication="Just Cars",
                        car_make="Rambler", car_model=column[1], model_year=column[2],
                        capacity="360V8",
                        colour=column[9], phone1=column[6], phone2="none",
                        dealers_licence="none", who=column[0], interior_trim="none",
                        body_style=column[3],
                        trim_level="none", price=column[8], milage="none", month="none",
                        VIN=column[10], Engine_No=column[11], Body_No=column[12], Location=column[7])
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

    ads = get_just_cars()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
