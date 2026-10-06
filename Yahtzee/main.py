from functions import *

welkombijyathzee()

speleraantal = spelers_kiezen()
spellenaantal = aantal_spellen_kiezen()

scores_speler1 = []
scores_speler2 = []

for wedstrijd in range(spellenaantal):

    print(f"\n--- Wedstrijd {wedstrijd + 1} van {spellenaantal} ---")

    if speleraantal == 1:
        scorekaart_data = scorekaart(speleraantal)

    elif speleraantal == 2:
        scorekaart_data, scorekaart_data2 = scorekaart(speleraantal)

    speler_aan_de_beurt = 1

    while scorekaart_checken(scorekaart_data) or (speleraantal == 2 and scorekaart_checken(scorekaart_data2)):
        if speleraantal == 2:
            print(f"Speler {speler_aan_de_beurt} is aan de beurt.")

        if speleraantal == 2:
            if speler_aan_de_beurt == 1 and not scorekaart_checken(scorekaart_data):
                speler_aan_de_beurt = 2
                continue

            elif speler_aan_de_beurt == 2 and not scorekaart_checken(scorekaart_data2):
                speler_aan_de_beurt = 1
                continue

        worp = 1

        dobbelstenen = dobbelstenen_gooien()

        antwoord, behouden_dobbels, worp = nog_een_keer(worp, dobbelstenen)

        while antwoord == "OPNIEUW":
            antwoord, behouden_dobbels, worp = nog_een_keer(worp, dobbelstenen)

        if antwoord == "CATKIEZEN":
            mogelijke_keuzes, totale_aces, totale_twos, totale_threes, totale_fours, totale_fives, totale_sixes, ToaK_totaal, FoaK_totaal, totaal_chance = categorie_mogelijkheden(dobbelstenen)

            if speler_aan_de_beurt == 1:
                categorie_kiezen(dobbelstenen, scorekaart_data, mogelijke_keuzes, totale_aces, totale_twos, totale_threes, totale_fours, totale_fives, totale_sixes, ToaK_totaal, FoaK_totaal, totaal_chance)

            elif speler_aan_de_beurt == 2:
                categorie_kiezen(dobbelstenen, scorekaart_data2, mogelijke_keuzes, totale_aces, totale_twos, totale_threes, totale_fours, totale_fives, totale_sixes, ToaK_totaal, FoaK_totaal, totaal_chance)

        if speleraantal == 2:
            if speler_aan_de_beurt == 1:
                speler_aan_de_beurt = 2
            else:
                speler_aan_de_beurt = 1

    if speleraantal == 2:
        totale_score_speler1 = totale_score(scorekaart_data)
        totale_score_speler2 = totale_score(scorekaart_data2)

        scores_speler1.append(totale_score_speler1)
        scores_speler2.append(totale_score_speler2)

        print(f"Speler 1 heeft {totale_score_speler1} punten.")
        print(f"Speler 2 heeft {totale_score_speler2} punten.")

        if totale_score_speler1 > totale_score_speler2:
            print("Speler 1 wint deze wedstrijd!")
        elif totale_score_speler2 > totale_score_speler1:
            print("Speler 2 wint deze wedstrijd!")
        else:
            print("Deze wedstrijd is gelijkspel!")

    elif speleraantal == 1:
        totale_score_speler1 = totale_score(scorekaart_data)

        scores_speler1.append(totale_score_speler1)

        print(f"Je hebt {totale_score_speler1} punten gehaald.")

if speleraantal == 2:
    eindtotaal_speler1 = sum(scores_speler1)
    eindtotaal_speler2 = sum(scores_speler2)

    print("\n--- Eindresultaat ---")
    print(f"Speler 1 heeft in totaal {eindtotaal_speler1} punten.")
    print(f"Speler 2 heeft in totaal {eindtotaal_speler2} punten.")

    if eindtotaal_speler1 > eindtotaal_speler2:
        print("Speler 1 heeft het spel gewonnen!")
    elif eindtotaal_speler2 > eindtotaal_speler1:
        print("Speler 2 heeft het spel gewonnen!")
    else:
        print("Het is gelijkspel!")
elif speleraantal == 1:
    eindtotaal_speler1 = sum(scores_speler1)

    print("\n--- Eindresultaat ---")
    print(f"Je hebt in totaal {eindtotaal_speler1} punten gehaald.")