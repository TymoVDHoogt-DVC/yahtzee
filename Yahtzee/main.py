from functions import *

welkombijyathzee()

scorekaart_data = scorekaart()

scorekaart_check = scorekaart_checken(scorekaart_data)

while scorekaart_checken(scorekaart_data):
    worp = 1

    dobbelstenen = dobbelstenen_gooien()
    # print(dobbelstenen)

    antwoord, behouden_dobbels, worp = nog_een_keer(worp, dobbelstenen)

    while antwoord == "OPNIEUW":
        # print(dobbelstenen)
        antwoord, behouden_dobbels, worp = nog_een_keer(worp, dobbelstenen)

    if antwoord == "CATKIEZEN":
        categorie_kiezen(antwoord, dobbelstenen, scorekaart_data)

# print(antwoord)
# print(worp)