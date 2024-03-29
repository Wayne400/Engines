import re




def get_exchange_dict():



    exchange_dict = {}
    exchange_dict['20'] = 'Pitt St.'
    exchange_dict['25'] = 'Hunter St.'
    exchange_dict['27'] = 'Kent St.'

    exchange_dict['3'] = 'St. Leonards'
    exchange_dict['30'] = 'Bondi'
    exchange_dict['31'] = 'Darlinghurst'
    exchange_dict['33'] = 'Darlinghurst'
    exchange_dict['337'] = 'Vaucluse'
    exchange_dict['35'] = 'Kings Cross'
    exchange_dict['38'] = 'Woollahra'
    exchange_dict['389']= 'Bondi Junction'
    exchange_dict['39'] = 'Randwick'

    exchange_dict['41'] = 'Chatswood, Roseville'
    exchange_dict['412'] = 'Chatswood, Roseville'
    exchange_dict['42'] = 'Lane Cove'
    exchange_dict['43'] = 'Artarmon'
    exchange_dict['44'] = 'Pymble'
    exchange_dict['44'] = 'St Ives'
    exchange_dict['449'] = 'St Ives'
    exchange_dict['449'] = 'Turramurra'
    exchange_dict['450'] = 'Terry Hills'
    exchange_dict['451'] = 'Belrose'
    exchange_dict['451'] = "French's Forest"
    exchange_dict['46'] = 'Lindfield'
    exchange_dict['46'] = 'Roseville'
    exchange_dict['47'] = 'Asquith'
    exchange_dict['47'] = 'Hornsby'
    exchange_dict['476'] = 'Hornsby'
    exchange_dict['48'] = 'Wahroonga'
    exchange_dict['487'] = 'Waitara'
    exchange_dict['49'] = 'Gordon'
    exchange_dict['49'] = 'Killara'
    exchange_dict['498'] = 'Gordon'

    exchange_dict['50'] = 'Kingsgrove'
    exchange_dict['519'] = 'Newtown'
    exchange_dict['521'] = 'Kirrawee'
    exchange_dict['523'] = 'Cronulla'
    exchange_dict['524'] = 'Caringbah, Lilli Pilli'
    exchange_dict['525'] = 'Caringbah'
    exchange_dict['528'] = 'Jannali'
    exchange_dict['529'] = 'Sans Souci'
    exchange_dict['53'] = 'Peakhurst'
    exchange_dict['546'] = 'Carlton'
    exchange_dict['55'] = 'Earlwood'
    exchange_dict['56'] = 'Stanmore'
    exchange_dict['560'] = 'Dulwich Hill'
    exchange_dict['579'] = 'Oatley, Hurstville'
    exchange_dict['590241'] = 'Purnell Motors'

    exchange_dict['602'] = 'Liverpool'
    exchange_dict['61'] = 'Elizabeth St'
    exchange_dict['621'] = 'Seven Hills'
    exchange_dict['623'] = 'St. Marys'
    exchange_dict['622'] = 'Seven Hills'
    exchange_dict['625'] = 'Rooty Hill'
    exchange_dict['630'] = 'Northmead'
    exchange_dict['631'] = 'Toongabbie'
    exchange_dict['632'] = 'Guilford'
    exchange_dict['635'] = 'Parramatta'
    exchange_dict['637'] = 'Merrylands. Parramatta'
    exchange_dict['644'] = 'Bass Hill, Sefton'
    exchange_dict['648'] = 'Auburn'
    exchange_dict['649'] = 'Auburn'
    exchange_dict['651'] = 'Dural'
    exchange_dict['665'] = 'Coogee'
    exchange_dict['667'] = 'Mascot'
    exchange_dict['67'] = 'Mascot'
    exchange_dict['698'] = 'Alexandria'

    exchange_dict['70'] = 'Bankstown'
    exchange_dict['708'] = 'Yagoona'
    exchange_dict['709'] = 'Yagoona'
    exchange_dict['74'] = 'Five Dock'
    exchange_dict['7476666'] = 'John Muirs Quality Corner, Five Dock'
    exchange_dict['745'] = 'Five Dock'
    exchange_dict['750'] = 'Lakemba'
    exchange_dict['759'] = 'Lakemba'
    exchange_dict['759'] = 'Punchbowl'
    exchange_dict['766988'] = 'Larke Hoskins L.D. 405, Homebush'
    exchange_dict['77'] = 'Revesby'
    exchange_dict['773'] = 'Padstow'
    exchange_dict['798'] = 'Five Dock, Haberfield'
    dealer_dict['7991555'] = "L.D. 148"

    exchange_dict['81'] = 'Drummoyne'
    exchange_dict['84'] = 'Pennant Hills'
    exchange_dict['848'] = 'Beecroft'
    exchange_dict['86'] = 'Epping'
    exchange_dict['871'] = 'Carlingford'
    exchange_dict['888'] = 'North Ryde'

    exchange_dict['90'] = 'Neutral Bay'
    exchange_dict['909'] = 'Cremorne'
    exchange_dict['918'] = 'Avalon Beach'
    exchange_dict['92'] = 'North Sydney'
    exchange_dict['929'] = 'North Sydney'
    exchange_dict['93'] = 'Brookvale'
    exchange_dict['938'] = 'Brookvale'
    exchange_dict['94'] = 'Balgowlah'
    exchange_dict['94'] = 'Seaforth'
    exchange_dict['949'] = 'Seaforth'
    exchange_dict['95'] = 'Castlecrag'
    exchange_dict['95'] = 'Northbridge'
    exchange_dict['969'] = 'Mosman'
    exchange_dict['97'] = 'Manly'
    exchange_dict['977'] = 'Manly'
    exchange_dict['98'] = 'Collaroy'
    exchange_dict['98'] = 'Dee Why'
    exchange_dict['982'] = 'Dee Why'
    exchange_dict['99'] = 'Mona Vale'

    return exchange_dict


def main():


    exchange_dictionary = get_exchange_dict()
    number = '6612233'
    if len(number) == 5:
        prefix = number[:1]
    if len(number) == 6:
        prefix = number[:2]
    if len(number) == 7:
        prefix = number[:3]

    exchange_list = list(exchange_dictionary.keys())
    if prefix in exchange_list:
        suburb = exchange_dictionary[prefix]
    else:
        suburb = 'bonk'


    print suburb



if __name__ == '__main__':
    main()