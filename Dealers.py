


def get_dealers():
    dealers = {

'112244': ("Wallhampton Motors", "23 Bingo St.", "Wallhampton", "LD007"),

'2222': ("Reg Blunty Motors", "47 Beale St", "Memphis", "LD666"),

'310333': ("Grenville Motors", "83-97 Flinders St.", "Darlinghurst", "LD"),
'310878': ("Anonymous", " St.", "Darlinghurst", "LD4377"),
'315298': ("Capitol Motors", " St.", "Unknown", "LD"),
'3494411': ("Lanock Motors", "54 Maroubra Rd", "Maroubra" , "LD"),
'3584644': ("Capitol Motors", " St.", "Unknown", "LD"),

'410377': ("Morisson Motors", "Street", "unknown", "DL"),
'418452': ("Lancaster Leyland", "728 Pacific Hwy", "418452", "LD"),
'430231': ("Rowley Motors", "unknown", "unknown", "LD238"),

'5252277': ("Larke Hoskins", "Miranda", "Miranda", "LD402"),
'590425': ("James House of Cars", "58 Princes Highway", "Arncliffe", "LD"),
'5872115': ("Larry Mason", "Highway", "unknown", "LD389"),
'5872646': ("Anonymous", "Highway", "unknown", "LD172"),

'6359755': ("Mazda House", "42-46 Church St.", "Parramatta", "LD"),
'6371025': ("Marshalls Motors", "Church St.", "Parramatta", "LD"),
'6481980': ("Ron Muir Cars", "44 Parramatta Rd", "Lidcombe", "LD"),
'6488033': ("Capitol Motors", "Parramatta Rd", "Unknown", "LD"),
'6672484': ("Mascot Motors", "180 O'Riordan St.", "Mascot", "LD1091"),
'6674460': ("Mascot Motors", "180 O'Riordan St.", "Mascot", "LD1091"),
'6831933': ("Maypow Motors", "606 Church St", "North Parramatta", "LD"),
'648XXXX': ("Robert Carroll Motors", "99 Parramatta Rd", "Auburn", "LD284"),

'7265666': ("Gilbert & Roach", "662 Woodville Rd", "Guildford", "LD30"),
'7476666': ("John Muirs Quality Corner", "275 Parramatta Rd", "Five Dock", "LD198"),
'741790': ("Anonymous", " Parramatta Rd", "Five Dock", "LD904i"),
'742332': ("John Muirs Quality Corner", "275 Parramatta Rd", "Five Dock", "LD198"),
'766988': ("Larke Hoskins", "Homebush", "Homebush", "LD405"),
'766141': ("Barr Motors", "unknown", "unknown", "LDBARR"),
'7978044': ("Frank Crott Motors", "Ashfield", "Ashfield", "LD710"),
'7980000': ("Geoghegans Recreational Vehicles", "253 Parramatta Rd.", "Haberfield", "LD"),
'7980900': ("British & Continental Cars", "Haberfield", "Haberfield", "LD"),
'7984144': ("Anonymous", "Haberfield", "Haberfield", "LD3545"),
'7985616': ("Lervan Traders", "277 Parramatta Rd.", "Haberfield", "LD01111"),

'802281': ("Glendenning Motors", "693 Victoria Rd.", "Ryde", "802281"),

'9382255': ("Murphy Johnston Imported Cars", "620 Pittwater Rd", "Brookvale", "LD253"),


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


