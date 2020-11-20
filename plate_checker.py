import re

def generate_IQ_block():

    IQ_plates = []
    for digit_1 in range(65, 70):
        for digit_2 in range(65, 91):
            for digit_3 in range(65, 91):
                if digit_3 == 73 or digit_3 == 81:
                    IQ_plates.append(chr(digit_1) + chr(digit_2) + chr(digit_3))

        for digit_3 in range(65, 91):
            for digit_2 in range(65, 91):
                if digit_2 == 73:
                    if digit_2 != digit_3:
                        IQ_plates.append(chr(digit_1) + chr(digit_2) + chr(digit_3))

        for digit_3 in range(65, 91):
            for digit_2 in range(65, 91):
                if digit_2 == 81:
                    if digit_2 != digit_3:
                        IQ_plates.append(chr(digit_1) + chr(digit_2) + chr(digit_3))

    IQ_plates.sort()
    return IQ_plates



def get_IQ_index(target_plate):

    iq_plates = []
    for digit_1 in range(65, 70):
        for digit_2 in range(65, 91):
            for digit_3 in range(65, 91):
                if digit_3 == 73 or digit_3 == 81:
                    iq_plates.append(chr(digit_1) + chr(digit_2) + chr(digit_3))

        for digit_3 in range(65, 91):
            for digit_2 in range(65, 91):
                if digit_2 == 73:
                    if digit_2 != digit_3:
                        iq_plates.append(chr(digit_1) + chr(digit_2) + chr(digit_3))

        for digit_3 in range(65, 91):
            for digit_2 in range(65, 91):
                if digit_2 == 81:
                    if digit_2 != digit_3:
                        iq_plates.append(chr(digit_1) + chr(digit_2) + chr(digit_3))

    iq_plates.sort()
    iq_index = 10000
    if target_plate[0:3] in iq_plates:
        iq_index = iq_plates.index(target_plate[0:3])

    return iq_index


def get_block_number(target_plate):
    plate_list = []

    stuff = list(target_plate)
    letterQ = 'Q'
    letterI = 'I'

    return (ord(stuff[1]) - ord('A')) * 26 + (1 + ord(stuff[2]) - ord('A'))




def main():



    nsw_series_one = {'6001':"CAA000" , '6101': 'CLL000', '6201': 'CTA000', '6301' : 'DAA000',
                    '6401': 'DKA000', '6501': 'DOJ000', '6601': 'EDA000', '6605': 'EFA000', '6610': 'EGB560','6701':'EMA000',
                    '6812': 'EZZ999'}

    nsw_series_two = {'1968': 'AAA000', '1969': 'BAJ000', '1970': 'BZZ999'}


    nsw_series_three = { '1970': 'AAI000', '1971': 'CWI000','1972': 'DXI000', '1973': 'EZQ999'}

    nsw_series_four = {'1972': 'GAA000','1973': 'GEA000', '1974': 'GQA000', '1975': 'HEA000',
                    '1976': 'HQA000', '1977': 'JCA050', '1978':'JPE050', '1979': 'KBH050',
                    '1980': 'FOA000', '1981':'LCZ050', '1982':'LOS050', '1983':'MBE050', '1984':'MOZ050'}



    target_plate = 'AQA878'
    plate_list = []
    if re.match('^[A-Q][A-Z][A-Z][0-9][0-9][0-9]',target_plate):
        print "valid nsw plate"

    if re.match('^[A-E][I,Q][A-Z][0-9][0-9][0-9]',target_plate):
        print "2rd digit IQ woopeeh"
        h = re.match('^[A-E][I,Q][A-Z][0-9][0-9][0-9]',target_plate)
        print h.group(0)
    if re.match('^[A-E][A-Z][I,Q][0-9][0-9][0-9]',target_plate):
        print "3rd digit IQ woopeeh"


    stuff = list(target_plate)
    letterQ = 'Q'
    letterI = 'I'
    print len(target_plate)
    print stuff

    if re.match('^[A-E][I,Q][A-Z][0-9][0-9][0-9]', target_plate) or re.match('^[A-E][A-Z][I,Q][0-9][0-9][0-9]',target_plate):
       block_number = get_IQ_index(target_plate)
    else:
       block_number = get_block_number(target_plate)

    print block_number


    if (((letterQ in stuff) or (letterI in stuff)) and target_plate < nsw_series_four["1972"]):
        nsw_series = nsw_series_three
        year_list = list(nsw_series_three.keys())
    elif target_plate < nsw_series_one["6001"]:
        nsw_series = nsw_series_two
        year_list = list(nsw_series_two.keys())
    elif target_plate >= nsw_series_four["1972"]:
        nsw_series = nsw_series_four
        year_list = list(nsw_series_four.keys())
    else:
        nsw_series = nsw_series_one
        year_list = list(nsw_series_one.keys())



    year_list.sort()
 #   print year_list
    for year in year_list: # create list from wiki table, sort by year
  #      print year , nsw_series[year]
        plate_list.append(nsw_series[year])


    print plate_list
    print year_list
    print ('im looking for ' + target_plate)

    search_key = 0
    for plate in plate_list:
        print plate , year_list[search_key]
        if  plate > target_plate:
            print target_plate, year_list[search_key -1 ]
            break
        search_key = search_key + 1

    print "found a plate from " + year_list[search_key - 1]
    iq_index = 9999
    wally = generate_IQ_block()
    print wally
    iq_index = get_IQ_index(target_plate)


    print iq_index, target_plate[0:3] , "wally"

if __name__ == '__main__':
    main()