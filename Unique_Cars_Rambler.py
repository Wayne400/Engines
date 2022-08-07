
import sqlite3
import re



def get_iso_unique_cars(ad_ref):
    start_year = 1996
    month_offset = 2
    stuff = re.match("(\d\d)\/(\d*)p(\d*)", ad_ref)
    month = stuff.group(1)
    year = stuff.group(2)
    page_no = int(stuff.group(3))
    if len(year) == 2:
        iso_date = "19" + year + "-" + month  + "-01"
    elif len(year) == 4:
        iso_date = year + "-" + month  + "-01"


    return iso_date, page_no



def get_unique_cars():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [

("11/87p132","X-Coupe","1977","Coupe","SA","SSF466","(087)250533","Mt Gambier","$9,990","Vermillion Fire","VIN","engine#","body no"),
("12/87p25","X-Coupe","1977","Coupe","Jurisdiction","NOPLATE","(07)2633173","QLD","$1","Bright Red","VIN","engine#","body no"),
("02/85p49","X-Coupe","1977","Coupe","Jurisdiction","NOPLATE","(03)5921991","New Brighton Motors","$8,999","Colour","VIN","engine#","body no"),
("08/85p17","X-Coupe","1977","Coupe","Jurisdiction","NOPLATE","(07)8081705","QLD","$7,850","Alley Cat Decal","VIN","engine#","body no"),
("05/86p7","X-Coupe","1977","Coupe","QLD","674PIF","(075)551692","QLD","$12,000","Red","VIN","engine#","body no"),
("05/88p145","X-Coupe","1977","Coupe","QLD","674PIF","(075)551692","QLD","$9,500","Guard Red","VIN","engine#","body no"),
("09/88p65","X-Coupe","1977","Coupe","QLD","NOPLATE","(07)2072072","QLD","$12,500","Red/Black Trim","VIN","engine#","body no"),
("10/91p20","Matador","1974","Sedan","NSW","HGY204","(02)443231","Turramurra","$8,000","Yellow","VIN","engine#","body no"),
("01/92p12","Matador","1974","Sedan","NSW","HGY204","(02)443231","Turramurra","$1","Yellow","VIN","engine#","body no"),
("02/89p225","Matador","1973","Sedan","VIC","NOPLATE","(03)7201439","Victoria","$9,000","Yellow","VIN","engine#","body no"),
("04/89p9","X-Coupe","1977","Coupe","NSW","NOPLATE","(02)3997621","NSW","$10,800","Bronze","VIN","engine#","body no"),
("05/89p48","Matador","1972","Sedan","NSW","NOPLATE","(064)956261","NSW","$3,500","Colour","VIN","engine#","body no"),
("05/89p71","Matador","1973","Sedan","VIC","NOPLATE","(03)7201439","VIC","$7,000","Colour","VIN","engine#","body no"),
("05/89p284","Matador","1976","Sedan","SA","UDR675","(08)2233780","SA","$9,450","Colour","VIN","engine#","body no"),
("10/89p37","X-Coupe","1977","Coupe","QLD","NOPLATE","(07)2072072","QLD","$10,000","Brilliant Red","VIN","engine#","body no"),
("05/88p96","Matador","1976","Wagon","QLD","NOPLATE","(075)431405","QLD","$1","Colour","VIN","engine#","body no"),
("12/89p201","Matador","1971","Sedan","NSW","CQU140","(02)5229884","NSW","$4,300","Colour","VIN","engine#","body no"),
("01/90p75","Matador","1976","Sedan","NSW","NOPLATE","(046)284888","NSW","$9,250","LPG Red Trim","VIN","engine#","body no"),
("02/90p46","Matador","1976","Sedan","VIC","NOPLATE","(053)315868","VIC","$8,500","White/Burgundy Trim","VIN","engine#","body no"),
("10/90p66","X-Coupe","1977","Coupe","QLD","NOPLATE","(07)8911411","QLD","$15,000","Red/Black Trim","VIN","engine#","body no"),
("01/91p68","X-Coupe","1977","Coupe","QLD","NOPLATE","(07)8911411","QLD","$15,000","Red/Black Trim","VIN","engine#","body no"),
("01/91p84","Matador","1976","Wagon","VIC","ILG161","(03)6876111","Footscray","$7,000","Colour","VIN","engine#","body no"),
("04/91p98","Matador","1974","Wagon","QLD","085ANV","(071)525910","Bundaburg","$7,500","ex-hearse","VIN","engine#","body no"),
("05/91p12","X-Coupe","1977","Coupe","NSW","OP101","(02)3446644","NSW","$12,000","White","VIN","engine#","body no"),
("06/91p78","Matador","1976","Sedan","NSW","RIS543","(068)926175","Tullamore","$11,500","Bullbar","VIN","engine#","body no"),
("06/91p188","Matador","1972","Sedan","VIC","LSE288","(03)3635766","Dealer","$5,500","Colour","VIN","engine#","body no"),
("08/91p62","Matador","1976","Sedan","VIC","INR309","(060)241285","Wandonga","$4,500","Maroon/Vinyl Top","VIN","engine#","body no"),
("08/91p78","Matador","1976","Sedan","QLD","192NLQ","(075)302271","Mudgeeraba","$10,000","Golden Yellow","VIN","engine#","body no"),
("08/91p113","X-Coupe","1977","Coupe","ACT","YTC890","(06)2576291","ACT","$15,500","Dragways","VIN","engine#","body no"),
("09/91p83","Matador","1976","Sedan","NSW","RMQ276","(049)613435","Newcastle","$7,500","Colour","VIN","engine#","body no"),
("12/91p25","X-Coupe","1977","Coupe","QLD","860AON","(07)8471061","QLD","$8,500","Red/Black Trim 12 Slots","VIN","engine#","body no"),
("03/92p33","Matador","1976","Sedan","VIC","INR309","(060)241385","Wandonga","$1","Maroon Vinyl Top","VIN","engine#","body no"),
("03/92p167","Matador","1974","Wagon","NSW","NOPLATE","(063)514453","Lithgow","$1","Colour","VIN","engine#","body no"),
("09/92p236","X-Coupe","1977","Coupe","QLD","860AON","(07)8471061","QLD","$1","Red","VIN","engine#","body no"),
("01/93p97","X-Coupe","1977","Coupe","SA","SHP173","(08)3470799","SA","$7,500","Red","VIN","engine#","body no"),
("02/93p248","X-Coupe","1977","Coupe","SA","SHP173","(08)3470799","SA","$7,500","Red","VIN","engine#","body no"),
("03/98p76","Matador","1976","Sedan","NSW","JDK949","(02)95678658","Location","$16,500","Red/White Vinyl","VIN","engine#","body no"),
("02/98p299","Matador","1971","Sedan","ACT","YYV738","(06)2382973","Location","$2,800","Colour","VIN","engine#","body no"),
("11/98p319","Matador","1976","Sedan","NSW","SUZ867","(02)62363219","Location","$1","Colour","VIN","engine#","body no"),
("04/98p184","Matador","1976","Sedan","NSW","MMF682","(02)44216794","Nowra","$10,000","White/Brown Trim","VIN","engine#","body no"),
("05/98p185","Matador","1971","Sedan","NSW","NOPLATE","(02)4515367","Location","$1","Colour","VIN","engine#","body no"),
("07/95p50","Matador","1976","Sedan","VIC","RL463","(054)532097","Strathallen","$2,500","Olive","VIN","engine#","body no"),
("07/95p136","Matador","1973","Sedan","NSW","THQ666","(069)771880","Location","$2,950","Colour","VIN","engine#","body no"),
("03/96p66","X-Coupe","1977","Coupe","NSW","MMK941","(060)369534","Albury","$8,750","Green","VIN","engine#","body no"),
("11/92p999","X-Coupe","1977","Coupe","SA","SCM768","(08)3823982","SA","$10,000","Bronze or Red","VIN","engine#","body no"),
("09/93p8","Matador","1976","Sedan","NSW","ABE14V","(02)5228716","Location","$6,500","Blue/White Vinyl Top","VIN","engine#","body no"),
("09/93p227","Matador","1972","Sedan","QLD","443ONR","(070)962301","Atherton","$1,600","Colour","VIN","engine#","body no"),
("10/93p23","Matador","1971","Sedan","NSW","PWP133","(066)723041","Coffs Harbour","$5,500","White","VIN","engine#","body no"),
("10/93p127","Matador","1976","Sedan","NSW","SFO889","(02)8434772","NSW","$2,700","Colour","VIN","engine#","body no"),
("10/93p142","Matador","1973","Sedan","VIC","LWF777","(03)3504436","VIC","$6,900","Colour","VIN","engine#","body no"),
("12/93p151","Matador","1975","Sedan","NSW","REM787","(043)432389","Gosford","$1","Colour","VIN","engine#","body no"),



      ]

    return adverts



def add_adverts(cursor, ads):

    master_index1 = 4054
    for column in ads:
        print column
        print column[0], column[11]
        master_index1 += 1
        iso_advert_date, item_number = get_iso_unique_cars(column[0])

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
                        iso_advert_date=iso_advert_date,
                        item_number=item_number, publication="Unique Cars",
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

    ads = get_unique_cars()
    add_adverts(cursor, ads)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    main()
