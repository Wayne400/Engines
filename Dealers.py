


def get_dealers():
    dealers = {

'112244': ("Wallhampton Motors", "23 Bingo St.", "Wallhampton", "LD007"),

'2222': ("Reg Blunty Motors", "47 Beale St", "Memphis", "LD666"),

'310333': ("Grenville Motors", "83-97 Flinders St.", "Darlinghurst", "LD"),
'310878': ("Anonymous", " St.", "Darlinghurst", "LD4377"),
'315298': ("Capitol Motors", " St.", "Unknown", "LD"),
'3494411': ("Lanock Motors", "54 Maroubra Rd", "Maroubra" , "LD"),
'3584644': ("Capitol Motors", " St.", "Unknown", "LD"),
'3893233': ("Larke Hoskins", "268 Oxford St", "Bondi Junction", "LD402"),

'410377': ("Morisson Motors", "Street", "unknown", "DL"),
'418452': ("Lancaster Leyland", "728 Pacific Hwy", "418452", "LD"),
'430231': ("Rowley Motors", "unknown", "unknown", "LD238"),
'430702': ("Caldwells GMH", "452 Pacific Hwy", "Crows Nest", "LD"),
'432999': ("Scotts Motors", "373 Pacific Hwy", "Artarmon", "LD01487"),
'434411': ("Scotts Motors", "373 Pacific Hwy", "Artarmon", "LD01487"),

'5240214': ("WH Lober & Co", "1 Kiora Rd.", "Miranda", "LD402"),
'5252277': ("Larke Hoskins", "Miranda", "Miranda", "LD402"),
'590425': ("James House of Cars", "58 Princes Highway", "Arncliffe", "LD"),
'5872115': ("Larry Mason", "Highway", "unknown", "LD389"),
'5872646': ("Anonymous", "Highway", "unknown", "LD172"),

'6355593': ("John Newell Motors", "155 Great Western Highway", "Westmead", "LD395"),
'6359755': ("Mazda House", "42-46 Church St.", "Parramatta", "LD"),
'6371025': ("Marshalls Motors", "Church St.", "Parramatta", "LD"),
'6481980': ("Ron Muir Cars", "44 Parramatta Rd", "Lidcombe", "LD"),
'6484311': ("John A Gilbert", "76 Parramatta Rd", "Lidcombe", "LD"),
'6488033': ("Capitol Motors", "Parramatta Rd", "Unknown", "LD"),
'6672484': ("Mascot Motors", "180 O'Riordan St.", "Mascot", "LD1091"),
'6674460': ("Mascot Motors", "180 O'Riordan St.", "Mascot", "LD1091"),
'6831933': ("Maypow Motors", "606 Church St", "North Parramatta", "LD"),
'648XXXX': ("Robert Carroll Motors", "99 Parramatta Rd", "Auburn", "LD284"),

'7265666': ("Gilbert & Roach", "662 Woodville Rd", "Guildford", "LD30"),
'7278554': ("Ken Sale Motors", "726 Woodville Rd", "Villawood", "LD"),
'7476666': ("John Muirs Quality Corner", "275 Parramatta Rd", "Five Dock", "LD198"),
'741790': ("Anonymous", " Parramatta Rd", "Five Dock", "LD904i"),
'742332': ("John Muirs Quality Corner", "275 Parramatta Rd", "Five Dock", "LD198"),
'7451255': ("Anonymous", "unknown", "unknown", "LD763"),
'749705': ("Jubilee", "155 Parramatta Rd", "Five Dock", "LD"),
'7597291': ("Motor & Marine", "unknown Rd.", "unknown", "LD"),
'7599774': ("Ronstan Motors", "875 Canterbury Rd.", "Lakemba", "LD"),
'766988': ("Larke Hoskins", "190 Parramatta Rd.", "Homebush", "LD405"),
'766141': ("Barr Motors", "unknown", "unknown", "LDBARR"),
'7978044': ("Frank Crott Motors", "Ashfield", "Ashfield", "LD710"),
'7980000': ("Geoghegans Recreational Vehicles", "253 Parramatta Rd.", "Haberfield", "LD188"),
'7980055': ("RC Phillips", "670 Parramatta Rd.", "Croydon", "LD"),
'7980900': ("British & Continental Cars", "Haberfield", "Haberfield", "LD"),
'7984144': ("Anonymous", "Haberfield", "Haberfield", "LD3545"),
'7985048': ("RC Phillips", "25 Parramatta Rd.", "Five Dock", "LD"),
'7985155': ("John A Gilbert", "22 Parramatta Rd.", "Summer Hill", "LD"),
'7985616': ("Lervan Traders", "277 Parramatta Rd.", "Haberfield", "LD01111"),
'7991111': ("Monaco Motors", "Cnr Sloane St & Parramatta Rd.", "Haberfield", "LD18733"),

'802281': ("Glendenning Motors", "693 Victoria Rd.", "Ryde", "802281"),
'8488222': ("Les Vagg", " Rd.", "Pennant Hills", "LD"),
'855226': ("Baker Gadd of Ryde", "1026 Victoria Rd", "West Ryde", "LD205"),
'865727': ("Epping Motors", "58 Rawson St", "Epping", "LD"),
'866727': ("Epping Motors", "58 Rawson St", "Epping", "LD"),

'930461': ("Pacific Ford", "780 Pittwater Rd", "Brookvale", "LD726"),
'9382255': ("Murphy Johnston Imported Cars", "620 Pittwater Rd", "Brookvale", "LD253"),
'9699513': ("Norman G Booth", "501 Military Rd", "Mosman", "LD"),
'9973470': ("unknown", "unknown Rd", "Manly", "LD315"),


}
    return dealers





def main():

    dealers = get_dealers()

    for key in dealers:
       dealer_data = dealers[key]
       dealer_name = dealer_data[0]
       print key, dealer_name



if __name__ == '__main__':
    main()


