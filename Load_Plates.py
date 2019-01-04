def get_adverts_mascot():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
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
        ("GEZ762", "NSW", "1977-01-01", 25, "smh", "Rambler", "Rebel", "none", "none", "unknown", "6672484", "6674460",
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


def get_adverts():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("JKQ458", "NSW", "1978-12-02", 1, "smh", "Rambler", "Rebel", "1970", "360", "unknown", "785122", "none", "LD223", "WW", "none", "none", "none", "none","none"),
        ("BQH878", "NSW", "1978-12-02", 1, "smh", "Rambler", "Hornet","1971","none","unknown","8480451","none","none","WW","none","none","none","none","none"),
        ("GVU672", "NSW", "1978-12-02", 1, "smh", "Rambler", "Hornet","1971","none", "unknown", "4519221", "none", "none", "WW","none","none","none","none","none"),
        ("CTJ846", "NSW", "1974-11-09", 1, "smh", "Rambler", "Ambassador", "none","none","unknown", "842371", "none", "none","WW","none","sedan","none","none","none"),
        ("KMK673", "NSW", "1980-11-05", 1, "smh", "Rambler", "Matador","1973","unknown", "unknown", "862866", "none", "DL 198","WW","none","wagon","none","none","none"),
        ("BKQ184", "NSW", "1974-04-06", 1, "smh", "Rambler", "Hornet", "unknown", "none", "White", "839896","none", "none", "WW","Brown","none","none","none","none"),
        ("GKZ716", "NSW", "1977-07-02", 1, "smh", "Rambler", "Hornet", "1973", "none", "Silver Grey Metallic", "321820","2122539", "none", "WW","chamois","Sedan","none", "$5250","none"),
        ("HPN843", "NSW", "1976-03-13", 1, "smh", "Rambler", "Hornet", "1973", "4.2", "unknown", "6220743", "6228761", "DL 913", "WW","none","none","none","$3590","none"),
        ("DNF054", "NSW", "1979-03-10", 1, "smh", "Rambler", "Hornet", "1971", "258", "none", "9821697","none", "none", "WW","none","none","none","$2900","none")
              ]
    return adverts



def get_adverts2():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("AIG524", "NSW", "1974-10-26", 1, "smh", "Rambler", "Hornet", "1971", "none", "Mustard", "6375781", "none", "none", "WW", "Black", "none", "none", "$3195","none"),
        ("GJO325", "NSW", "1974-10-26", 1, "smh", "Rambler", "Ambassador","1970","360","unknown","775627","none","none","WW","none","none","none","$3000","none"),
        ("GLO068", "NSW", "1974-10-26", 1, "smh", "Rambler", "Hornet","1973","none", "unknown", "9098800", "9296125", "none", "WW","none","none","none","none","11000 mis"),
        ("JBK581", "NSW", "1977-05-14", 1, "smh", "Rambler", "Hornet", "1972","4.2","Peak White", "7476666", "742332", "DL 198","John Muirs Quality Corner","none","sedan","none","none","none"),
        ("OQR664", "NSW", "1988-01-23", 1, "smh", "Rambler", "Hornet","none","unknown", "unknown", "8887982", "none", "none","WW","none","none","none","none","none"),
        ("KSF620", "NSW", "1988-01-23", 1, "smh", "Rambler", "Javelin", "1972", "401", "Red", "9083144","9250893", "none", "WW","Black","none","none","$14500","69,000 mis","none"),
        ("MMM190", "NSW", "1988-01-23", 1, "smh", "Rambler", "Matador", "1976", "none", "none", "3496110","none", "none", "WW","none","Wagon","none", "$5000","86,000 mis"),
        ("JAF743", "NSW", "1977-05-03", 1, "smh", "Rambler", "Hornet", "1975", "none", "unknown", "6672484", "none", "none", "Mascot Motors","none","none","none","none","none"),
        ("HKY299", "NSW", "1978-01-14", 1, "smh", "Rambler", "Hornet", "1973", "none", "none", "7091835","720867", "none", "WW","none","none","none","$4500","none")
              ]
    return adverts

def get_adverts4():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("GRT707", "NSW", "1974-02-23", 1, "smh", "Rambler", "Matador", "1971", "360", "none", "315649", "none", "none", "WW", "none", "sedan", "none", "none","none"),
        ("DKU114", "NSW", "1974-02-23", 1, "smh", "Rambler", "Rebel","1969","none","unknown","8698506","none","none","WW","none","sedan","none","$1875","none"),
        ("EOP187", "NSW", "1974-02-23", 1, "smh", "Rambler", "Rebel","1968","none", "none", "none", "none", "none", "WW","none","wagon","none","none","none"),
        ("DYM011", "NSW", "1977-02-19", 1, "smh", "Rambler", "Classic", "none","V8","none", "5334684", "none", "none","WW","none","sedan","none","$680","none"),
        ("GOC668", "NSW", "1977-02-19", 1, "smh", "Rambler", "Matador","1971","360", "none", "5253804", "none", "none","11/77","none","sedan","none","$2600","none"),
        ("EZW404", "NSW", "1973-03-17", 1, "smh", "Rambler", "Rebel", "1968", "none", "none", "4408137","none", "none", "WW","none","wagon","none","1200","none"),
        ("DLN313", "NSW", "1973-03-17", 1, "smh", "Rambler", "American", "1964", "none", "unknown", "4763291","none", "none", "WW","none","sedan","none","$750","none"),
        ("JBK581", "NSW", "1977-05-21", 1, "smh", "Rambler", "Hornet", "1972", "4.2", "Peak White", "7476666", "742332", "DL 198", "WW","Tan","none","none","none","none"),
        ("EWB131", "NSW", "1977-05-21", 1, "smh", "Rambler", "American", "1969", "none", "none", "6619699","none", "none", "04/78","none","sedan","none","$1100","none")
              ]
    return adverts


def get_adverts3():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("HJQ788", "NSW", "1979-05-30", 1, "smh", "Rambler", "Hornet", "1975", "none", "Bamboo", "3573631", "none", "none", "WW", "White", "sedan", "SST", "$4500","42,000 mis"),
        ("GTL935", "NSW", "1986-12-21", 1, "smh", "Rambler", "Hornet","1973","4.2","unknown","6821399","none","LD 8011","Catchpenny Cars","none","sedan","SST","$2499","none"),
        ("JKZ716", "NSW", "1978-01-28", 1, "smh", "Rambler", "Hornet","1973","4.2", "irridescent grey", "2117263", "32180", "none", "WW","chamois","sedan","SST","$5500","20000 mis"),
        ("CPU410", "NSW", "1976-06-11", 1, "smh", "Rambler", "Hornet", "1970","232","Blue", "893399", "none", "none","WW","sand","sedan","SST","$2400","none"),
        ("GEO119", "NSW", "1978-02-18", 1, "smh", "Rambler", "Hornet","1972","4.2", "Bottle Green", "9224612", "6616797", "none","12/78","White","sedan","SST","$4200","none"),
        ("GMI179", "NSW", "1977-06-04", 1, "smh", "Rambler", "Hornet", "1970", "232", "none", "5193068","none", "none", "10/77","none","sedan","SST","$2500","none"),
        ("XX116", "NSW", "1977-02-26", 1, "smh", "Rambler", "Hornet", "1975", "4.2", "mustard gold", "6651502","none", "none", "WW","none","sedan","SST","$6200","none"),
        ("GZE200", "NSW", "1977-02-26", 1, "smh", "Rambler", "Matador", "1972", "360", "White", "6399659", "none", "none", "WW","bone","none","none","none","none"),
        ("TWI403", "NSW", "1977-02-19", 1, "smh", "Rambler", "Rebel", "none", "none", "none", "7983501","none", "none", "02/78","none","sedan","770","$1300","none")
              ]
    return adverts


def get_adverts5():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("AQP983", "NSW", "1977-05-21", 1, "smh", "Rambler", "Rebel", "1969", "343", "Polar White", "315649", "none", "none", "Ken Allen", "Deep Burgundy", "wagon", "none", "$3998","none"),
        ("AIB118", "NSW", "1977-05-21", 1, "smh", "Rambler", "Hornet","1971","none","unknown","3492378","none","none","1/78","none","sedan","SST","$3000","33000 mis"),
        ("JBX484", "NSW", "1977-05-21", 1, "smh", "Rambler", "Hornet","1971","232", "Black", "426488", "none", "none", "WW","Vinyl Roof","sedan","SST","$3200","none"),
        ("IDG022", "VIC", "1977-05-21", 1, "smh", "Rambler", "Matador", "1974","V8","none", "9602692", "none", "none","WW","none","sedan","none","none","35000 mis"),
        ("GOH959", "NSW", "1978-02-28", 1, "smh", "Rambler", "Hornet","1973","4.2", "White", "852722", "4283186", "none","10/78","none","sedan","SST","$4200","none"),
        ("GLN940", "NSW", "1978-04-08", 1, "smh", "Rambler", "Hornet", "1970", "232", "none", "308154","none", "none", "WW","none","sedan","SST","$1800","none"),
        ("LH096", "NSW", "1977-08-27", 1, "smh", "Rambler", "Hornet", "1971", "none", "Marina Blue", "6362615","none", "none", "WW","white","sedan","SST","$4200","21000 mis"),
        ("EIC103", "NSW", "1977-08-27", 1, "smh", "Rambler", "Renel", "1971", "360", "Paint Fair", "433457", "none", "none", "WW","none","sedan","none","$1500","none"),
        ("AWQ479", "NSW", "1977-08-27", 1, "smh", "Rambler", "Hornet", "1970", "232", "none", "7984144","7500354", "LD 3545", "WW","Vinyl Roof","sedan","SST","$1900","none"),
        ("DIO522", "NSW", "1977-08-27", 1, "smh", "Rambler", "Rebel", "1969", "343", "White", "802004", "none","none", "WW", "Cream", "sedan", "none", "$1500", "none")]
    return adverts


def get_adverts6():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("GAX724", "NSW", "1976-06-12", 1, "smh", "Rambler", "Matador", "1971", "360", "Wild Plum", "5606764", "none", "none", "8/72", "none", "Sedan", "none", "none","none"),
        ("GMY265", "NSW", "1976-06-12", 1, "smh", "Rambler", "Classic","1966","none","unknown","6365059","none","none","WW","none","sedan","770","$650","none"),
        ("DAS702", "NSW", "1976-01-03", 1, "smh", "Rambler", "Classic","1964","none", "unknown", "6236145", "none", "none", "WW","none","sedan","none","$200","none"),
        ("EUZ234", "NSW", "1976-01-03", 1, "smh", "Rambler", "Rebel", "1969","290","unknown", "8312793", "none", "none","WW","none","sedan","none","$1900","none"),
        ("DKY248", "NSW", "1976-01-03", 1, "smh", "Rambler", "American","none","6-cyl", "unknown", "5609590", "none", "none","WW","none","sedan","330","$1290","none"),
        ("BKN784", "NSW", "1974-05-27", 1, "smh", "Rambler", "Hornet", "none", "none", "unknown", "6445433","none", "LD 221", "John Newell Motors","none","sedan","SST","$2990","49000 mis"),
        ("EOE427", "NSW", "1977-08-27", 1, "smh", "Rambler", "Classic", "none", "V8", "unknown", "6246490","none", "none", "WW","none","sedan","none","$720","none"),
        ("AGI601", "NSW", "1980-11-05", 1, "smh", "Rambler", "Ambassador", "none", "360", "unknown", "5871154", "none", "LD 167", "WW","none","sedan","none","$1495","none"),
        ("HGX646", "NSW", "1980-11-05", 1, "smh", "Rambler", "Matador", "1972", "360", "unknown", "6313130","6300339", "11/81", "WW","none","sedan","none","$2225","none"),
        ("KMK673", "NSW", "1980-11-05", 1, "smh", "Rambler", "Matador", "1973", "360", "unknown", "862866", "none","none", "WW", "none", "Wagon", "none", "$1950", "none"),
        ("CTJ846", "NSW", "1974-11-09", 1, "smh", "Rambler", "Ambassador", "unknown", "V8", "unknown", "842371", "none", "none", "WW", "none", "Sedan", "none", "$390", "none"),
        ("GVU672", "NSW", "1978-12-02", 1, "smh", "Rambler", "Hornet", "1971", "none", "unknown", "4519221", "none", "none", "11/79", "none", "sedan", "SST", "$2350", "none"),
        ("BQH878", "NSW", "1978-12-02", 1, "smh", "Rambler", "Hornet", "1971", "none", "unknown", "8480451", "none", "none", "WW", "none", "sedan", "SST", "$2400", "none"),
        ("JKQ458", "NSW", "1978-12-02", 1, "smh", "Rambler", "Rebel", "1970", "360", "785122", "none", "LD 223", "none", "10/79", "none", "sedan", "none", "$2495", "none"),
        ("AEL322", "NSW", "1974-09-21", 1, "smh", "Rambler", "American", "1964", "none", "unknown", "4988137", "none","none", "4/75", "none", "sedan", "440", "$1250", "none"),
        ("GFN135", "NSW", "1974-09-21", 1, "smh", "Rambler", "Hornet", "1973", "4.2", "unknown", "696961", "6985855", "none", "WW", "none", "sedan", "SST", "none", "none"),
        ("PZX062", "NSW", "1974-09-21", 1, "smh", "Rambler", "Hornet", "1972", "none", "unknown", "4985726", "none", "none", "WW", "none", "sedan", "SST", "$3000", "none"),
        ("EVN462", "NSW", "1974-10-19", 1, "smh", "Rambler", "Rebel", "1967", "290", "unknown", "6442161", "none", "none", "WW", "none", "sedan", "none", "$1200", "none"),
        ("DOY285", "NSW", "1974-10-19", 1, "smh", "Rambler", "Classic", "none", "V8", "unknown", "6213170", "none", "none", "WW", "none", "sedan", "none", "$350", "none"),
        ("DQQ812", "NSW", "1974-10-19", 1, "smh", "Rambler", "Classic", "none", "V8", "unknown", "5229424", "none", "none", "WW", "none", "sedan", "660", "$725", "none"),
        ("BJP513", "NSW", "1974-03-16", 1, "smh", "Rambler", "Hornet", "none", "4.2", "White", "6250646", "none", "none", "WW", "Black", "sedan", "SST", "$3750", "21000 mis"),
        ("HUW275", "NSW", "1977-04-30", 1, "smh", "Rambler", "Javelin", "1971", "none", "Brown", "7977311", "none", "LD 204", "Ken Mathews", "Bone", "Coupe", "none", "$6500", "none"),
        ("ELL354", "NSW", "1977-04-30", 1, "smh", "Rambler", "Classic", "none", "V8", "unknown", "881127", "none", "none", "WW", "none", "sedan", "none", "$300", "none"),
        ("DEI087", "NSW", "1977-04-16", 1, "smh", "Rambler", "Hornet", "1971", "none", "white", "956592", "none", "none", "WW", "Tan", "sedan", "SST", "$2850", "none"),
        ("OQG943", "NSW", "1977-04-16", 1, "smh", "Rambler", "Javelin", "1970", "390", "unknown", "5245274", "none", "none", "WW", "none", "Coupe", "none", "$5450", "none")]
    return adverts


def get_adverts7():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("HUR216", "NSW", "1977-04-16", 1, "smh", "Rambler", "Hornet", "1970", "232", "unknown", "592572", "none", "none", "WW", "none", "Sedan", "SST", "$2950","65000 mis"),
        ("HTI448", "NSW", "1977-04-16", 1, "smh", "Rambler", "Matador","1972","360","unknown","471515","none","none","WW","none","sedan","none","$3790","none"),
        ("AUX377", "NSW", "1977-04-16", 1, "smh", "Rambler", "Matador","1971","360", "unknown", "7721689", "none", "none", "WW","none","Wagon","none","$2700","none"),
        ("GPX737", "NSW", "1976-07-10", 1, "smh", "Rambler", "Matador", "1971","360","Brown", "7985048", "none", "LD 159","C G Phillips","Bone Vinyl Roof","Sedan","none","none","none"),
        ("HDK452", "NSW", "1976-07-10", 1, "smh", "Rambler", "Classic","1966","V8", "unknown", "8886574", "none", "none","WW","none","Wagon","770","$600","none"),
        ("OPL922", "NSW", "1976-07-10", 1, "smh", "Rambler", "Classic", "1964", "none", "unknown", "Elanora","none", "none", "WW","none","Wagon","none","$850","none"),
        ("EWX088", "NSW", "1976-07-10", 1, "smh", "Rambler", "Classic", "1965", "none", "unknown", "430231","none", "DL 238", "Rowley Motors","none","sedan","none","$1195","none"),
        ("ENJ542", "NSW", "1976-01-03", 1, "smh", "Rambler", "Classic", "1965", "none", "unknown", "4516150", "none", "none", "WW","none","sedan","none","$700","none"),
        ("AQG186", "NSW", "1976-06-26", 1, "smh", "Rambler", "Rebel", "1971", "none", "unknown", "7597291","none", "none", "WW","none","Wagon","none","none","none"),
        ("AIP825", "NSW", "1976-06-19", 1, "smh", "Rambler", "Rebel", "1967", "none", "unknown", "8375781", "none","DL 961", "1/77", "none", "Sedan", "none", "$995", "none"),
        ("DJK639", "NSW", "1976-06-19", 1, "smh", "Rambler", "Classic", "1966", "V8", "unknown", "Crows Nest", "none", "none", "WW", "none", "Sedan", "none", "none", "none"),
        ("HFJ428", "NSW", "1976-06-19", 1, "smh", "Rambler", "Matador", "1974", "360", "Gold", "766988", "none", "LD 405", "Larke Hoskins", "none", "sedan", "SST", "none", "14000 mis"),
        ("CQC028", "NSW", "1976-07-03", 1, "smh", "Rambler", "Rebel", "1969", "none", "unknown", "6247147", "none", "none", "WW", "none", "Wagon", "none", "none", "none"),
        ("CBR726", "NSW", "1976-03-13", 1, "smh", "Rambler", "Rebel", "6869", "343", "unknown", "7903616", "none", "DL 1111", "Lervan Traders", "none", "sedan", "none", "$2499", "none"),
        ("CJQ827", "NSW", "1976-04-03", 1, "smh", "Rambler", "Hornet", "1971", "none", "unknown", "5207733", "none","LD 982", "WW", "none", "Sedan", "SST", "$2590", "none"),
        ("ELL354", "NSW", "1976-04-03", 1, "smh", "Rambler", "Classic", "1965", "V8", "unknown", "Castle Hill", "none", "none", "WW", "none", "Sedan", "none", "$950", "none"),
        ("GKK291", "NSW", "1976-04-03", 1, "smh", "Rambler", "Rebel", "1970", "360", "Green", "7641152", "none", "DL 937", "WW", "Bone", "Wagon", "SST", "none", "none"),
        ("HKC268", "NSW", "1976-04-03", 1, "smh", "Rambler", "Classic", "1966", "V8", "unknown", "5021915", "none", "DL 03267", "9/76", "none", "Sedan", "660", "$650", "none"),
        ("EVN462", "NSW", "1974-08-03", 1, "smh", "Rambler", "Rebel", "1967", "290", "unknown", "6442161", "none", "none", "WW", "none", "Sedan", "none", "$1450", "none"),
        ("ESB485", "NSW", "1974-08-03", 1, "smh", "Rambler", "Rebel", "1967", "290", "unknown", "3718897", "none", "none", "WW", "Black", "Sedan", "none", "$2000", "none"),
        ("GJY267", "NSW", "1974-08-03", 1, "smh", "Rambler", "Classic", "none", "none", "unknown", "3286188", "none", "none", "5/75", "none", "Sedan", "770", "$900", "none"),
        ("DKN342", "NSW", "1974-08-03", 1, "smh", "Rambler", "Classic", "none", "V8", "White Blue", "9493580", "none", "none", "WW", "none", "Sedan", "660", "$890", "54000 mis"),
        ("EQW159", "NSW", "1974-11-02", 1, "smh", "Rambler", "Classic", "none", "V8", "unknown", "6371268", "none", "none", "WW", "none", "Sedan", "660", "none", "none"),
        ("JAG060", "NSW", "1977-02-09", 1, "smh", "Rambler", "Matador", "1973", "none", "unknown", "7591672", "none", "none", "WW", "none", "Sedan", "none", "none", "none"),
        ("AGE819", "NSW", "1977-02-09", 1, "smh", "Rambler", "Rebel", "1969", "343", "unknown", "554752", "none", "none", "WW", "none", "Sedan", "none", "$1200", "none")]
    return adverts



def get_adverts_dummy():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("CAA000", "NSW", "1960-01-01", 1, "smh", "Rambler","Ambassador","1960","dummy","dummy","dummy", "none", "none", "WW", "none", "Sedan", "SST", "$2950","65000 mis"),
        ("CLL000", "NSW", "1961-01-01", 1, "smh", "Rambler","Ambassador","1961","dummy","dummy","dummy","none","none","WW","none","sedan","none","$3790","none"),
        ("CTA000", "NSW", "1962-01-01", 1, "smh", "Rambler","Ambassador","1962","dummy","dummy","dummy", "none", "none", "WW","none","Wagon","none","$2700","none"),
        ("DAA000", "NSW", "1963-01-01", 1, "smh", "Rambler","Ambassador","1963","dummy","dummy","dummy", "none", "LD 159","C G Phillips","Bone Vinyl Roof","Sedan","none","none","none"),
        ("DKA000", "NSW", "1964-01-01", 1, "smh", "Rambler","Classic","1964","dummy","dummy","dummy","dummy", "none","WW","none","Wagon","770","$600","none"),
        ("DOJ000", "NSW", "1965-01-01", 1, "smh", "Rambler","Classic","1965","dummy","dummy","dummy","dummy", "none", "WW","none","Wagon","none","$850","none"),
        ("EDA000", "NSW", "1966-01-01", 1, "smh", "Rambler","Classic","1966","dummy","dummy","dummy","dummy", "DL 238", "Rowley Motors","none","sedan","none","$1195","none"),
        ("EMA000", "NSW", "1967-01-01", 1, "smh", "Rambler","Rebel","1967","dummy","dummy","dummy","dummy","none", "WW","none","sedan","none","$700","none"),
        ("AAA000", "NSW", "1968-01-01", 1, "smh", "Rambler","Rebel","1968","dummy","dummy","dummy","dummy","none", "WW","none","Wagon","none","none","none"),
        ("BAJ000", "NSW", "1969-01-01", 1, "smh", "Rambler","Rebel","1969","dummy","dummy","dummy","dummy","DL 961", "1/77", "none", "Sedan", "none", "$995", "none"),
        ("AIA000", "NSW", "1970-01-01", 1, "smh", "Rambler","Hornet","1970","dummy","dummy","dummy","dummy", "none", "WW", "none", "Sedan", "none", "none", "none"),
        ("CWI000", "NSW", "1971-01-01", 1, "smh", "Rambler","Hornet","1971","dummy","dummy","dummy","dummy", "LD 405", "Larke Hoskins", "none", "sedan", "SST", "none", "14000 mis"),
        ("DXI000", "NSW", "1972-01-01", 1, "smh", "Rambler","Hornet","1972","dummy","dummy","dummy","dummy", "none", "WW", "none", "Wagon", "none", "none", "none"),
        ("GEA000", "NSW", "1973-01-01", 1, "smh", "Rambler","Hornet","1973","dummy","dummy","dummy","dummy", "DL 1111", "Lervan Traders", "none", "sedan", "none", "$2499", "none"),
        ("GQA000", "NSW", "1974-01-01", 1, "smh", "Rambler","Hornet","1974","dummy","dummy","dummy","dummy","LD 982", "WW", "none", "Sedan", "SST", "$2590", "none"),
        ("HEA000", "NSW", "1975-01-01", 1, "smh", "Rambler","Hornet","1975","dummy","dummy","dummy","dummy", "none", "WW", "none", "Sedan", "none", "$950", "none"),
        ("HQA000", "NSW", "1976-01-01", 1, "smh", "Rambler","Matador","1976","dummy","dummy","dummy","dummy", "DL 937", "WW", "Bone", "Wagon", "SST", "none", "none"),
        ("JCA050", "NSW", "1977-01-01", 1, "smh", "Rambler","Matador","1977","dummy","dummy","dummy","dummy", "DL 03267", "9/76", "none", "Sedan", "660", "$650", "none"),
        ("JPE050", "NSW", "1978-01-01", 1, "smh", "Rambler","Matador","1978","dummy","dummy","dummy","dummy", "none", "WW", "none", "Sedan", "none", "$1450", "none"),
        ("KBH050", "NSW", "1979-01-01", 1, "smh", "Rambler","Replate","1979","dummy","dummy","dummy","dummy", "none", "WW", "Black", "Sedan", "none", "$2000", "none"),
        ("FOA000", "NSW", "1980-01-01", 1, "smh", "Rambler","Replate","1980","dummy","dummy","dummy","dummy", "none", "5/75", "none", "Sedan", "770", "$900", "none"),
        ("LCZ050", "NSW", "1981-01-01", 1, "smh", "Rambler","Replate","1981","dummy","dummy","dummy","dummy", "none", "WW", "none", "Sedan", "660", "$890", "54000 mis"),
        ("LOS050", "NSW", "1982-01-01", 1, "smh", "Rambler","Replate","1982","dummy","dummy","dummy","dummy", "none", "WW", "none", "Sedan", "660", "none", "none"),
        ("MBE050", "NSW", "1983-01-01", 1, "smh", "Rambler","Replate","1983","dummy","dummy","dummy","dummy", "none", "WW", "none", "Sedan", "none", "none", "none"),
        ("MOZ050", "NSW", "1984-01-01", 1, "smh", "Rambler","Replate","1984","dummy","dummy","dummy","dummy", "none", "WW", "none", "Sedan", "none", "$1200", "none")]
    return adverts


def get_adverts8():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("GXX834", "NSW", "1974-07-01", 1, "WW", "Rambler", "Hornet","1973","4.2","White", "43650791", "none", "none", "H39237", "Bone", "none", "none", "$1000","none"),
        ("GAI674", "NSW", "2000-05-01", 1, "JCr", "Rambler", "Hornet","1972","4.2","Light Colour","44465615","none","none","8/72","none","none","none","$3850","none"),
        ("EHI555", "NSW", "1972-03-28", 1, "Grn", "Rambler", "Matador","1972","360","Safety Wattle","Grenville","none", "none", "WW","Clay","none","none","$6490","none"),
        ("EBQ444", "NSW", "1972-04-27", 1, "Grn", "Rambler", "Matador","1972","360","Mocca Brown","Grenville","none", "none","WW","Clay","sedan","none","$6570","none"),
        ("BKN433", "NSW", "1970-09-17", 1, "Grn", "Rambler", "Rebel","1970","360","White", "Grenville", "none","none","WW","Black","none","none","$4600","none"),
        ("BAI530", "NSW", "1971-03-11", 1, "Grn", "Rambler", "Rebel","1971","360","Safety Wattle","Grenville","none", "none", "WW","Black","none","none","$4700","none"),
        ("CHI292", "NSW", "1971-07-19", 1, "Grn", "Rambler", "Rebel","1971","360","Deep Russet","Grenville","none","none", "WW","Beige","Sedan","none", "$4800","none"),
        ("CIZ375", "NSW", "1971-10-12", 1, "Grn", "Rambler", "Hornet","1971","4.2","Sienna Brown","Grenville", "none", "none", "WW","Clay","none","none","$3450","none"),
        ("DQM977", "NSW", "1972-03-01", 1, "Grn", "Rambler", "Hornet","1971","4.2","White","Grenville","none", "none", "WW","Clay","none","none","$4250","none")
              ]
    return adverts

def get_adverts9():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("EEU770", "NSW", "1974-11-02", 1, "smh", "Rambler","American","1967","440","5877586","none", "none", "none", "WW", "none", "Sedan", "440", "$890","none"),
        ("DVM340", "NSW", "1972-08-30", 1, "smh", "Rambler","Classic","1966","V8","Green","5994143","none","none","WW","none","sedan","none","$1195","none"),
        ("DQM014", "NSW", "1974-02-02", 1, "smh", "Rambler","Hornet","1972","4.2","Orange","3492157","none", "none", "WW","Black","Sedan","SST","none","none"),
        ("DKU114", "NSW", "1974-02-02", 1, "smh", "Rambler","Rebel","1969","none","unknown","8698506","none", "none","WW","none","Sedan","none","$1875","none"),
        ("DCA333", "NSW", "1974-02-02", 1, "smh", "Rambler","Classic","June","V8","none","8718514","none", "none","6/74","none","Sedan","none","$450","none"),
        ("DWC273", "NSW", "1974-02-02", 1, "smh", "Rambler","Classic","1965","V8","none","5258526","none", "none", "10/74","none","Sedan","none","none","none"),
        ("ALL380", "NSW", "1974-02-02", 1, "smh", "Rambler","Classic","1965","V8","Black","6077124","none", "none", "5/74","none","Sedan","660","$900","none"),
        ("AJU524", "NSW", "1974-02-02", 1, "smh", "Rambler","Rebel","1968","none","unknown","5253804","none","none", "4/74","none","Sedan","none","$875","none"),
        ("DSZ109", "NSW", "1974-02-02", 1, "smh", "Rambler","Classic","1965","V8","Clean Car","5255560","none","none", "WW","none","Sedan","none","$580","none"),
        ("GII759", "NSW", "1974-02-02", 1, "smh", "Rambler","American","1968","6-cyl","unknown","7594218","none","none", "WW", "none", "Sedan", "none", "$995", "none"),
        ("HHX067", "NSW", "1977-02-12", 1, "smh", "Rambler","American","1966","6-cyl","unknown","5464563","none", "none", "WW", "none", "Sedan", "330", "$550", "none"),
        ("JAF669", "NSW", "1977-02-12", 1, "smh", "Rambler","Matador","1973","360","unknown","7591672","none", "LD ", "WW", "none", "Sedan", "none", "$4450", "none"),
        ("AQJ145", "NSW", "1977-02-12", 1, "smh", "Rambler","Ambassador","1971","360","Gold","none","none", "LD 284", "Jeff Fripp", "none", "Sedan", "none", "$3795", "none"),
        ("GOC668", "NSW", "1977-02-12", 1, "smh", "Rambler","Matador","1971","360","White","5253804","none", "none", "11/77", "Bone", "sedan", "none", "$2950", "none"),
        ("EIQ105", "NSW", "1977-02-12", 1, "smh", "Rambler","Rebel","1968","290","unknown","7983501","none","none", "6/77", "none", "Sedan", "none", "$1000", "none"),
        ("JAG060", "NSW", "1973-01-06", 1, "smh", "Rambler","Matador","1972","360","White","5217222","none","DL 770", "WW", "none", "Sedan", "none", "$5590", "none"),
        ("BGA021", "NSW", "1973-01-06", 1, "smh", "Rambler","Classic","1967","V8","unknown","892623","none", "none", "WW", "none", "Sedan", "770", "$1150", "none"),
        ("BUQ277", "NSW", "1973-01-06", 1, "smh", "Rambler","Rebel","1970","none","Black","6076120","none", "none", "WW", "none", "Sedan", "none", "$2200", "none"),
        ("ADK690", "NSW", "1973-06-09", 1, "smh", "Rambler","American","1968","6-cyl","unknown","4983648","none", "none", "WW", "none", "Sedan", "none", "$1200", "none"),
        ("EXZ498", "NSW", "1973-06-09", 1, "smh", "Rambler","Rebel","1969","360","White","7722963","6043584", "none", "WW", "Bone", "Sedan", "none", "$2290", "none"),
        ("EOM611", "NSW", "1973-06-09", 1, "smh", "Rambler","Rebel","none","unknown","7596403","none","none", "none", "WW", "none", "Wagon", "none", "none", "none"),]
    return adverts

def get_adverts_10():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("BGT732", "NSW", "1970-07-01", 1, "Wheels", "Rambler","Hornet","1970","232","Havana Gold","43650791", "none","none","WW","none","Sedan","none","none","none"),
        ("LVW876", "NSW", "2006-08-01", 1, "smh", "Rambler","Hornet","1973","258","Big Bad Orange","43650791","none","none","WW","none","Sedan","SST","$2400","none"),
        ("DRB746", "NSW", "1975-02-08", 1, "smh", "Rambler","American","1966","none","unknown","Belmore","manual","none","WW","none","Sedan","330","none","none"),
        ("DPI586", "NSW", "1975-02-08", 1, "smh", "Rambler","Rebel","7071","360","White","6271528","none","none","WW","Red","Sedan","none","none","none"),
        ("AUS494", "NSW", "1975-02-08", 1, "smh", "Rambler","Rebel","1968","290","unknown","7993881","none","none","WW","none","Sedan","none","$1500","none"),
        ("EAQ138", "NSW", "1975-02-08", 1, "smh", "Rambler","Rebel","1968","V8","unknown","5208300","none","none","WW","none","Sedan","none","$1590","none"),
        ("HDD457", "NSW", "1975-05-31", 1, "smh", "Rambler","Rebel","1970","none","unknown","Cammeray","6674460","none","WW","none","Sedan","none","$1750","none"),
        ("CIZ602", "NSW", "1975-05-31", 1, "smh", "Rambler","Rebel","1971","360","unknown","482741","434221","none", "WW","none","Sedan","none","none","none"),
        ("HHM576", "NSW", "1975-05-31", 1, "smh", "Rambler","Classic","none","none","Dark Green","6022341","none","none","WW","none","Sedan","660","$895","none"),
        ("ATO313", "NSW", "1975-05-31", 1, "smh", "Rambler","Rebel","1968","none","unknown","7599327","none","none","WW","none","Sedan","none","$950","none"),
        ("EMJ798", "NSW", "1975-08-16", 1, "smh", "Rambler","Classic","1966","V8","Blue","7476666","742332", "John Muir","WW","Blue","Sedan","none","$1590","none"),
        ("EIE904", "NSW", "1975-08-16", 1, "smh", "Rambler","Matador","1972","360","White","574796","none","none","WW","none","Wagon","none","$5200","none"),
        ("BDQ404", "NSW", "1975-08-16", 1, "smh", "Rambler","Rebel","1971","360","Blue","6484311","6484311","John A Gilbert","WW","Beige","Sedan","none","none","none")]
    return adverts

def get_adverts_11():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("AQA558", "NSW", "1975-08-20", 1, "smh", "Rambler","Rebel","1971","360","none","6615229", "none","none","WW","none","Wagon","none","$2950","none"),
        ("BAG111", "NSW", "1975-09-06", 1, "smh", "Rambler","Classic","1965","V8","none","5879997","none","none","WW","none","Sedan","none","none","none"),
        ("BKF816", "NSW", "1975-09-06", 1, "smh", "Rambler","Rebel","1968","none","unknown","305636","none","none","WW","none","Sedan","none","$1450","none"),
        ("GDE457", "NSW", "1975-09-10", 1, "smh", "Rambler","Rebel","none","360","none","6674460","none","Mascot Motors","WW","none","Sedan","none","$2950","none"),
        ("EZP114", "NSW", "1975-09-27", 1, "smh", "Rambler","Rebel","1969","V8","unknown","5871154","none","LD 167","WW","none","Sedan","none","$1895","none"),
        ("BFK916", "NSW", "1975-09-27", 1, "smh", "Rambler","Rebel","1968","V8","unknown","305636","none","none","WW","none","Sedan","none","$1100","none"),
        ("GKP329", "NSW", "1975-10-25", 1, "smh", "Rambler","Classic","1966","V8","unknown","813305","none","DL 2297","WW","none","Sedan","none","$790","none"),
        ("BJD072", "NSW", "1975-11-08", 1, "smh", "Rambler","Hornet","none","none","unknown","880249","House Of David","none", "WW","none","Sedan","none","$2899","none"),
        ("AQG106", "NSW", "1975-11-08", 1, "smh", "Rambler","Javelin","none","304","Daytona Green","7476666","742332","John Muir","WW","none","Sedan","SST","$5599","none"),
        ("GTR620", "NSW", "1975-11-08", 1, "smh", "Rambler","Matador","1972","360","Ivory","430702","Caldwell","none","WW","Brown","Sedan","none","$4690","30000 mis"),
        ("HCJ355", "NSW", "1975-12-06", 1, "smh", "Rambler","Hornet","1972","258","none","7597291","none", "none","WW","none","Sedan","none","none","32000 mis"),
        ("AIZ538", "NSW", "1975-12-08", 1, "smh", "Rambler","Hornet","none", "none","none","6674460","none","Mascot Motors","WW","none","Sedan","none","$2250","none"),
        ("HJW816", "NSW", "1975-12-06", 1, "smh", "Rambler","Classic","1966","none","none","6321165","none","none","WW","none","Sedan","770","$495","none"),
        ("GZB961", "NSW", "1975-12-06", 1, "smh", "Rambler","Rebel","1968","none","Blue","3262958","none","none","WW","none","Sedan","none","$1800","none")]
    return adverts

def get_adverts_12():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("HMP370", "NSW", "1989-06-11", 1, "smh", "Rambler","Hornet","1975","232","White","7504838", "none","none","10/89","none","Sedan","none","$7600","none"),
        ("CZQ813", "NSW", "1989-06-11", 1, "smh", "Rambler","Hornet","1971","none","unknown","(046)557742","none","none","WW","none","Sedan","none","$4000","none"),
        ("AUS494", "NSW", "1975-02-22", 1, "smh", "Rambler","Rebel","1968","none","unknown","7993881","none","none","WW","none","Sedan","none","$1500","none"),
        ("CIZ602", "NSW", "1975-05-17", 1, "smh", "Rambler","Rebel","1971","360","none","482741","434221","none","WW","none","Sedan","none","none","none"),
        ("EWB896", "NSW", "1975-05-24", 1, "smh", "Rambler","American","1968","none","unknown","890345","none","none","WW","none","Sedan","none","$850","none"),
        ("DXQ159", "NSW", "1975-05-24", 1, "smh", "Rambler","Classic","1965","none","unknown","6654261","none","none","WW","none","Sedan","none","$800","none"),
        ("EWV135", "NSW", "1975-05-24", 1, "smh", "Rambler","Classic","none","V8","unknown","6079749","none","none","5/76","none","Sedan","660","$900","none"),
        ("HHM376", "NSW", "1975-05-24", 1, "smh", "Rambler","Classic","none","V8","none","6022341","none","none","WW","none","Sedan","none","$970","none"),
        ("HVJ565", "NSW", "1975-05-24", 1, "smh", "Rambler","Classic","none","none","none","821391","none", "none","WW","none","Wagon","660","$450","none"),
        ("AQD866", "NSW", "1975-05-24", 1, "smh", "Rambler","Classic","V8", "none","none","4516035","none","none","WW","none","Sedan","660","$450","none"),
        ("EVO870", "NSW", "1975-05-24", 1, "smh", "Rambler","Rebel","1967","none","none","5249001","none","none","WW","none","Sedan","none","$1900","34000 mis"),
        ("HDD457", "NSW", "1975-05-24", 1, "smh", "Rambler","Rebel","1971","none","none","8961616","none","none","WW","none","Sedan","none","$1800","none")]
    return adverts

def get_adverts_13():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("HJL208", "NSW", "1975-08-02", 1, "smh","Rambler","American","none","none","unknown","(046)571147","none","none","WW","none","Sedan","none","$550","none"),
        ("GPC367", "NSW", "1975-08-02", 1, "smh","Rambler","Hornet","1973","4.2","unknown","9494396","none","none","WW","none","Sedan","none","none","none"),
        ("GIK111", "NSW", "1975-08-02", 1, "smh", "Rambler","Matador","1973","360","Willow","6488033","none","Capital Motors","4/76","Bone","Sedan","none","$4550","20000 mis"),
        ("AXV965", "NSW", "1975-08-02", 1, "smh", "Rambler","Rebel","1970","343","Yellow","5609506","none","none","2/76","Black","sedan","none","$2000","38000 mis"),
        ("AIP825", "NSW", "1975-08-02", 1, "smh", "Rambler","Rebel","none","V8","unknown","Newtown","none","none","WW","none","Sedan","none","$1400","none"),
        ("HKP509", "NSW", "1975-08-02", 1, "smh", "Rambler","Rebel","7071","360","unknown","8717400","none","none","WW","none","none","none","$2500","none"),
        ("HHZ217", "NSW", "1980-01-05", 1, "smh", "Rambler","Rebel","1968","none","none","6373068","none","none","WW","none","Sedan","none", "none","none"),
        ("HIK642", "NSW", "1980-01-05", 1, "smh", "Rambler","Hornet","none","none","none","598405","none","none","7/80","none","Sedan","none","$2200","none"),
        ("HPR775", "NSW", "1980-01-05", 1, "smh", "Rambler","Hornet","1975","4.2","White","760202","none","Cullen's LD 394","12/80","Burgundy","Sedan","none","$3995","none"),
        ("GGM425", "NSW", "1980-01-05", 1, "smh", "Rambler","Rebel","none","V8","unknown","5871154","none","BA Andrews LD167","WW","none","Sedan","none","$995","none"),
        ("CFQ152", "NSW", "1980-02-23", 1, "smh", "Rambler","Hornet","none","none","unknown","9812182","non","none","WW","none","Sedan","none","$2950","none"),
        ("JFS808", "NSW", "1980-02-23", 1, "smh", "Rambler","Matador","1977","360","unknown","6672484","none","Mascot Motors LD 1091","WW","none","Sedan","none","$3950","none"),
        ("DQD576", "NSW", "1980-02-23", 1, "smh", "Rambler","Rebel","1971","360","unknown","4498166","none","none","WW","none","Sedan","none","none","none"),
        ("EVC996", "NSW", "1980-06-14", 1, "smh", "Rambler","American","none","none","Steel Grey","7089993","none","Apex Motors LD 1184","5/81","none","Sedan","none","$2495","none"),
        ("HNH802", "NSW", "1980-06-14", 1, "smh", "Rambler","Hornet","1975","4.2","Blue","6375024","none","Ken Allen LD 301","WW","White","Sedan","none","$4995","none"),
        ("HRY380", "NSW", "1980-06-14", 1, "smh", "Rambler","Hornet","1975","4.2","Red Pepper","7278877","none","Ken Sale Motors LD 513","WW","Black","Sedan","none","$3995","none"),
        ("KOQ320", "NSW", "1980-06-14", 1, "smh", "Rambler","Matador","1976","360","unknown","812281","none","Thomas DL 5150","WW","none","Wagon","none","$6750","none"),
        ("GRN680", "NSW", "1980-06-14", 1, "smh", "Rambler","Matador","1973","360","Silver Grey","7287486","none","none","10/80","Black","Sedan","none","$2900","none"),
        ("JCG870", "NSW", "1980-06-14", 1, "smh", "Rambler","Matador","none","360","none","767184","none","none","WW","none","Sedan","none","$2750","45000 mis")]
    return adverts

def get_adverts_14():   # creating a list of tuples representing individual ads in the newspapers , item_number is > 1 if multiple cars listed
    adverts = [
        ("LGQ313", "NSW", "1984-01-07", 1, "smh","Rambler","Hornet","1971","none","unknown","(065)722149","none","none","WW","none","Sedan","none","$3600","none"),
        ("576ONR", "QLD", "1984-01-10", 1, "smh","Rambler","Hornet","1973","none","unknown","811843","none","none","WW","none","Sedan","none","$2500","none"),
        ("GZS719", "NSW", "1984-03-03", 1, "smh", "Rambler","Hornet","1973","none","unknown","auction","none","Sydney Motor Auctions","WW","none","Sedan","none","none","none"),
        ("HJQ788", "NSW", "1984-03-03", 1, "smh", "Rambler","Hornet","1976","4.2","Mustard","6672484","none","Mascot Motors","WW","none","sedan","none","$3990","none"),
        ("HWV950", "NSW", "1984-03-10", 1, "smh", "Rambler","Hornet","1975","4.2","Light Green","5255734","none","none","WW","none","Sedan","none","$3300","none"),
        ("BLV689", "NSW", "1984-04-07", 1, "smh", "Rambler","Hornet","1971","none","unknown","auction","none","none","WW","none","Sedan","none","none","none"),
        ("HKG342", "NSW", "1984-04-07", 1, "smh", "Rambler","Hornet","1975","4.2","unknown","9397619","none","none","WW","none","Sedan","none","$3300","100000 kms"),
        ("GIL814", "NSW", "1984-04-21", 1, "smh", "Rambler","Hornet","1973","4.2","unknown","auction","none","Motor Market","none","none","Sedan","none","none","none"),
        ("JGG307", "NSW", "1984-05-19", 1, "smh", "Rambler","Hornet","1970","232","unknown","9825347","none","none","WW","none","Sedan","none","$2000","70000 mis"),
        ("LKY854", "NSW", "1984-05-19", 1, "smh", "Rambler","Hornet","1972","4.2","unknown","auction","none","LD 7003","WW","none","Sedan","none","none","none"),
        ("EYI951", "NSW", "1984-07-20", 1, "smh", "Rambler","Hornet","1970","232","unknown","6424320","non","none","07/85","none","Sedan","none","$3350","none"),
        ("MON199", "NSW", "1984-07-21", 1, "smh", "Rambler","Javelin","1972","401","unknown","9383642","none","none","WW","none","Coupe","none","$12000","none"),
        ("EJM162", "NSW", "1984-07-21", 1, "smh", "Rambler","Hornet","1971","none","unknown","422682","none","none","WW","none","Sedan","none","$2200","none"),
        ("HHG443", "NSW", "1984-07-21", 1, "smh", "Rambler","Hornet","1975","4.2","unknown","6549247","none","none","07/85","none","Sedan","none","$3500","none"),
        ("LKW566", "NSW", "1984-09-01", 1, "smh", "Rambler","Hornet","1971","none","unknown","5294695","none","none","WW","none","Sedan","none","$2500","none"),
        ("CJQ827", "NSW", "1984-09-01", 1, "smh", "Rambler","Hornet","1971","V8","unknown","5191573","(047)354138","none","WW","none","Sedan","none","$2500","none"),
        ("GVY410", "NSW", "1984-09-01", 1, "smh", "Rambler","none","none","none","unknown","3574373","none","none","WW","none","Sedan","none","$1200","none"),
        ("HOG287", "NSW", "1984-09-07", 1, "smh", "Rambler","Hornet","none","4.2","unknown","5871154","none","DL 167", "WW","none","Sedan","SST","$2495","none"),
        ("EIZ192", "NSW", "1984-09-22", 1, "smh", "Rambler","Hornet","7273","4.2","unknown","942780","none","none","WW", "none","Sedan","SST","$2950","none"),
        ("LGL800", "NSW", "1984-10-20", 1, "smh", "Rambler","Matador","1976","360","unknown","6982706","3375943","none","WW","none","Wagon","none","none","none"),
        ("EYI951", "NSW", "1984-10-20", 1, "smh", "Rambler","Hornet","1970","232","unknown", "6424320","none","none","WW","none","Sedan","none","$2750","none"),
        ("HDP966", "NSW", "1984-11-10", 1, "smh", "Rambler","Classic","none", "none","unknown","none","none","LD 139","WW","none","Sedan","none","$1490","none"),
        ("CQM414", "NSW", "1984-11-17", 1, "smh", "Rambler","Hornet","1971","4.2","Mocca","5217090","none","none","9/85", "none","Sedan","none","$2950","none"),
        ("BSQ001", "NSW", "1984-11-10", 1, "smh", "Rambler","Rebel", "7071","360","unknown","9699925","none","none","WW", "none","Wagon","SST","$3000","none"),
        ("LKW566", "NSW", "1984-11-24", 1, "smh", "Rambler","Hornet","1971","none","unknown","5294695","none","none","WW","none","Sedan","none","$2250","none"),
        ("JWE823", "NSW", "1984-12-22", 1, "smh", "Rambler","Hornet","none","none","none","5200617","none","none","10/85","none","Sedan","none","$1500","none")]
    return adverts
