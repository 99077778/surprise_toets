import time, math, random

player_attack = 1
player_defense = 0
player_health = 3

sleutel = 0
ruppee = 0


# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)


# === [kamer7] === #
print('je loopt door een kamer en vint een ruppee')
ruppee = 1
print('je ziet 2 kanten die je op kan, rechtdoor of rechts')
keuzenarupee = input("Wil je naar rechts gaan? (j/n): ")

time.sleep(1)

if keuzenarupee.lower() == 'n':
    


    # === [kamer 2] === #
    nummer1 = random.randint(10, 25)
    nummer2 = random.randint(-5, 75)
    antwoord = (nummer1 + nummer2)

    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een sleutel vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    print(f'Daarboven zie je een som staan {nummer1} + {nummer2} = ')
    inputantwoord = int(input('Wat toest je in?: '))

    if inputantwoord == antwoord:
        print('Het stadbeeld laat de sleutel vallen en je pakt het op')
        sleutel = 1
        waar6of3 = input('Je kan nu door 2 kamers, maar welke (kamer3 of kamer6): ')
    else:
        print('Er gebeurt niets....')
        #sleutel = 0
        waar6of3 = input('Je kan nu door 2 kamers, maar welke (kamer3 of kamer6): ')

    print('Je zie een deur achter het standbeeld.')
    print('')
    time.sleep(1)


    if waar6of3 == 6 or waar6of3.lower() == 'kamer6' or waar6of3.lower() == 'kamer 6':
        # === [kamer 6] === #
        zombie_attack = 1
        zombie_defense = 0
        zombie_health = 2
        print(f'Dapper loop je de kamer binnen.')
        print('Je loopt tegen een zombie aan.')

        zombie_hit_damage = (zombie_attack - player_defense)
        if zombie_hit_damage <= 0:
            print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
        else:
            zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
            
            player_hit_damage = (player_attack - zombie_defense)
            player_attack_amount = math.ceil(zombie_health / player_hit_damage)

            if player_attack_amount < zombie_attack_amount:
                print(f'In {player_attack_amount} rondes versla je de zombie.')

                player_health -= player_attack_amount * zombie_hit_damage

                print(f'Je health is nu {player_health}.')
            else:
                print('Helaas is de zombie te sterk voor je.')
                print('Game over.')
                exit()
        print('')
        time.sleep(1)

    else:
        # === [kamer 8] === #
        print('je komt in een kamer met een gokmachine')
        print('')
        print('er worden 2 dobbelstenen gerold in de machine')
        print('als de uitkomst hoger dan 7 is, verdubbeld je ruppees')
        print('als de uitkomst 7 is, krijg je 1 ruppee en 4 health erbij')
        print('als de uitkomst minder dan 7 is verlies je 1 health')
        print('')
        spelen = input('wil je spelen (y/n): ')
        if spelen.lower() == 'y':
            dobbel1 = random.randint(1, 6)
            dobbel2 = random.randint(1, 6)
            print(f"de eerste dobbelsteen valt op {dobbel1}")
            time.sleep(1)
            print(f"en de tweede op {dobbel2}")
            uitkomst = dobbel1 + dobbel2
            if uitkomst == 7:
                print(f'de uitkomst is {uitkomst}, je krijgt 1 ruppee en 4 health erbij. nu heb je {ruppee} ruppees en {player_health} health')
            elif uitkomst > 7:
                print(f'de uitkomst is {uitkomst}, je ruppees verdubbelen, je hebt nu {ruppee} ruppees')
                
        else:
            print('je gaat verder')







        # === [kamer 3] === #
        # rndomitem = random.randint(1, 2)

        # if rndomitem == 1:
        #     item = 'schild'
        #     player_defense += 1
        # else:
        #     item = 'zwaard'
        #     player_attack += 2

        # print('Je duwt hem open en stap een hele lange kamer binnen.')
        # print(f'In deze kamer staat een tafel met daarop een {item}.')
        # print(f'Je pakt het {item} op en houd het bij je.')
        # print('Op naar de volgende deur.')
        # print('')
        # time.sleep(1)
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
            elif item_keuze.lower() == 'niks' or item_keuze == '':
                print('je koopt niets')
                item = 'niks'
            else:
                print('je hebt geen rupees om items te kopen')
                item = 'niks'
else:


    # === [kamer 8 (op afsnijden manier)] === #
    print('je komt in een kamer met een gokmachine')
    print('')
    print('er worden 2 dobbelstenen gerold in de machine')
    print('als de uitkomst hoger dan 7 is, verdubbeld je ruppees')
    print('als de uitkomst 7 is, krijg je 1 ruppee en 4 health erbij')
    print('als de uitkomst minder dan 7 is verlies je 1 health')
    print('')
    spelen = input('wil je spelen (y/n): ')
    if spelen.lower() == 'y':
        dobbel1 = random.randint(1, 6)
        dobbel2 = random.randint(1, 6)
        print(f"de eerste dobbelsteen valt op {dobbel1}")
        time.sleep(1)
        print(f"en de tweede op {dobbel2}")
        uitkomst = dobbel1 + dobbel2
        if uitkomst == 7:
            print(f'de uitkomst is {uitkomst}, je krijgt 1 ruppee en 4 health erbij. nu heb je {ruppee} ruppees en {player_health} health')
        elif uitkomst > 7:
            print(f'de uitkomst is {uitkomst}, je ruppees verdubbelen, je hebt nu {ruppee} ruppees')
            
    else:
        print('je gaat verder')


    # === [kamer 3, (op afsnijden manier)] === #
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
        elif item_keuze.lower() == 'niks' or item_keuze == '':
            print('je koopt niets')
            item = 'niks'
        else:
            print('je hebt geen rupees om items te kopen')
            item = 'niks'




# === [kamer 4] === #
zombie2_attack = 2
zombie2_defense = 0
zombie2_health = 3
print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print('Je loopt tegen een sterkere zombie aan.')

zombie2_hit_damage = (zombie2_attack - player_defense)
if zombie2_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
else:
    zombie2_attack_amount = math.ceil(player_health / zombie2_hit_damage)
    
    player_hit_damage = (player_attack - zombie2_defense)
    player_attack_amount = math.ceil(zombie2_health / player_hit_damage)

    if player_attack_amount < zombie2_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')

        player_health -= player_attack_amount * zombie2_hit_damage

        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is deze zombie te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)



# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
if sleutel == 1:
    print('Je opent de kist met de sleutel die je gevonden hebt!')
    time.sleep(2)
    print('Je hebt gewonnen!!!')
    time.sleep(3)
    exit()
else:
    print("Je hebt geen sleutel en kan de kist niet openen.")
    time.sleep(2)
    print('je hebt verloren.')
    time.sleep(3)
    exit()