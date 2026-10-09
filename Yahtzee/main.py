from functions import *

welkombijyathzee()

speleraantal = spelers_kiezen()         # Spelers kiezen
spellenaantal = aantal_spellen_kiezen() # Aantal spellen kiezen

scores_speler1 = [] # Lijst van de scores van speler 1
scores_speler2 = [] # Lijst van de scores van speler 2

for wedstrijd in range(spellenaantal):  # Speel aantal websites aan de hand an de keuze

    print(f"\n--- Wedstrijd {wedstrijd + 1} van {spellenaantal} ---")       # Welke wedstrijd?

    if speleraantal == 1:
        scorekaart_data = scorekaart(speleraantal)  # Scorekaart speler 1

    elif speleraantal == 2:
        scorekaart_data, scorekaart_data2 = scorekaart(speleraantal)    # Socrekaart speler 2

    speler_aan_de_beurt = 1     # Speler 1 begint

    while scorekaart_checken(scorekaart_data) or (speleraantal == 2 and scorekaart_checken(scorekaart_data2)):
        if speleraantal == 2:
            print(f"Speler {speler_aan_de_beurt} is aan de beurt.")     # Spler 2 aan de beurt

        if speleraantal == 2:
            if speler_aan_de_beurt == 1 and not scorekaart_checken(scorekaart_data):
                speler_aan_de_beurt = 2
                continue        # Kaart niet vol

            elif speler_aan_de_beurt == 2 and not scorekaart_checken(scorekaart_data2):
                speler_aan_de_beurt = 1
                continue

        worp = 1    # Begint al met 1 worp klaar 

        dobbelstenen = dobbelstenen_gooien()        # Dobbelstenen gooien

        antwoord, behouden_dobbels, worp = nog_een_keer(worp, dobbelstenen) # Nog een keer

        while antwoord == "OPNIEUW":
            antwoord, behouden_dobbels, worp = nog_een_keer(worp, dobbelstenen) # Als opnieuw, hergooien behalve behouden dobbels

        if antwoord == "CATKIEZEN":
            mogelijke_keuzes, totale_aces, totale_twos, totale_threes, totale_fours, totale_fives, totale_sixes, ToaK_totaal, FoaK_totaal, totaal_chance = categorie_mogelijkheden(dobbelstenen)    # Categorie kiezen

            if speler_aan_de_beurt == 1:
                categorie_kiezen(dobbelstenen, scorekaart_data, mogelijke_keuzes, totale_aces, totale_twos, totale_threes, totale_fours, totale_fives, totale_sixes, ToaK_totaal, FoaK_totaal, totaal_chance)   # Speler 1 scorekaart

            elif speler_aan_de_beurt == 2:
                categorie_kiezen(dobbelstenen, scorekaart_data2, mogelijke_keuzes, totale_aces, totale_twos, totale_threes, totale_fours, totale_fives, totale_sixes, ToaK_totaal, FoaK_totaal, totaal_chance)    # Speler 2 scorekaart

        if speleraantal == 2:
            if speler_aan_de_beurt == 1:
                speler_aan_de_beurt = 2     # Goede speler aan de beurt
            else:
                speler_aan_de_beurt = 1     # Goede speler aan de beurt

    if speleraantal == 2:
        totale_score_speler1 = totale_score(scorekaart_data)    # Totale score berekenen speler 1
        totale_score_speler2 = totale_score(scorekaart_data2)   # Totale score berekenen speler 2

        scores_speler1.append(totale_score_speler1)             # Socre in de lijst van wedstrijden zetten
        scores_speler2.append(totale_score_speler2)

        print(f"Speler 1 heeft {totale_score_speler1} punten.") # Totale score printen
        print(f"Speler 2 heeft {totale_score_speler2} punten.")

        if totale_score_speler1 > totale_score_speler2:
            print("Speler 1 wint deze wedstrijd!")      # Als speler 1 meer heeft, wint
        elif totale_score_speler2 > totale_score_speler1:
            print("Speler 2 wint deze wedstrijd!")      # Als speler 2 meer heeft, wint
        else:
            print("Deze wedstrijd is gelijkspel!")      # Anders gelijkspel

    elif speleraantal == 1:
        totale_score_speler1 = totale_score(scorekaart_data)

        scores_speler1.append(totale_score_speler1)

        print(f"Je hebt {totale_score_speler1} punten gehaald.")    # Score printen voor als je allen speelt

if speleraantal == 2:
    eindtotaal_speler1 = sum(scores_speler1)        # Eindsocre na 5 wedtrijden berekenen van beide spelers
    eindtotaal_speler2 = sum(scores_speler2)

    print("\n--- Eindresultaat ---")
    print(f"Speler 1 heeft in totaal {eindtotaal_speler1} punten.")     # Eindsocre na 5 wedtrijden printen van beide spelers    
    print(f"Speler 2 heeft in totaal {eindtotaal_speler2} punten.")

    if eindtotaal_speler1 > eindtotaal_speler2:
        print("Speler 1 heeft het spel gewonnen!")  # Speler 1 meer, wint
    elif eindtotaal_speler2 > eindtotaal_speler1:
        print("Speler 2 heeft het spel gewonnen!")  # Speler 2 meer, wint
    else:
        print("Het is gelijkspel!")
elif speleraantal == 1:
    eindtotaal_speler1 = sum(scores_speler1)

    print("\n--- Eindresultaat ---")
    print(f"Je hebt in totaal {eindtotaal_speler1} punten gehaald.")    # Eindscore van 5 wedstrijden alleen