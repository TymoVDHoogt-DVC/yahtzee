from functions import *

welkombijyathzee()

scorekaart_data = scorekaart()

scorekaart_check = scorekaart_checken(scorekaart_data)

if scorekaart_check == True:
    print("Beurt voorzetten")
else:
    print("Bereken totaalscore")

worp = 1

dobbelstenen = dobbelstenen_gooien()
print(dobbelstenen)

antwoord, behouden_dobbels, worp = nog_een_keer(worp, dobbelstenen)

while antwoord == "OPNIEUW":
    print(dobbelstenen)
    antwoord, behouden_dobbels, worp = nog_een_keer(worp, dobbelstenen)

if antwoord == "CATKIEZEN":
    categorie_kiezen(antwoord, dobbelstenen)

# print(antwoord)
# print(worp)