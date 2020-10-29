import time

print("Welkom bij keuzes maken")
time.sleep(0.5)
print("je wordt wakker, snooze je de wekker?")
keuze = input("Y/N ")
if keuze == "Y":
    print("Ok lekker tukkie")
elif keuze == "N":
    print("Je gaat er lekker uit")
else:
    print ("Je hebt niks ingevuld, de keuze is dus automatisch Nee")
time.sleep(0.5)
print("Eet je muesli of brood")
keuze = input("meusli of brood ")
if keuze == "meusli":
    print("Ok lekker meusli hmmm")
elif keuze == "brood":
    print("hmmmm lekker broodje pindakaas")
else:
    print ("Je hebt niks ingevuld, de keuze is dus automatisch meusli")
time.sleep(0.5)
print("Doe je je rode of gele schoenen aan")
keuze = input("rood of geel ")
if keuze == "rood":
    print("Ok ziet er blits uit man")
elif keuze == "geel":
    print("damn son you lookin fresh")
else:
    print ("Je hebt niks ingevuld, de keuze is dus automatisch rood")
time.sleep(0.5)
print("Neem je de fiets of de auto")
keuze = input("fiets of auto ")
if keuze == "fiets":
    print("Ok lekker trappen")
elif keuze == "auto":
    print("Vroem vroem snel op school")
else:
    print ("je gaat lekker met de fiets")
time.sleep(0.5)
print("Ga je opletten in de les of niet")
keuze = input("Y/N ")
if keuze == "Y":
    print("je doet goed mee en haalt 10en")
elif keuze == "N":
    print("Je gaat maar lekker slapen en haalt 3en")
else:
    print ("Je hebt niks ingevuld, de keuze is dus automatisch Nee, ga maar lekker een 1 halen")
