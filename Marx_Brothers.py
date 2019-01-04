from collections import defaultdict


Brothers = defaultdict(list)
Brothers["marxes"] = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo' ]
Brothers["pythons"] = ['Chapman', 'Cleese', 'Idle', 'Jones', 'Palin', 'Gilliam']
Brothers["kennedys"] = ['John', 'Robert', 'Edward']
# brothers = [marxes, pythons, kennedys]

Brothers["castros"] = ["Raul", "Fidel"]  # add brother Wally Castro

for family in Brothers:
    print family, Brothers[family]
