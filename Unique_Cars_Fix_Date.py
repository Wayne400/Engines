import re

def get_iso_unique_cars(ad_ref):
    start_year = 1996
    month_offset = 2
    stuff = re.match("(\d\d)\/(\d*)p(\d*)", ad_ref)
    month = stuff.group(1)
    year = stuff.group(2)
    page_no = stuff.group(3)
    if len(year) == 2:
        iso_date = "19" + year + "-" + month  + "-01"
    elif len(year) == 4:
        iso_date = year + "-" + month  + "-01"


    return iso_date, page_no


#Just_Cars_Number_list = ["JC#1", "JC#11", "JC#12", "JC#13", "JC#78", "JC#34", "JC#115", "JC#133", "JC#154"]
Unique_Cars_Number_list = ["02/2000p156", "10/87p112", "11/87p97", "02/85p49", "08/85p17", "05/86p7", "05/88p145", "09/88p65", "11/88p72", "01/92p12", "01/2006p1"]
actual_month_year = ["3_96", "1_97", "2_97", "3_97", "8_02", "12_98", "9_05", "3_07", "12_08"]

iso_date = "2099-12-31"
for entry in Unique_Cars_Number_list:
    iso_date, page_no = get_iso_unique_cars(entry)
    print entry, iso_date, page_no


