from functions import *

welkombijyathzee()

scorekaart_data = scorekaart()

scorekaart_check = scorekaart_checken(scorekaart_data)

while scorekaart_checken(scorekaart_data):
    worp = 1

    dobbelstenen = dobbelstenen_gooien()

    antwoord, behouden_dobbels, worp = nog_een_keer(worp, dobbelstenen)

    while antwoord == "OPNIEUW":
        antwoord, behouden_dobbels, worp = nog_een_keer(worp, dobbelstenen)

    if antwoord == "CATKIEZEN":
        mogelijke_keuzes, totale_aces, totale_twos, totale_threes, totale_fours, totale_fives, totale_sixes, ToaK_totaal, FoaK_totaal, totaal_chance = categorie_mogelijkheden(dobbelstenen)
        categorie_kiezen(dobbelstenen, scorekaart_data, mogelijke_keuzes, totale_aces, totale_twos, totale_threes, totale_fours, totale_fives, totale_sixes, ToaK_totaal, FoaK_totaal, totaal_chance)

totale_score()