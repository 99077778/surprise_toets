print('je komt in een kamer met een verkoper')
print('hij heeft verschillende items te koop')

while ruppee > 0:
    time.sleep(1)
    print('ITEMS:')
    time.sleep(2)
    print('Item1: Zwaard (1 Ruppee)')
    time.sleep(1)
    print('Item2: Schild (1 Ruppee)')
    time.sleep(1)
    print('')
    item_keuze = input('''Wat wil je kopen:
    Item1 / Item2 / Niks
    : ''')
    if item_keuze == '1' or item_keuze.lower() == 'item1' or item_keuze.lower() == 'item 1' and ruppee > 0:
        ruppee = ruppee -1
        print(f'je hebt een zwaard gekocht, je hebt nog {ruppee} Ruppees')
        item = 'zwaard'
        player_attack +=2
    elif item_keuze == '2' or item_keuze.lower() == 'item2' or item_keuze.lower() == 'item 2' and ruppee > 0:
        ruppee = ruppee -1
        print(f'je hebt een schild gekocht, je hebt nog {ruppee} Ruppees')
        item = 'schild'
        player_defense +=1
    else:
        print('je koopt niets')
        item = 'niks'

print('je hebt geen rupees meer om items te kopen')