import time, random

def welkombijyathzee():
    print("Welkom bij Yathzee!")

def scorekaart():
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
    return scorekaart

def scorekaart_checken(scorekaart):
    res = any(waarde is None for waarde in scorekaart.values())
    if res == True:
        print("placeholder")
    else:
        print("Totaal score berekenen")
    return res

def dobbelstenen_gooien():
    dobbelstenen = {
    "Dobbelsteen 1": 0,
    "Dobbelsteen 2": 0,
    "Dobbelsteen 3": 0,
    "Dobbelsteen 4": 0,
    "Dobbelsteen 5": 0
    }

    print("We gaan nu gooien...")
    totale_score = 0
    time.sleep(2)

    for dobbelsteen in dobbelstenen.keys():
        gooi = random.randint(1, 6)
        dobbelstenen[dobbelsteen] = gooi
        print(f"{dobbelsteen} heeft een {gooi} gegooid.")
        totale_score += gooi
    print(f" Totale waarde van deze beurt: {totale_score}")
    return dobbelstenen

def nog_een_keer(worp, dobbelstenen):
    behouden_dobbels = []

    if worp == 3:
        print("Je moet nu een categorie kiezen.")
        behouden_dobbels = list(dobbelstenen.keys())
        return "CATKIEZEN", behouden_dobbels, worp

    opnieuw_catkiezen = input("Wil je opnieuw gooien of een categorie kiezen? (OPNIEUW/CATKIEZEN) ").upper()
    if opnieuw_catkiezen == "OPNIEUW":
        worp += 1
        aantal_keuzes = 0
        while aantal_keuzes < 5:
            dobbel_houden = input("Welke dobbelsteen/stenen wilt u houden? (1-5/GEEN) ").upper()
            if dobbel_houden == "1":
                if "Dobbelsteen 1" in behouden_dobbels:
                    print("Deze dobbelsteen is al gekozen.")
                else:
                    behouden_dobbels.append("Dobbelsteen 1")
                    aantal_keuzes += 1
            elif dobbel_houden == "2":
                if "Dobbelsteen 2" in behouden_dobbels:
                    print("Deze dobbelsteen is al gekozen")
                else:
                    behouden_dobbels.append("Dobbelsteen 2")
                    aantal_keuzes += 1
            elif dobbel_houden == "3":
                if "Dobbelsteen 3" in behouden_dobbels:
                    print("Deze dobbelsteen is al gekozen.")
                else:
                    behouden_dobbels.append("Dobbelsteen 3")
                    aantal_keuzes += 1
            elif dobbel_houden == "4":
                if "Dobbelsteen 4" in behouden_dobbels:
                    print("Deze dobbelsteen is al gekozen.")
                else:
                    behouden_dobbels.append("Dobbelsteen 4")
                    aantal_keuzes += 1
            elif dobbel_houden == "5":
                if "Dobbelsteen 5" in behouden_dobbels:
                    print("Deze dobbelsteen is al gekozen.")
                else:
                    behouden_dobbels.append("Dobbelsteen 5")
                    aantal_keuzes += 1
            elif dobbel_houden == "GEEN":
                aantal_keuzes += 1
            else:
                print("Sorry, dat is geen geldig nummer.")
        for dobbelsteen in dobbelstenen:
            if dobbelsteen in behouden_dobbels:
                print
            else:
                print()
                dobbelstenen[dobbelsteen] = random.randint(1, 6)
    elif opnieuw_catkiezen == "CATKIEZEN":
        print("Categorie kiezen")
    return opnieuw_catkiezen, behouden_dobbels, worp

def categorie_kiezen(antwoord, dobbelstenen):
    if antwoord == "CATKIEZEN":
        dobbelsteen_waardes = list(dobbelstenen.values())
        print(dobbelsteen_waardes)
        frequentie = {
            "Ones": 0,
            "Twos": 0,
            "Threes": 0,
            "Fours": 0,
            "Fives": 0,
            "Sixes": 0
        }
        #               Aces               #
        aces = dobbelsteen_waardes.count(1)
        if aces >= 1:
            print("Aces mogelijk")
            totale_aces = aces * 1
            print(f"Totale score in Aces is {totale_aces}.")
            frequentie["Ones"] = aces
        else:
            print("Geen aces.")
        #                Twos              #
        twos = dobbelsteen_waardes.count(2)
        if twos >= 1:
            print("Twos mogelijk")
            totale_twos = twos * 2
            print(f"Totale score in Twos is {totale_twos}.")
            frequentie["Twos"] = twos
        else:
            print("Geen twos.")
        #               Threes               #
        threes = dobbelsteen_waardes.count(3)
        if threes >= 1:
            print("Threes mogelijk")
            totale_threes = threes * 3
            print(f"Totale score in Threes is {totale_threes}.")
            frequentie["Threes"] = threes
        else:
            print("Geen threes.")
        #               Fours                #
        fours = dobbelsteen_waardes.count(4)
        if fours >= 1:
            print("Fours mogelijk")
            totale_fours = fours * 4
            print(f"Totale score in Fours is {totale_fours}.")
            frequentie["Fours"] = fours
        else:
            print("Geen fours.")
        #               Fives               #
        fives = dobbelsteen_waardes.count(5)
        if fives >= 1:
            print("Fives mogelijk")
            totale_fives = fives * 5
            print(f"Totale score in Fives is {totale_fives}")
            frequentie["Fives"] = fives
        else:
            print("Geen fives.")
        #               Sixes               #
        sixes = dobbelsteen_waardes.count(6)
        if sixes >= 1:
            print("Sixes mogelijk")
            totale_sixes = sixes * 6
            print(f"Totale score in Sixes is {totale_sixes}.")
            frequentie["Sixes"] = sixes
        else:
            print("Geen sixes")

        ###             Speciale Cats             ###

        aantallen = set(frequentie.values())
        straten_aantallen = {cijfer for cijfer, aantal in frequentie.items() if aantal > 0}
        #            Three of a Kind             #
        if 3 in aantallen:
            print("Three of a Kind mogelijk")
            ToaK_totaal = aces + twos + threes + fours + fives + sixes
            print(f"Totale score van Three of a Kind is {ToaK_totaal}.")

        #           Four of a Kind               #
        if 4 in aantallen:
            print("Four of a Kind mogelijk")
            FoaK_totaal = aces + twos + threes + fours + fives + sixes
            print(f"Totale socre van Four of a Kind is {FoaK_totaal}.")

        #               Full House              #
        if 2 in aantallen and 3 in aantallen:
            print("Full House mogelijk")
            print("Totale score van Full House is 25.")
        else:
            print("Geen Full House.")

        #               Small Straight  en Large Straight          #
                            # Large Straight #
        grote_straat_opties = [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}]

        is_grote_straat = straten_aantallen in grote_straat_opties
                            # Small Straight #
        kleine_straat_opties = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]

        # Welke volgorde dan ook, hij kan checken
        is_kleine_straat = any(optie.issubset(straten_aantallen) for optie in kleine_straat_opties)


        # Straat gooien
        if is_grote_straat:
            print("Large Straight en Small Straight mogelijk")
            print("Totale score van Large Straight is 40.")
            print("Totale score van Small Straight is 30.")
        elif is_kleine_straat:
            print("Small Straight mogelijk")
            print("Totale score van Small Straight is 30.")
        else:
            print("Geen Straights.")

        #               Top Score                   #
        if 5 in aantallen:
            print("Top Score!")
            print("Totale score van Top Score is 50.")

        print(frequentie)
    else:
        print
