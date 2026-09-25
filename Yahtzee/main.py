from functions import *

welkombijyathzee()

scorekaart_data = scorekaart()

scorekaart_check = scorekaart_checken(scorekaart_data)

if scorekaart_check == True:
    print("Beurt voorzetten")
else:
    print("Bereken totaalscore")

worp = dobbelstenen_gooien()

print(worp)

antwoord = nog_een_keer()
print(antwoord)

dobbelstenen = nog_een_keer()