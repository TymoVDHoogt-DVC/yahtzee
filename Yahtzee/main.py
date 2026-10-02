from functions import *

welkombijyathzee()

speleraantal = spelers_kiezen()
# spellenaantal = aantal_spellen_kiezen()

if speleraantal == 1:
    scorekaart_data = scorekaart(speleraantal)

elif speleraantal == 2:
    scorekaart_data, scorekaart_data2 = scorekaart(speleraantal)

scorekaart_check = scorekaart_checken(scorekaart_data)

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

elif speleraantal == 1:
    totale_score_speler1 = totale_score(scorekaart_data)

if speleraantal == 2:
    if totale_score_speler1 > totale_score_speler2:
        print("Speler 1 heeft gewonnen!")
    elif totale_score_speler2 > totale_score_speler1:
        print("Speler 2 heeft gewonnen!")
    else:
        print("Het is gelijkspel!")