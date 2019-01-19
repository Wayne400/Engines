
def get_month(target_plate):
    nsw_plate_search = {

'1967-01-01': ("EGF030", "none", "none", "none", "none"),
'1967-02-01': ("none", "none", "none", "none", "none"),
'1967-03-01': ("EJP504", "none", "none", "none", "none"),
'1967-04-01': ("none", "none", "none", "none", "none"),
'1967-05-01': ("none", "none", "none", "none", "none"),
'1967-06-01': ("none", "none", "none", "none", "none"),
'1967-07-01': ("none", "none", "none", "none", "none"),
'1967-08-01': ("none", "none", "none", "none", "none"),
'1967-09-01': ("ESX827", "none", "none", "none", "none"),
'1967-10-01': ("none", "none", "none", "none", "none"),
'1967-11-01': ("none", "none", "none", "none", "none"),
'1967-12-01': ("none", "none", "none", "none", "none"),

'1968-01-01': ("none", "none", "none", "none", "none"),
'1968-02-01': ("none", "none", "none", "none", "none"),
'1968-03-01': ("none", "none", "none", "none", "none"),
'1968-04-01': ("EVP414", "none", "none", "none", "none"),
'1968-05-01': ("none", "none", "none", "none", "none"),
'1968-06-01': ("none", "none", "none", "none", "none"),
'1968-07-01': ("EYZ800", "none", "none", "none", "none"),
'1968-08-01': ("none", "none", "none", "none", "none"),
'1968-09-01': ("ABF456", "EPX812", "none", "none", "none"),
'1968-10-01': ("none", "none", "none", "none", "none"),
'1968-11-01': ("none", "none", "none", "none", "none"),
'1968-12-01': ("none", "none", "none", "none", "none"),


'1969-01-01': ("none", "none", "none", "none", "none"),
'1969-02-01': ("AHD734", "none", "none", "none", "none"),
'1969-03-01': ("none", "none", "none", "none", "none"),
'1969-04-01': ("ADB424", "AKZ729", "AKF338", "AKA218", "none"),
'1969-05-01': ("AMR774", "AMP362", "AMP693", "none", "none"),
'1969-06-01': ("none", "none", "none", "none", "none"),
'1969-07-01': ("AOB424", "APE697", "none", "none", "none"),
'1969-08-01': ("AOO695", "none", "none", "none", "none"),
'1969-09-01': ("APT629", "none", "none", "none", "none"),
'1969-10-01': ("AUW774", "AUF935", "none", "none", "none"),
'1969-11-01': ("ATJ608", "AVS177", "none", "none", "none"),
'1969-12-01': ("AWM635", "none", "none", "none", "none"),


'1970-01-01': ("AXK202", "none", "none", "none", "none"),
'1970-02-01': ("AZE614", "none", "none", "none", "none"),
'1970-03-01': ("AYJ331", "AYJ230", "AYJ219", "none", "none"),
'1970-04-01': ("BCL015", "none", "none", "none", "none"),
'1970-05-01': ("BCY554", "none", "none", "none", "none"),
'1970-06-01': ("none", "none", "none", "none", "none"),
'1970-07-01': ("BGT739", "BGP323", "BGJ842", "BFP142", "none"),
'1970-08-01': ("BJD879", "none", "none", "none", "none"),
'1970-09-01': ("none", "none", "none", "none", "none"),
'1970-10-01': ("BME521", "BLN404", "BLV006", "BMZ218", "BLN403"),
'1970-11-01': ("ACQ643", "none", "none", "none", "none"),
'1970-12-01': ("ABQ154", "BMK203", "AMQ153", "none", "none"),

'1971-01-01': ("AVQ692", "AIL658", "AWI069", "AIL145", "none"),
'1971-02-01': ("none", "none", "none", "none", "none"),
'1971-03-01': ("BAI631", "BAI218", "none", "none", "none"),
'1971-04-01': ("BBQ466", "BDQ153", "BGI676", "none", "none"),
'1971-05-01': ("BMQ458", "BKQ309", "none", "none", "none"),
'1971-06-01': ("none", "none", "none", "none", "none"),
'1971-07-01': ("BQV847", "BQV249", "none", "none", "none"),
'1971-08-01': ("CFQ813", "CUQ354", "none", "none", "none"),
'1971-09-01': ("CIK740", "none", "none", "none", "none"),
'1971-10-01': ("CQB172", "none", "none", "none", "none"),
'1971-11-01': ("DAI235", "none", "none", "none", "none"),
'1971-12-01': ("none", "none", "none", "none", "none"),


'1972-01-01': ("none", "none", "none", "none", "none"),
'1972-02-01': ("DIW815", "DQD646", "DIW774", "DIZ151", "DOQ699"),
'1972-03-01': ("DQX493", "DQX896", "none", "none", "none"),
'1972-04-01': ("none", "none", "none", "none", "none"),
'1972-05-01': ("EBQ908", "ENQ771", "ENQ503", "none", "none"),
'1972-06-01': ("EIA945", "none", "none", "none", "none"),
'1972-07-01': ("EQZ589", "EIE430", "none", "none", "none"),
'1972-08-01': ("GAA280", "EIY761", "GAX474", "GAX601", "none"),
'1972-09-01': ("GBA418", "GBS966", "none", "none", "none"),
'1972-10-01': ("GBB809", "GCH970", "none", "none", "none"),
'1972-11-01': ("GDW436", "none", "none", "none", "none"),
'1972-12-01': ("GDK650", "GDP317", "none", "none", "none"),


'1973-01-01': ("none", "none", "none", "none", "none"),
'1973-02-01': ("GFF896", "GGM292", "GFR340", "none", "none"),
'1973-03-01': ("GHD856", "GGR191", "GHN644", "GHD520", "none"),
'1973-04-01': ("GHU453", "GHT996", "GIX301", "none", "none"),
'1973-05-01': ("GJO186", "GJU823", "none", "none", "none"),
'1973-06-01': ("GKH196", "GKV554", "GIZ636", "none", "none"),
'1973-07-01': ("GKI211", "GLO643", "GLO466", "GLO467", "none"),
'1973-08-01': ("GMV932", "none", "none", "none", "none"),
'1973-09-01': ("none", "none", "none", "none", "none"),
'1973-10-01': ("none", "none", "none", "none", "none"),
'1973-11-01': ("GOS442", "none", "none", "none", "none"),
'1973-12-01': ("none", "none", "none", "none", "none"),

'1974-01-01': ("GRL801", "none", "none", "none", "none"),
'1974-02-01': ("GSX278", "GUE307", "none", "none", "none"),
'1974-03-01': ("GTX069", "GTO283", "GUE017", "none", "none"),
'1974-04-01': ("none", "none", "none", "none", "none"),
'1974-05-01': ("GVK199", "none", "none", "none", "none"),
'1974-06-01': ("none", "none", "none", "none", "none"),
'1974-07-01': ("GYE144", "none", "none", "none", "none"),
'1974-08-01': ("GZY893", "none", "none", "none", "none"),
'1974-09-01': ("HAV241", "HAV053", "none", "none", "none"),
'1974-10-01': ("HBI236", "none", "none", "none", "none"),
'1974-11-01': ("HBB697", "none", "none", "none", "none"),
'1974-12-01': ("HDD459", "HCN997", "HDU867", "HDV023", "none"),


'1975-01-01': ("HEJ203", "HDP842", "none", "none", "none"),
'1975-02-01': ("HEP228", "HFJ719", "none", "none", "none"),
'1975-03-01': ("HGB886", "none", "none", "none", "none"),
'1975-04-01': ("HHZ147", "HHB542", "HGZ530", "none", "none"),
'1975-05-01': ("HIW894", "HIW478", "none", "none", "none"),
'1975-06-01': ("none", "none", "none", "none", "none"),
'1975-07-01': ("HKW029", "none", "none", "none", "none"),
'1975-08-01': ("none", "none", "none", "none", "none"),
'1975-09-01': ("none", "none", "none", "none", "none"),
'1975-10-01': ("none", "none", "none", "none", "none"),
'1975-11-01': ("none", "none", "none", "none", "none"),
'1975-12-01': ("none", "none", "none", "none", "none"),



}
    found_month = "none"
    for key in sorted(nsw_plate_search):
       month = nsw_plate_search[key]
       for plate in month:
           if plate[0:3] == target_plate[0:3]:
               found_month = key
               break


    return found_month[0:7]





def main():

    nsw_plate_search = get_month("HXX979")
    print nsw_plate_search





if __name__ == '__main__':
    main()


