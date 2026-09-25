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

def nog_een_keer(dobbelstenen):
    behouden_dobbels = []
    opnieuw_catkiezen = input("Wil je opnieuw gooien of een categorie kiezen? (OPNIEUW/CATKIEZEN) ").upper()
    if opnieuw_catkiezen == "OPNIEUW":
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
                print
    elif opnieuw_catkiezen == "CATKIEZEN":
        print("Categorie kiezen")
    return opnieuw_catkiezen, behouden_dobbels