import time, random

def welkombijyathzee():                 # Print de onderstaande zin
    print("Welkom bij Yathzee!")

def spelers_kiezen():                   # Kies of je met 1 of 2 spelers wilt spelen
    print("Je mag alleen of samen spelen.")
    while True:
        try:
            aantal_spelers = int(input("Met hoeveel spelers wil je dit spelen? (1/2) "))    # Input 1 of 2
            if aantal_spelers == 1:
                break                           # 1 speler
            elif aantal_spelers == 2:
                break                           # 2 spelers
            else:
                print("Dit is geen optie.")     # Geen optie (integer)
        except ValueError:
            print("Dit is geen optie.")         # Geen optie (string of floar)
    return aantal_spelers                       # Returned het gekozen aantal spelers zodat later wordt gebruikt voor aantal scorekaarten

def aantal_spellen_kiezen():
    print("Je mag 1, of 5 wedstrijden spelen.")
    while True:
        try:
            aantal_spellen = int(input("Hoeveel wedstrijden wil je spelen? (1/5) "))    # Input 1 of 5
            if aantal_spellen == 1:
                break                           # 1 Wedstrijd
            elif aantal_spellen == 5:
                break                           # 5 Wedstrijden
            else:
                print("Dit is geen optie.")     # Geen optie (integer)
        except ValueError:
            print("Dit is geen optie.")         # Geen optie (string of float)
    return aantal_spellen                       # Returned gekozen aantal spellen om te kiezen hoeveel wedstrijden er worden gespeelt.

def scorekaart(speleraantal):
    if speleraantal == 1:
        scorekaart = {
        "Aces": None,
        "Twos": None,
        "Threes": None,
        "Fours": None,
        "Fives": None,
        "Sixes": None,
        "Three of a Kind": None,
        "Four of a Kind": None,
        "Full House": None,
        "Small Straight": None,
        "Large Straight": None,
        "Top Score": None,
        "Chance": None
        }
        return scorekaart           # 1 speler scorekaart, wordt gereturned voor invullen
    elif speleraantal == 2:
        scorekaart = {
                "Aces": None,
                "Twos": None,
                "Threes": None,
                "Fours": None,
                "Fives": None,
                "Sixes": None,
                "Three of a Kind": None,
                "Four of a Kind": None,
                "Full House": None,
                "Small Straight": None,
                "Large Straight": None,
                "Top Score": None,
                "Chance": None
                }
        
        scorekaart2 = {
            "Aces": None,
            "Twos": None,
            "Threes": None,
            "Fours": None,
            "Fives": None,
            "Sixes": None,
            "Three of a Kind": None,
            "Four of a Kind": None,
            "Full House": None,
            "Small Straight": None,
            "Large Straight": None,
            "Top Score": None,
            "Chance": None
            }
        return scorekaart, scorekaart2      # 2 spelers scorekaarten, wordt gereturned voor invullen

def scorekaart_checken(scorekaart):
    res = any(waarde is None for waarde in scorekaart.values())     # Checked of any waarde in scorekaart None is, en dus nog niet volledig is ingevult of wel volledig is ingevult
    if res == True:
        print()        # Niet helemaal ingevult
    else:
        print("Totaal score berekenen")
    return res         # Wel helemaal ingevult

def dobbelstenen_gooien():
    dobbelstenen = {
    "Dobbelsteen 1": 0,
    "Dobbelsteen 2": 0,
    "Dobbelsteen 3": 0,
    "Dobbelsteen 4": 0,
    "Dobbelsteen 5": 0
    }                                                   # Lijst van dobbelstenen

    print("We gaan nu gooien...")
    totale_score = 0
    time.sleep(2)

    for dobbelsteen in dobbelstenen.keys():             # 5 keer dobbelsteen gooien
        gooi = random.randint(1, 6)                     # Gooit de dobbelsten
        dobbelstenen[dobbelsteen] = gooi
        print(f"{dobbelsteen} heeft een {gooi} gegooid.")   # Checked wat er is gegooit
        totale_score += gooi
    print(f" Totale waarde van deze beurt: {totale_score}") # Totale waarde van de gooi (voor Chance)
    return dobbelstenen         # Returned de aantalen die gegooit zijn

def nog_een_keer(worp, dobbelstenen):
    behouden_dobbels = []       # Lijst van dobbelsteen waardes die je niet nog een keer gooit

    if worp == 3:
        print("Je moet nu een categorie kiezen.")
        behouden_dobbels = list(dobbelstenen.keys())    # Kijken welke dobbelsteen waardes er zijn
        return "CATKIEZEN", behouden_dobbels, worp      # Na worp 3, verplicht categorie kiezen

    opnieuw_catkiezen = input("Wil je opnieuw gooien of een categorie kiezen? (OPNIEUW/CATKIEZEN) ").upper()    # Input opnieuw of categorie kiezen
    if opnieuw_catkiezen == "OPNIEUW":
        worp += 1       # Elke nieuwe gooi + 1 bij de counter
        aantal_keuzes = 0       # 5 keuzes nodig
        while aantal_keuzes < 5:    # Terwijl er nog iets moet worden gekozen, blijf vragen
            dobbel_houden = input("Welke dobbelsteen/stenen wilt u houden? (1-5/GEEN) ").upper()
            if dobbel_houden == "1":
                if "Dobbelsteen 1" in behouden_dobbels:
                    print("Deze dobbelsteen is al gekozen.")        # Al gekozen, dan niet nog een keer
                else:
                    behouden_dobbels.append("Dobbelsteen 1")
                    aantal_keuzes += 1      # Voeg de waarde van dobbelsteen 1 toe
            elif dobbel_houden == "2":
                if "Dobbelsteen 2" in behouden_dobbels:
                    print("Deze dobbelsteen is al gekozen")         # Al gekozen, dan niet nog een keer
                else:
                    behouden_dobbels.append("Dobbelsteen 2")
                    aantal_keuzes += 1      # Voeg de waarde van dobbelsteen 2 toe
            elif dobbel_houden == "3":
                if "Dobbelsteen 3" in behouden_dobbels:
                    print("Deze dobbelsteen is al gekozen.")        # Al gekozen, dan niet nog een keer
                else:
                    behouden_dobbels.append("Dobbelsteen 3")
                    aantal_keuzes += 1      # Voeg de waarde van dobbelsteen 3 toe
            elif dobbel_houden == "4":
                if "Dobbelsteen 4" in behouden_dobbels:
                    print("Deze dobbelsteen is al gekozen.")        # Al gekozen, dan niet nog een keer
                else:
                    behouden_dobbels.append("Dobbelsteen 4")
                    aantal_keuzes += 1      # Voeg de waarde van dobbelsteen 4 toe
            elif dobbel_houden == "5":
                if "Dobbelsteen 5" in behouden_dobbels:
                    print("Deze dobbelsteen is al gekozen.")        # Al gekozen, dan niet nog een keer
                else:
                    behouden_dobbels.append("Dobbelsteen 5")
                    aantal_keuzes += 1      # Voeg de waarde van dobbelsteen 5 toe
            elif dobbel_houden == "GEEN":
                aantal_keuzes += 1      # Als een wordt behouden
            else:
                print("Sorry, dat is geen geldig nummer.")      # 6 of hoger gekozen of iets anders dan geen

        for dobbelsteen in dobbelstenen:
            if dobbelsteen not in behouden_dobbels:
                dobbelstenen[dobbelsteen] = random.randint(1, 6)    # Gooi weer voor alle dobbelstenen de niet zijn behouden

        for dobbelsteen in dobbelstenen:
            gooi = dobbelstenen[dobbelsteen]
            print(f"{dobbelsteen} heeft een {gooi} gegooid.")       # Print de waardes van dobbelstenen

    elif opnieuw_catkiezen == "CATKIEZEN":
        print("Categorie kiezen")

    return opnieuw_catkiezen, behouden_dobbels, worp                # Returned de keuze

def categorie_mogelijkheden(dobbelstenen): # Kijken of je een categorie kan kiezen
    totale_aces = 0
    totale_twos = 0
    totale_threes = 0
    totale_fours = 0
    totale_fives = 0
    totale_sixes = 0
    ToaK_totaal = 0
    FoaK_totaal = 0
    totaal_chance = 0           # Lijst van totale scores

    dobbelsteen_waardes = list(dobbelstenen.values())   # Waardes van je eindwaardes van de dobbelstenen
    print(dobbelsteen_waardes) # Print de waardes
    frequentie = { 
        "Ones": 0, 
        "Twos": 0, 
        "Threes": 0, 
        "Fours": 0, 
        "Fives": 0, 
        "Sixes": 0 
    }               # Lijst van frequentie

    #               Keuzelijst          # 
    mogelijke_keuzes = [] 

    #               Aces               # 
    aces = dobbelsteen_waardes.count(1) # Check of 1 in de waardes zit
    if aces >= 1:                       # Zo ja, voeg toe aan frequentie lijst en voeg toe aan mogelijke keuzes
        print("Aces mogelijk.") 
        totale_aces = aces * 1 
        print(f"Totale score van Aces is {totale_aces}.") 
        frequentie["Ones"] = aces 
        mogelijke_keuzes.append("ACES") 
        print() 
    else:                               # Zo niet, print melding en skip
        print("Geen Aces.") 
        print() 

    #                Twos              # 
    twos = dobbelsteen_waardes.count(2) # Check of er 2 in de waardes zit
    if twos >= 1:                       # Zo ja, voeg toe aan frequentie lijst en voeg toe aan mogelijke keuzes
        print("Twos mogelijk.") 
        totale_twos = twos * 2 
        print(f"Totale score van Twos is {totale_twos}.") 
        frequentie["Twos"] = twos 
        mogelijke_keuzes.append("TWOS") 
        print() 
    else: 
        print("Geen Twos.")             # Zo niet, print melding en skip
        print() 

    #               Threes               # 
    threes = dobbelsteen_waardes.count(3)   # Check of er 3 in de waardes zit
    if threes >= 1:                         # Zo ja, voeg toe aan frequentie lijst en voeg toe aan mogelijke keuzes
        print("Threes mogelijk.") 
        totale_threes = threes * 3 
        print(f"Totale score van Threes is {totale_threes}.") 
        frequentie["Threes"] = threes 
        mogelijke_keuzes.append("THREES") 
        print() 
    else: 
        print("Geen Threes.")               # Zo niet, print melding en skip
        print() 

    #               Fours                # 
    fours = dobbelsteen_waardes.count(4)    # Check of er 4 in de waardes zit
    if fours >= 1:                          # Zo ja, voeg toe aan frequentie lijst en voeg toe aan mogelijke keuzes
        print("Fours mogelijk.")
        totale_fours = fours * 4 
        print(f"Totale score van Fours is {totale_fours}.") 
        frequentie["Fours"] = fours 
        mogelijke_keuzes.append("FOURS") 
        print() 
    else: 
        print("Geen Fours.")                # Zo niet, print melding en skip
        print() 

    #               Fives               # 
    fives = dobbelsteen_waardes.count(5) # Check of er 5 in de waardes zit
    if fives >= 1:                       # Zo ja, voeg toe aan frequentie lijst en voeg toe aan mogelijke keuzes
        print("Fives mogelijk.") 
        totale_fives = fives * 5 
        print(f"Totale score van Fives is {totale_fives}") 
        frequentie["Fives"] = fives 
        mogelijke_keuzes.append("FIVES") 
        print() 
    else: 
        print("Geen Fives.")             # Zo niet, print melding en skip
        print() 

    #               Sixes               # 
    sixes = dobbelsteen_waardes.count(6) # Check of er 6 in de waardes zit
    if sixes >= 1:                       # Zo ja voeg toe aan frequentie lijst en voeg toe aan mogelijke keuzes
        print("Sixes mogelijk.") 
        totale_sixes = sixes * 6 
        print(f"Totale score van Sixes is {totale_sixes}.") 
        frequentie["Sixes"] = sixes 
        mogelijke_keuzes.append("SIXES") 
        print() 
    else: 
        print("Geen Sixes.")             # Zo niet, print melding en skip
        print() 

    ###             Speciale Cats             ### 

    aantallen = set(frequentie.values())        # Check waardes
    straten_aantallen = set(dobbelsteen_waardes) # Maak lijst van de waardes, en verwijder dubbele

    #            Three of a Kind             # 
    if 3 in aantallen:                          # Als er 3 dezelfde waardes zijn, mogelijk
        print("Three of a Kind mogelijk.") 
        ToaK_totaal = sum(dobbelsteen_waardes) 
        print(f"Totale score van Three of a Kind is {ToaK_totaal}.") 
        mogelijke_keuzes.append("THREE OF A KIND") 
        print() 
    else: 
        print("Geen Three of a Kind.")          # Anders niet
        print() 

    #           Four of a Kind               # 
    if 4 in aantallen: 
        print("Four of a Kind mogelijk.")       # Als er 4 dezelfe waardes zijn, mogelijk
        FoaK_totaal = sum(dobbelsteen_waardes) 
        print(f"Totale socre van Four of a Kind is {FoaK_totaal}.") 
        mogelijke_keuzes.append("FOUR OF A KIND") 
        print() 
    else: 
        print("Geen Four of a Kind.")           # Anders niet
        print() 

    #               Full House              # 
    if 2 in aantallen and 3 in aantallen:       # Als er 2 dezelfe en 3 dezelfde waarden zijn, mogelijk
        print("Full House mogelijk.") 
        print("Totale score van Full House is 25.") 
        mogelijke_keuzes.append("FULL HOUSE") 
        print() 
    else: 
        print("Geen Full House.")               # Anders niet
        print() 

    #               Small Straight  en Large Straight          # 
                        # Large Straight # 
    grote_straat_opties = [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}]    # De twee opties voor grote straat

    is_grote_straat = straten_aantallen in grote_straat_opties 

                        # Small Straight # 
    kleine_straat_opties = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]   # De 3 opties voor kleine straat

    # Controleert of er minimaal één van de mogelijke Small Straights aanwezig is in de gegooide dobbelstenen.
    # 'for optie in kleine_straat_opties' controleert elke mogelijke straat.
    # 'issubset()' controleert of alle getallen van die straat in straten_aantallen zitten.
    # 'any()' geeft True zodra één van de opties klopt. 
    is_kleine_straat = any(optie.issubset(straten_aantallen) for optie in kleine_straat_opties) 

    if is_grote_straat:                                         # Als grote straat mogelijk is is ook kleinde straat mogelijk, dus alle twee valide
        print("Large Straight en Small Straight mogelijk.") 
        print("Totale score van Large Straight is 40.") 
        print("Totale score van Small Straight is 30.") 
        mogelijke_keuzes.append("LARGE STRAIGHT") 
        mogelijke_keuzes.append("SMALL STRAIGHT") 
        print()     
    elif is_kleine_straat:                  # Kleinde straat mogelijk
        print("Small Straight mogelijk") 
        print("Totale score van Small Straight is 30.") 
        mogelijke_keuzes.append("SMALL STRAIGHT") 
        print() 
    else: 
        print("Geen Small of Large Straight.")  # Geen van beide
        print() 

    #               Top Score                   # 
    if 5 in aantallen:               # 5 dezelfe waardes betekent yathzee
        print("Top Score!") 
        print("Totale score van Top Score is 50.") 
        mogelijke_keuzes.append("TOP SCORE") 
        print() 
    else: 
        print("Geen Top Score.")     # Anders niet
        print() 

    #               Chance                      # 
    print("Chance is mogelijk.") 
    totaal_chance = sum(dobbelsteen_waardes) 
    print(f"Totale Score van Chance is {totaal_chance}.") 
    mogelijke_keuzes.append("CHANCE") 
    print()                           # Chance is altijd mogelijk, behalve als die al gekozen is.

    return mogelijke_keuzes, totale_aces, totale_twos, totale_threes, totale_fours, totale_fives, totale_sixes, ToaK_totaal, FoaK_totaal, totaal_chance     # Return de totale scores van elke categorie

def categorie_kiezen(dobbelstenen, scorekaart_data, mogelijke_keuzes, totale_aces, totale_twos, totale_threes, totale_fours, totale_fives, totale_sixes, ToaK_totaal, FoaK_totaal, totaal_chance):
    #                   Kiezen                     #
    print("Je mag nu kiezen welke categorie je wilt invullen, je mag alleen kiezen uit de categorieën die mogelijk zijn. Voer in de naam van de categorie, let op spelling.")
    while True:
        cat_keuze = input("Welke categorie wil je invullen? ").upper()  # Kies welke categorie je wil
        if cat_keuze in mogelijke_keuzes:
            cat_ingevuld = False            # Zolang je geen correcte keuze heb ingevult, doorvragen
            if cat_keuze == "ACES":         # Als de keuze ACES is, voeg die score toe aan scorekaart (etc bij de andere)
                if scorekaart_data["Aces"] is None:
                    print(f"Je hebt gekozen voor {cat_keuze}. De totale score hiervan is {totale_aces}.")
                    scorekaart_data["Aces"] = totale_aces
                    cat_ingevuld = True
                else:
                    print("Aces is al ingevuld.")
            elif cat_keuze == "TWOS":
                if scorekaart_data["Twos"] is None:
                    print(f"Je hebt gekozen voor {cat_keuze}. De totale score hiervan is {totale_twos}.")
                    scorekaart_data["Twos"] = totale_twos
                    cat_ingevuld = True
                else:
                    print("Twos is al ingevuld.")
            elif cat_keuze == "THREES":
                if scorekaart_data["Threes"] is None:
                    print(f"Je hebt gekozen voor {cat_keuze}. De totale score hiervan is {totale_threes}.")
                    scorekaart_data["Threes"] = totale_threes
                    cat_ingevuld = True
                else:
                    print("Threes is al ingevuld.")
            elif cat_keuze == "FOURS":
                if scorekaart_data["Fours"] is None:
                    print(f"Je hebt gekozen voor {cat_keuze}. De totale score hiervan is {totale_fours}.")
                    scorekaart_data["Fours"] = totale_fours
                    cat_ingevuld = True
                else:
                    print("Fours is al ingevuld.")
            elif cat_keuze == "FIVES":
                if scorekaart_data["Fives"] is None:
                    print(f"Je hebt gekozen voor {cat_keuze}. De totale score hiervan is {totale_fives}.")
                    scorekaart_data["Fives"] = totale_fives
                    cat_ingevuld = True
                else:
                    print("Fives is al ingevuld.")
            elif cat_keuze == "SIXES":
                if scorekaart_data["Sixes"] is None:
                    print(f"Je hebt gekozen voor {cat_keuze}. De totale score hiervan is {totale_sixes}.")
                    scorekaart_data["Sixes"] = totale_sixes
                    cat_ingevuld = True
                else:
                    print("Sixes is al ingevuld.")
            elif cat_keuze == "THREE OF A KIND":
                if scorekaart_data["Three of a Kind"] is None:
                    print(f"Je hebt gekozen voor {cat_keuze}. De totale score hiervan is {ToaK_totaal}.")
                    scorekaart_data["Three of a Kind"] = ToaK_totaal
                    cat_ingevuld = True
                else:
                    print("Three of a Kind is al ingevuld.")
            elif cat_keuze == "FOUR OF A KIND":
                if scorekaart_data["Four of a Kind"] is None:
                    print(f"Je hebt gekozen voor {cat_keuze}. De totale score hiervan is {FoaK_totaal}.")
                    scorekaart_data["Four of a Kind"] = FoaK_totaal
                    cat_ingevuld = True
                else:
                    print("Four of a Kind is al ingevuld.")
            elif cat_keuze == "FULL HOUSE":
                if scorekaart_data["Full House"] is None:
                    print(f"Je hebt gekozen voor {cat_keuze}. De totale score hiervan is 25.")
                    scorekaart_data["Full House"] = 25
                    cat_ingevuld = True
                else:
                    print("Full House is al ingevuld.")
            elif cat_keuze == "SMALL STRAIGHT":
                if scorekaart_data["Small Straight"] is None:
                    print(f"Je hebt gekozen voor {cat_keuze}. De totale score hiervan is 30.")
                    scorekaart_data["Small Straight"] = 30
                    cat_ingevuld = True
                else:
                    print("Small Straight is al ingevuld.")
            elif cat_keuze == "LARGE STRAIGHT":
                if scorekaart_data["Large Straight"] is None:
                    print(f"Je hebt gekozen voor {cat_keuze}. De totale score hiervan is 40.")
                    scorekaart_data["Large Straight"] = 40
                    cat_ingevuld = True
                else:
                    print("Large Straight is al ingevuld.")
            elif cat_keuze == "TOP SCORE":
                if scorekaart_data["Top Score"] is None:
                    print(f"Je hebt gekozen voor {cat_keuze}. De totale score hiervan is 50.")
                    scorekaart_data["Top Score"] = 50
                    cat_ingevuld = True
                else:
                    print("Top Score is al ingevuld.")
            elif cat_keuze == "CHANCE":
                if scorekaart_data["Chance"] is None:
                    print(f"Je hebt gekozen voor {cat_keuze}. De totale score hiervan is {totaal_chance}.")
                    scorekaart_data["Chance"] = totaal_chance
                    cat_ingevuld = True
                else:
                    print("Chance is al ingevuld.")
            if cat_ingevuld == True:
                break
            else:
                print("Niks ingevuld.")
        elif cat_keuze == "SKIP":
            print("Je skipt. Kies een categorie om 0 punten in te vullen.")
            # Schrap een categorie
            print(scorekaart_data)
            while True:
                nul_categorie = input("Welke categorie wil je schrappen? ")
                print(repr(nul_categorie))
                if nul_categorie in scorekaart_data and scorekaart_data[nul_categorie] is None:   # Als de categorie die je wilt schrappen None is, dan kan die worden gekozen, anders niet
                    scorekaart_data[nul_categorie] = 0
                    print(f"{nul_categorie} is ingevuld met 0 punten.")
                    return
                else:
                    print("Dat is geen mogelijke categorie. Hij is al ingevuld, of bestaat niet. Probeer opnieuw.")
        else:
            print("Dat is geen mogelijke categorie. Probeer opnieuw.")      # Andere keuze die niet bestaat

def totale_score(scorekaart):
    totaal_boven = scorekaart["Aces"] + scorekaart["Twos"] + scorekaart["Threes"] + scorekaart["Fours"] + scorekaart["Fives"] + scorekaart["Sixes"]

    if totaal_boven >= 63:
        totaal_boven = totaal_boven + 35        # +35 punten als je basis boventotaal 63 of hoger is
        print(f"De totale score van de bovenste vakken is {totaal_boven}.")
    else:
        print(f"De totale score van de bovenste vakken is {totaal_boven}.") # Totaal van boven

    totaal_onder = scorekaart["Three of a Kind"] + scorekaart["Four of a Kind"] + scorekaart["Full House"] + scorekaart["Small Straight"] + scorekaart["Large Straight"] + scorekaart["Top Score"] + scorekaart["Chance"]   # Totaal van onder

    print(f"De totale score van de onderste vakken is {totaal_onder}.")

    totale_score = totaal_boven + totaal_onder

    print(f"Jouw totale score is dus {totale_score}")

    return totale_score