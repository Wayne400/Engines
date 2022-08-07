import re




def get_exchange_dict():



    exchange_dict = {}

    exchange_dict['042'] = 'Wollongong'
    exchange_dict['043'] = 'Gosford'
    exchange_dict['045'] = 'Windsor'
    exchange_dict['046'] = 'Campbelltown'
    exchange_dict['047'] = 'Penrith'
    exchange_dict['049'] = 'Newcastle'

    exchange_dict['20'] = 'Pitt St.'
    exchange_dict['211'] = 'Broadway'
    exchange_dict['25'] = 'Hunter St.'
    exchange_dict['27'] = 'Kent St.'

    exchange_dict['3'] = 'St. Leonards'
    exchange_dict['30'] = 'Bondi'
    exchange_dict['31'] = 'Darlinghurst, Paddington'
    exchange_dict['32'] = 'Rushcutters Bay, Double Bay'
    exchange_dict['327'] = 'Point Piper'
    exchange_dict['328'] = 'Edgecliff'
    exchange_dict['33'] = 'Darlinghurst'
    exchange_dict['337'] = 'Vaucluse'
    exchange_dict['34'] = 'Maroubra Junction'
    exchange_dict['349'] = 'Maroubra'
    exchange_dict['35'] = 'Kings Cross, Woolloomooloo'
    exchange_dict['356'] = 'Sydney, William St.'
    exchange_dict['357'] = 'Kings Cross'
    exchange_dict['358'] = 'East Sydney'
    exchange_dict['359'] = 'Kings Cross, Woolloomooloo'
    exchange_dict['36'] = 'Double Bay'
    exchange_dict['37'] = 'Rose Bay'
    exchange_dict['371'] = 'Rose Bay'
    exchange_dict['38'] = 'Woollahra'
    exchange_dict['387']= 'Bondi'
    exchange_dict['389']= 'Bondi Junction'
    exchange_dict['39'] = 'Randwick'
    exchange_dict['399'] = 'Eastern Suburbs???'

    exchange_dict['40'] = 'Killarney Heights'
    exchange_dict['41'] = 'Chatswood, Roseville'
    exchange_dict['411'] = 'Chatswood, Roseville ???'
    exchange_dict['412'] = 'Chatswood, Roseville'
    exchange_dict['42'] = 'Lane Cove'
    exchange_dict['43'] = 'Artarmon'
    exchange_dict['438'] = 'North Shore???'
    exchange_dict['439'] = 'Crows Nest'
    exchange_dict['44'] = 'Pymble'
    exchange_dict['44'] = 'St Ives'
    exchange_dict['449'] = 'St Ives, Turramurra, Pymble'
    exchange_dict['450'] = 'Terry Hills'
    exchange_dict['451'] = 'Belrose'
    exchange_dict['451'] = "French's Forest"
    exchange_dict['467'] = 'Lindfield'
    exchange_dict['46'] = 'Lindfield, Roseville'
    exchange_dict['47'] = 'Asquith, Hornsby'
    exchange_dict['476'] = 'Hornsby, Asquith'
    exchange_dict['48'] = 'Wahroonga'
    exchange_dict['487'] = 'Waitara, Wahroonga'
    exchange_dict['49'] = 'Gordon'
    exchange_dict['49'] = 'Killara'
    exchange_dict['498'] = 'Gordon'

    exchange_dict['50'] = 'Kingsgrove, Hurstville'
    exchange_dict['502'] = 'Bexley'
    exchange_dict['51'] = 'Newtown, Camperdown'
    exchange_dict['516'] = 'Around Newtown?'
    exchange_dict['519'] = 'Newtown, St. Peters, Marrickville'
    exchange_dict['52'] = 'Miranda'
    exchange_dict['520'] = 'Engadine'
    exchange_dict['521'] = 'Kirrawee'
    exchange_dict['522'] = 'Sylvania Hts.'
    exchange_dict['523'] = 'Cronulla'
    exchange_dict['524'] = 'Caringbah, Lilli Pilli, Taren Point'
    exchange_dict['525'] = 'Caringbah, Gymea'
    exchange_dict['528'] = 'Jannali'
    exchange_dict['529'] = 'Sans Souci'
    exchange_dict['53'] = 'Peakhurst'
    exchange_dict['546'] = 'Blakehurst, Carlton'
    exchange_dict['55'] = 'Earlwood'
    exchange_dict['555'] = 'Balmain'
    exchange_dict['559'] = 'Tempe'
    exchange_dict['56'] = 'Stanmore, Dulwich Hill'
    exchange_dict['560'] = 'Dulwich Hill'
    exchange_dict['569'] = 'Leichhardt'
    exchange_dict['57'] = 'Hurstvlle, Penshurst'
    exchange_dict['570'] = 'Hurstville'
    exchange_dict['579'] = 'Oatley, Hurstville, Penshurst'
    exchange_dict['58'] = 'Carlton'
    exchange_dict['587'] = 'Hurstville'
    exchange_dict['59'] = 'Rockdale, Arncliffe, Banksia'
    exchange_dict['597'] = 'Rockdale'
    exchange_dict['599'] = 'Rockdale, Arncliffe, Banksia'

    exchange_dict['602'] = 'Liverpool'
    exchange_dict['604'] = 'Smithfield, Ingleburn'
    exchange_dict['605'] = 'Around Liverpool ???'
    exchange_dict['607'] = 'Mt. Pritchard'
    exchange_dict['61'] = 'Elizabeth St'
    exchange_dict['621'] = 'Seven Hills'
    exchange_dict['622'] = 'Blacktown, Seven Hills, Lalor Park'
    exchange_dict['623'] = 'St. Marys'
    exchange_dict['625'] = 'Rooty Hill, Mt Druitt'
    exchange_dict['627'] = 'Riverstone'
    exchange_dict['628'] = 'Mt Druitt'
    exchange_dict['630'] = 'Northmead, Dundas, Winston Hills'
    exchange_dict['631'] = 'Toongabbie,Wentworthville'
    exchange_dict['632'] = 'Guilford'
    exchange_dict['634'] = 'Castle Hill'
    exchange_dict['635'] = 'Parramatta, Westmead'
    exchange_dict['637'] = 'Granville, Merrylands. Parramatta'
    exchange_dict['638'] = 'Rydalmere'
    exchange_dict['639'] = 'Baulkham Hills'
    exchange_dict['642'] = 'Chullora, Belfield'
    exchange_dict['644'] = 'Bass Hill, Sefton, Regents Park'
    exchange_dict['648'] = 'Auburn, Lidcombe'
    exchange_dict['649'] = 'Auburn'
    exchange_dict['651'] = 'Dural'
    exchange_dict['653'] = 'Galston'
    exchange_dict['660'] = 'Broadway'
    exchange_dict['662'] = 'Kingsford'
    exchange_dict['663'] = 'Rosebery, Kensington'
    exchange_dict['664'] = 'Clovelly'
    exchange_dict['665'] = 'Coogee'
    exchange_dict['666'] = 'Botany'
    exchange_dict['667'] = 'Mascot'
    exchange_dict['669'] = 'Botany'
    exchange_dict['67'] = 'Mascot'


    exchange_dict['673'] = 'St. Marys'
    exchange_dict['682'] = 'Merrylands'
    exchange_dict['683'] = 'North Parramatta'
    exchange_dict['69'] = 'Redfern'
    exchange_dict['692'] = 'Glebe'
    exchange_dict['698'] = 'Alexandria'
    exchange_dict['699'] = 'Alexandria'

    exchange_dict['70'] = 'Bankstown, Punchbowl, Yagoona'
    exchange_dict['707'] = 'Yagoona'
    exchange_dict['708'] = 'Bankstown, Yagoona'
    exchange_dict['709'] = 'Yagoona'
    exchange_dict['71'] = 'Summer Hill'
    exchange_dict['713'] = 'Unknown Summer Hill??'
    exchange_dict['72'] = 'Cabramatta'
    exchange_dict['726'] = 'Guildford, Cabramatta'
    exchange_dict['727'] = 'Fairfield, Cabramatta, Villawood'
    exchange_dict['728'] = 'Fairfield'
    exchange_dict['74'] = 'Burwood, Five Dock'
    exchange_dict['745'] = 'Five Dock, Burwood'
    exchange_dict['747'] = 'Burwood, Five Dock, Concord, Croydon'
    exchange_dict['750'] = 'Lakemba'
    exchange_dict['759'] = 'Punchbowl, Lakemba, Roselands'
    exchange_dict['76'] = 'Homebush, Flemington, Strathfield'
    exchange_dict['764'] = 'Homebush'
    exchange_dict['77'] = 'Revesby'
    exchange_dict['771'] = 'Panania, Revesby'
    exchange_dict['773'] = 'Padstow'
    exchange_dict['774'] = 'Revesby'
    exchange_dict['78'] = 'Campsie'
    exchange_dict['789'] = 'Belmore'
    exchange_dict['797'] = 'Ashfield, Summer Hill, Haberfield'
    exchange_dict['798'] = 'Croydon, Five Dock, Haberfield, Ashfield'
    exchange_dict['799'] = 'Haberfield'

    exchange_dict['80'] = 'West Ryde'
    exchange_dict['807'] = 'West Ryde'
    exchange_dict['81'] = 'Drummoyne'
    exchange_dict['816'] = 'Gladesville'
    exchange_dict['818'] = 'Gladesville Drummoyne ???'
    exchange_dict['819'] = 'Drummoyne'
    exchange_dict['82'] = 'Rozelle, Balmain'
    exchange_dict['827'] = 'Balmain'
    exchange_dict['84'] = 'Pennant Hills'
    exchange_dict['848'] = 'Beecroft'
    exchange_dict['85'] = 'Eastwood, West Ryde'
    exchange_dict['858'] = 'West Ryde'
    exchange_dict['86'] = 'Epping'
    exchange_dict['868'] = 'Epping'
    exchange_dict['869'] = 'Epping'
    exchange_dict['871'] = 'Carlingford, North Rocks'
    exchange_dict['872'] = 'Maybe Carlingford?'
    exchange_dict['88'] = 'North Ryde'
    exchange_dict['888'] = 'North Ryde'

    exchange_dict['90'] = 'Mosman, Neutral Bay'
    exchange_dict['909'] = 'Cremorne'
    exchange_dict['913'] = 'Narrabeen'
    exchange_dict['918'] = 'Avalon Beach'
    exchange_dict['919'] = 'Whale Beach'
    exchange_dict['92'] = 'North Sydney'
    exchange_dict['929'] = 'North Sydney'
    exchange_dict['93'] = 'Brookvale'
    exchange_dict['938'] = 'Brookvale'
    exchange_dict['939'] = 'Brookvale'
    exchange_dict['94'] = 'Balgowlah, Seaforth'
    exchange_dict['948'] = 'Balgowlah'
    exchange_dict['949'] = 'Balgowlah, Seaforth'
    exchange_dict['95'] = 'Castlecrag', 'Northbridge'
    exchange_dict['96'] = 'Mosman'
    exchange_dict['960'] = 'Mosman'
    exchange_dict['969'] = 'Mosman'
    exchange_dict['97'] = 'Manly'
    exchange_dict['977'] = 'Manly'
    exchange_dict['98'] = 'Dee Why', 'Collaroy'
    exchange_dict['982'] = 'Dee Why, Collaroy'
    exchange_dict['99'] = 'Mona Vale'
    exchange_dict['997'] = 'Newport'

    exchange_dict['043'] = 'Gosford'
    exchange_dict['066'] = 'Grafton'

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


    print(suburb)



if __name__ == '__main__':
    main()