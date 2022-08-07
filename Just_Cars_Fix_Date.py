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


#Just_Cars_Number_list = ["JC#1", "JC#11", "JC#12", "JC#13", "JC#78", "JC#34", "JC#115", "JC#133", "JC#154"]
#Just_Cars_Number_list = ["JC#1p8", "JC#11p9", "JC#12p345", "JC#13p43", "JC#78p55", "JC#34p33", "JC#115p11", "JC#133p4", "JC#154p53"]
Just_Cars_Number_list = [ "JC#78p10","JC#79p8","JC#79p17","JC#22p6","JC#58p38""JC#81p9","JC#46p46","JC#41p31",
                          "JC#109p61","JC#109p62","JC#113p64","JC#117p70","JC#117p79","JC#120p46","JC#128p69",
                          "JC#124p4","JC#133p4","JC#133p4","JC#145p98","JC#145p98","JC#148p13","JC#153p139",
                          "JC#153p143","JC#154p17","JC#159p106","JC#61p14","JC#163p104","JC#164p15","JC#165p5",
                          "JC#166p112","JC#166p112","JC#173p89","JC#174p10","JC#174p90",]
actual_month_year = ["3_96", "1_97", "2_97", "3_97", "8_02", "12_98", "9_05", "3_07", "12_08"]

iso_date = "2099-12-31"
for entry in Just_Cars_Number_list:
    iso_date = get_iso_just_cars(entry)
    print entry, iso_date


