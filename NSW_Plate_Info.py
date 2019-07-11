
def get_month(target_plate):
    nsw_plate_search = {


'1960-01-01': ("none", "none", "none", "none", "none"),
'1960-02-01': ("none", "none", "none", "none", "none"),
'1960-03-01': ("none", "none", "none", "none", "none"),
'1960-04-01': ("none", "none", "none", "none", "none"),
'1960-05-01': ("none", "none", "none", "none", "none"),
'1960-06-01': ("none", "none", "none", "none", "none"),
'1960-07-01': ("none", "none", "none", "none", "none"),
'1960-08-01': ("none", "none", "none", "none", "none"),
'1960-09-01': ("none", "none", "none", "none", "none"),
'1960-10-01': ("none", "none", "none", "none", "none"),
'1960-11-01': ("none", "none", "none", "none", "none"),
'1960-12-01': ("none", "none", "none", "none", "none"),


'1961-01-01': ("none", "none", "none", "none", "none"),
'1961-02-01': ("none", "none", "none", "none", "none"),
'1961-03-01': ("none", "none", "none", "none", "none"),
'1961-04-01': ("none", "none", "none", "none", "none"),
'1961-05-01': ("none", "none", "none", "none", "none"),
'1961-06-01': ("none", "none", "none", "none", "none"),
'1961-07-01': ("none", "none", "none", "none", "none"),
'1961-08-01': ("none", "none", "none", "none", "none"),
'1961-09-01': ("CLZ341", "none", "none", "none", "none"),
'1961-10-01': ("none", "none", "none", "none", "none"),
'1961-11-01': ("none", "none", "none", "none", "none"),
'1961-12-01': ("none", "none", "none", "none", "none"),


'1962-01-01': ("none", "none", "none", "none", "none"),
'1962-02-01': ("none", "none", "none", "none", "none"),
'1962-03-01': ("CPN098", "none", "none", "none", "none"),
'1962-04-01': ("none", "none", "none", "none", "none"),
'1962-05-01': ("none", "none", "none", "none", "none"),
'1962-06-01': ("none", "none", "none", "none", "none"),
'1962-07-01': ("none", "none", "none", "none", "none"),
'1962-08-01': ("none", "none", "none", "none", "none"),
'1962-09-01': ("none", "none", "none", "none", "none"),
'1962-10-01': ("none", "none", "none", "none", "none"),
'1962-11-01': ("none", "none", "none", "none", "none"),
'1962-12-01': ("none", "none", "none", "none", "none"),


'1963-01-01': ("none", "none", "none", "none", "none"),
'1963-02-01': ("none", "none", "none", "none", "none"),
'1963-03-01': ("none", "none", "none", "none", "none"),
'1963-04-01': ("none", "none", "none", "none", "none"),
'1963-05-01': ("none", "none", "none", "none", "none"),
'1963-06-01': ("none", "none", "none", "none", "none"),
'1963-07-01': ("none", "none", "none", "none", "none"),
'1963-08-01': ("none", "none", "none", "none", "none"),
'1963-09-01': ("DCH830", "none", "none", "none", "none"),
'1963-10-01': ("none", "none", "none", "none", "none"),
'1963-11-01': ("DEE332", "none", "none", "none", "none"),
'1963-12-01': ("none", "none", "none", "none", "none"),

'1964-01-01': ("none", "none", "none", "none", "none"),
'1964-02-01': ("none", "none", "none", "none", "none"),
'1964-03-01': ("none", "none", "none", "none", "none"),
'1964-04-01': ("DHC311", "none", "none", "none", "none"),
'1964-05-01': ("none", "none", "none", "none", "none"),
'1964-06-01': ("none", "none", "none", "none", "none"),
'1964-07-01': ("none", "none", "none", "none", "none"),
'1964-08-01': ("none", "none", "none", "none", "none"),
'1964-09-01': ("none", "none", "none", "none", "none"),
'1964-10-01': ("DMW530", "none", "none", "none", "none"),
'1964-11-01': ("none", "none", "none", "none", "none"),
'1964-12-01': ("none", "none", "none", "none", "none"),

'1965-01-01': ("none", "none", "none", "none", "none"),
'1965-02-01': ("none", "none", "none", "none", "none"),
'1965-03-01': ("none", "none", "none", "none", "none"),
'1965-04-01': ("none", "none", "none", "none", "none"),
'1965-05-01': ("DUH479", "none", "none", "none", "none"),
'1965-06-01': ("none", "none", "none", "none", "none"),
'1965-07-01': ("DKL903", "none", "none", "none", "none"),
'1965-08-01': ("none", "none", "none", "none", "none"),
'1965-09-01': ("DVW268", "none", "none", "none", "none"),
'1965-10-01': ("none", "none", "none", "none", "none"),
'1965-11-01': ("none", "none", "none", "none", "none"),
'1965-12-01': ("none", "none", "none", "none", "none"),

'1966-01-01': ("none", "none", "none", "none", "none"),
'1966-02-01': ("EAZ456", "none", "none", "none", "none"),
'1966-03-01': ("EAW645", "none", "none", "none", "none"),
'1966-04-01': ("none", "none", "none", "none", "none"),
'1966-05-01': ("none", "none", "none", "none", "none"),
'1966-06-01': ("none", "none", "none", "none", "none"),
'1966-07-01': ("EDY017", "none", "none", "none", "none"),
'1966-08-01': ("none", "none", "none", "none", "none"),
'1966-09-01': ("EFT685", "none", "none", "none", "none"),
'1966-10-01': ("EGB560", "none", "none", "none", "none"),
'1966-11-01': ("EGA878", "none", "none", "none", "none"),
'1966-12-01': ("none", "none", "none", "none", "none"),

'1967-01-01': ("EGF030", "none", "none", "none", "none"),
'1967-02-01': ("EKF265", "none", "none", "none", "none"),
'1967-03-01': ("EJP504", "EKN463", "none", "none", "none"),
'1967-04-01': ("none", "none", "none", "none", "none"),
'1967-05-01': ("EMJ265", "none", "none", "none", "none"),
'1967-06-01': ("none", "none", "none", "none", "none"),
'1967-07-01': ("none", "none", "none", "none", "none"),
'1967-08-01': ("none", "none", "none", "none", "none"),
'1967-09-01': ("ESX827", "EPX812", "none", "none", "none"),
'1967-10-01': ("none", "none", "none", "none", "none"),
'1967-11-01': ("none", "none", "none", "none", "none"),
'1967-12-01': ("none", "none", "none", "none", "none"),


'1968-01-01': ("EUH083", "none", "none", "none", "none"),
'1968-02-01': ("EUM835", "EUO022", "EUB862", "none", "none"),
'1968-03-01': ("EUY146", "EVF770", "EUY884", "none", "none"),
'1968-04-01': ("EVP414", "none", "none", "none", "none"),
'1968-05-01': ("EXN005", "EXF134", "none", "none", "none"),
'1968-06-01': ("none", "none", "none", "none", "none"),
'1968-07-01': ("EYZ800", "none", "none", "none", "none"),
'1968-08-01': ("none", "none", "none", "none", "none"),
'1968-09-01': ("ABF456", "ABM514", "none", "none", "none"),
'1968-10-01': ("ACF930", "none", "none", "none", "none"),
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
'1969-12-01': ("AWM635", "AXF942", "none", "none", "none"),


'1970-01-01': ("AXK202", "none", "none", "none", "none"),
'1970-02-01': ("AZE614", "none", "none", "none", "none"),
'1970-03-01': ("AYJ331", "AYJ230", "AYJ219", "none", "none"),
'1970-04-01': ("BCL015", "BBU632", "none", "none", "none"),
'1970-05-01': ("BCY554", "none", "none", "none", "none"),
'1970-06-01': ("BDL507", "none", "none", "none", "none"),
'1970-07-01': ("BGT739", "BGP323", "BGJ842", "BFP142", "BFT325"),
'1970-08-01': ("BJD879", "none", "none", "none", "none"),
'1970-09-01': ("BLA532", "none", "none", "none", "none"),
'1970-10-01': ("BME521", "BLN404", "BLV006", "BMZ218", "BLN403"),
'1970-11-01': ("ACQ643", "none", "none", "none", "none"),
'1970-12-01': ("ABQ154", "BMK203", "AMQ153", "none", "none"),

'1971-01-01': ("AVQ692", "AIL658", "AWI069", "AIL145", "none"),
'1971-02-01': ("none", "none", "none", "none", "none"),
'1971-03-01': ("BAI631", "BAI218", "none", "none", "none"),
'1971-04-01': ("BBQ466", "BDQ153", "BGI676", "none", "none"),
'1971-05-01': ("BMQ458", "BKQ309", "none", "none", "none"),
'1971-06-01': ("none", "none", "none", "none", "none"),
'1971-07-01': ("BQV847", "BQV249", "BQV586", "none", "none"),
'1971-08-01': ("CFQ813", "CUQ354", "none", "none", "none"),
'1971-09-01': ("CIK740", "none", "none", "none", "none"),
'1971-10-01': ("CQB172", "none", "none", "none", "none"),
'1971-11-01': ("DAI235", "none", "none", "none", "none"),
'1971-12-01': ("DBQ714", "CQO004", "none", "none", "none"),


'1972-01-01': ("none", "none", "none", "none", "none"),
'1972-02-01': ("DIW815", "DQD646", "DIW774", "DIZ151", "DOQ699","DQM462"),
'1972-03-01': ("DQX493", "DQX896", "none", "none", "none"),
'1972-04-01': ("DQK176", "none", "none", "none", "none"),
'1972-05-01': ("EBQ908", "ENQ771", "ENQ503", "none", "none"),
'1972-06-01': ("EIA945", "none", "none", "none", "none"),
'1972-07-01': ("EQZ589", "EIE430", "none", "none", "none"),
'1972-08-01': ("GAA280", "EIY761", "GAX474", "GAX601", "none"),
'1972-09-01': ("GBA418", "GBS966", "GBF483", "none", "none"),
'1972-10-01': ("GBB809", "GCH970", "none", "none", "none"),
'1972-11-01': ("GDW436", "none", "none", "none", "none"),
'1972-12-01': ("GDK650", "GDP317", "none", "none", "none"),


'1973-01-01': ("none", "none", "none", "none", "none"),
'1973-02-01': ("GFF896", "GGM292", "GFR340", "none", "none"),
'1973-03-01': ("GHD856", "GGR191", "GHN644", "GHD520", "GHO608"),
'1973-04-01': ("GHU453", "GHT996", "GIX301", "none", "none"),
'1973-05-01': ("GJO186", "GJU823", "GJC670", "none", "none"),
'1973-06-01': ("GKH196", "GKV554", "GIZ636", "none", "none"),
'1973-07-01': ("GKI211", "GLO643", "GLO466", "GLO467", "GLH214"),
'1973-08-01': ("GMV932", "GMG114", "none", "none", "none"),
'1973-09-01': ("none", "none", "none", "none", "none"),
'1973-10-01': ("GNS270", "GNF450", "none", "none", "none"),
'1973-11-01': ("GOS442", "GPX980", "none", "none", "none"),
'1973-12-01': ("GQY252", "none", "none", "none", "none"),

'1974-01-01': ("GRL801", "none", "none", "none", "none"),
'1974-02-01': ("GSX278", "GUE307", "none", "none", "none"),
'1974-03-01': ("GTX069", "GTO283", "GUE017", "none", "none"),
'1974-04-01': ("GTD847", "none", "none", "none", "none"),
'1974-05-01': ("GVK199", "none", "none", "none", "none"),
'1974-06-01': ("GUD399", "none", "none", "none", "none"),
'1974-07-01': ("GYE144", "GXX834", "none", "none", "none"),
'1974-08-01': ("GZY893", "GYF534", "none", "none", "none"),
'1974-09-01': ("HAV241", "HAV053", "none", "none", "none"),
'1974-10-01': ("HBI236", "HAN286", "none", "none", "none"),
'1974-11-01': ("HBB697", "none", "none", "none", "none"),
'1974-12-01': ("HDD459", "HCN997", "HDU867", "HDV023", "none"),


'1975-01-01': ("HEJ203", "HDP842", "none", "none", "none"),
'1975-02-01': ("HEP228", "HFJ719", "none", "none", "none"),
'1975-03-01': ("HGB886", "none", "none", "none", "none"),
'1975-04-01': ("HHZ147", "HHB542", "HGZ530", "none", "none"),
'1975-05-01': ("HIW894", "HIW478", "HIM553", "none", "none"),
'1975-06-01': ("none", "none", "none", "none", "none"),
'1975-07-01': ("HKW029", "none", "none", "none", "none"),
'1975-08-01': ("HLI854", "none", "none", "none", "none"),
'1975-09-01': ("none", "none", "none", "none", "none"),
'1975-10-01': ("none", "none", "none", "none", "none"),
'1975-11-01': ("HNW698", "none", "none", "none", "none"),
'1975-12-01': ("none", "none", "none", "none", "none"),


'1976-01-01': ("none", "none", "none", "none", "none"),
'1976-02-01': ("none", "none", "none", "none", "none"),
'1976-03-01': ("none", "none", "none", "none", "none"),
'1976-04-01': ("none", "none", "none", "none", "none"),
'1976-05-01': ("none", "none", "none", "none", "none"),
'1976-06-01': ("none", "none", "none", "none", "none"),
'1976-07-01': ("none", "none", "none", "none", "none"),
'1976-08-01': ("none", "none", "none", "none", "none"),
'1976-09-01': ("none", "none", "none", "none", "none"),
'1976-10-01': ("none", "none", "none", "none", "none"),
'1976-11-01': ("none", "none", "none", "none", "none"),
'1976-12-01': ("JSL325", "none", "none", "none", "none"),


'1977-01-01': ("none", "none", "none", "none", "none"),
'1977-02-01': ("none", "none", "none", "none", "none"),
'1977-03-01': ("JCF700", "none", "none", "none", "none"),
'1977-04-01': ("none", "none", "none", "none", "none"),
'1977-05-01': ("none", "none", "none", "none", "none"),
'1977-06-01': ("none", "none", "none", "none", "none"),
'1977-07-01': ("none", "none", "none", "none", "none"),
'1977-08-01': ("none", "none", "none", "none", "none"),
'1977-09-01': ("none", "none", "none", "none", "none"),
'1977-10-01': ("none", "none", "none", "none", "none"),
'1977-11-01': ("none", "none", "none", "none", "none"),
'1977-12-01': ("none", "none", "none", "none", "none"),


'1978-01-01': ("none", "none", "none", "none", "none"),
'1978-02-01': ("none", "none", "none", "none", "none"),
'1978-03-01': ("JCF700", "none", "none", "none", "none"),
'1978-04-01': ("none", "none", "none", "none", "none"),
'1978-05-01': ("none", "none", "none", "none", "none"),
'1978-06-01': ("none", "none", "none", "none", "none"),
'1978-07-01': ("none", "none", "none", "none", "none"),
'1978-08-01': ("none", "none", "none", "none", "none"),
'1978-09-01': ("none", "none", "none", "none", "none"),
'1978-10-01': ("none", "none", "none", "none", "none"),
'1978-11-01': ("none", "none", "none", "none", "none"),
'1978-12-01': ("none", "none", "none", "none", "none"),


'1979-01-01': ("none", "none", "none", "none", "none"),
'1979-02-01': ("none", "none", "none", "none", "none"),
'1979-03-01': ("none", "none", "none", "none", "none"),
'1979-04-01': ("none", "none", "none", "none", "none"),
'1979-05-01': ("none", "none", "none", "none", "none"),
'1979-06-01': ("none", "none", "none", "none", "none"),
'1979-07-01': ("none", "none", "none", "none", "none"),
'1979-08-01': ("none", "none", "none", "none", "none"),
'1979-09-01': ("none", "none", "none", "none", "none"),
'1979-10-01': ("none", "none", "none", "none", "none"),
'1979-11-01': ("KMG348", "none", "none", "none", "none"),
'1979-12-01': ("none", "none", "none", "none", "none"),


'1980-01-01': ("none", "none", "none", "none", "none"),
'1980-02-01': ("none", "none", "none", "none", "none"),
'1980-03-01': ("none", "none", "none", "none", "none"),
'1980-04-01': ("none", "none", "none", "none", "none"),
'1980-05-01': ("KSD681", "none", "none", "none", "none"),
'1980-06-01': ("none", "none", "none", "none", "none"),
'1980-07-01': ("none", "none", "none", "none", "none"),
'1980-08-01': ("none", "none", "none", "none", "none"),
'1980-09-01': ("none", "none", "none", "none", "none"),
'1980-10-01': ("none", "none", "none", "none", "none"),
'1980-11-01': ("none", "none", "none", "none", "none"),
'1980-12-01': ("none", "none", "none", "none", "none"),



'1981-01-01': ("none", "none", "none", "none", "none"),
'1981-02-01': ("none", "none", "none", "none", "none"),
'1981-03-01': ("none", "none", "none", "none", "none"),
'1981-04-01': ("none", "none", "none", "none", "none"),
'1981-05-01': ("none", "none", "none", "none", "none"),
'1981-06-01': ("none", "none", "none", "none", "none"),
'1981-07-01': ("none", "none", "none", "none", "none"),
'1981-08-01': ("LKF926", "none", "none", "none", "none"),
'1981-09-01': ("LPG487", "none", "none", "none", "none"),
'1981-10-01': ("none", "none", "none", "none", "none"),
'1981-11-01': ("none", "none", "none", "none", "none"),
'1981-12-01': ("none", "none", "none", "none", "none"),


'1983-01-01': ("none", "none", "none", "none", "none"),
'1983-02-01': ("MDG365", "none", "none", "none", "none"),
'1983-03-01': ("none", "none", "none", "none", "none"),
'1983-04-01': ("none", "none", "none", "none", "none"),
'1983-05-01': ("none", "none", "none", "none", "none"),
'1983-06-01': ("none", "none", "none", "none", "none"),
'1983-07-01': ("none", "none", "none", "none", "none"),
'1983-08-01': ("none", "none", "none", "none", "none"),
'1983-09-01': ("none", "none", "none", "none", "none"),
'1983-10-01': ("none", "none", "none", "none", "none"),
'1983-11-01': ("none", "none", "none", "none", "none"),
'1983-12-01': ("none", "none", "none", "none", "none"),

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


