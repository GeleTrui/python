# NOTE: eerst alles definen domme

def Boekie():
    print("Wil je een boek schrijven over je avonturen?")
    keuze11 == input("Y/N")
    if keuze11 == "Y":
        print("Je schrijft een heel mooi boek, het boek verdient genoeg om met pensioen te gaan. Je leeft nog lang en gelukkig")
        loopie()
    elif keuze11 == "N":
        print("Je vind het mooi geweest en wil dit gedeelte van je leven achterlaten")
        loopie()




def bijnaeinde():
    print("waar geef je het geld aan uit? A: een vliegticket naar nederland B: een bus naar nederland")
    keuze10 == input()
    if keuze10 == "A":
        print("Je hebt geen paspoort duh")
        badending()
    elif keuze10 == "B":
        print("Je neemt een lange busreis naar nederland toe, je komt aan en van de autoriteiten mag je inburgeren")
        Boekie()







def dinnerscene():
    print("Je schuift bij de oude dame aan om mee te eten, ze vraagt waar je vandaan komt")
    print("A: Vertel de waarheid dat je een vluchteling bent of B: Lieg en zeg daty je in het dorp hiernaast woont")
    keuze9 = input()
    if keuze9 == "A":
        print("Je vertelt de waarheid over wie je bent en waar je vandaan komt, je gaat met een slecht gevoel naar bed. blijkbaar was de oude dame een snitch en je hoort politiesirenes")
        badending()
    elif keuze9 == "B":
        print("Je liegt en zegt dat je uit het dorp hiernaast komt en dat je aardappelen kwam kopen. ze gelooft je. ze geeft je wat geld om terug te komen en een nieuw paar schoenen")
        bijnaeinde()


def badending():
    print("je bent opgepakt door de autoriteiten, game over")
    loopie()
def deadending():
    print("Je boot zink in de middelandse zee en je verdrinkt, GAME OVER")
    loopie()

def oudedame():
    print("Een oudere dame nodigt je uit om bij haar een hapje te eten, accepteer je haar aanbod? Y/N")
    keuze8 = input()
    if keuze8 == "Y":
        print("Je schuift bij haar aan tafel")
        dinnerscene()
    elif keuze8 == "N":
        print("dood ouleh")
        loopie()



def BrotherHelp():
    print("Je broer geeft je wat geld en een busticket naar de turkse grens")
    a = True
    nohelp()
    # NOTE: variable a is in dit geval geld

def auto():
    print("iemand ziet je een auto bekijken, hij zegt dat de auto van hem is")
    if a == True:
        print("A koop de auto van hem met het geld van je broer B vraag om een lift naar het dorp hiernaast")
        keuze7 = input()
        if keuze7 == "A":
            print("Je koopt de auto van hem en rijd er helemaal naar nederland mee")
            print("Je komt aan in nederland en begint met inburgeren, het is je gelukt om te ontsnappen")
            loopie()

            # NOTE: VERGEET NYET TE LOOPEN
        elif keuze7 == "B":
            print("Je vraagt hem om een lift naar het dorp hiernaast, hij zegt ja.")
            oudedame()

def loopie():
    print("Wil je nog een keer? ")
    keuze9 = input("Y/N")
    if keuze9 == "Y":
        begin()
    elif keuze9 == "N":
        print("Ok doei")






def nohelp():
    print("Je komt aan bij de grens van turkije, wat doe je nu?")
    print("A: Je loopt B: Je huurt een goedkope boot C: Je gaat op zoek naar een auto")
    keuze2 = input()
    if keuze2 == "A":
        print("je gaat te voet verder")
        lift()
    elif keuze2 == "B":
        print("Je huurt een goedkope boot")
        deadending()
    elif keuze2 == "C":
        print("Je gaat op speurtocht naar een auto die je misschien wil helpen om een lift kan vragen")
        auto()


def WithHelp():
    print("Van wie wil je hulp")
    print("A: van een smokkelaar B: van je broer")
    keuze3 = input()
    if keuze3 == "A":
        print("Je vraagt een smokkelaar om hulp")
        planeorboat()
    elif keuze3 == "B":
        print("Je vraagt je broer om hulp")
        BrotherHelp()

def planeorboat():
    print("Hij bied je een kueze aan tussen een vliegtuig en een boot")
    print("A voor het vliegtuig, B voor de boot")
    keuze4 = input()
    if keuze4 == "A":
        NoHelp()
    elif keuze4 == "B":
        print("Hier moet nog een def")


def liftyes():
    print("Je neemt de lift aan, maar nadat je in de auto stapt blijkt de bestuurder niet vriendelijk en eist hij je bezittingen, geef je die? Y/N")
    keuze6 = input()
    if keuze6 == "Y":
        print("je geeft hem alles")
        oudedame()
    elif keuze6 == "N":
        print("De man is hier niet blij mee en gooit je uit de auto, de val is je dood")
        # NOTE: HIER MOET NOG EEN GAMEOVER

def lift():
    print("Je loopt langs de weg en iemand bied je een lift aan. wat doe je?")
    print("A je neemt de lift aan B je neemt de lift niet aan")
    keuze5 = input()
    if keuze5 == "A":
        print("Je neemt de lift aan")
        liftyes()
    elif keuze5 == "B":
        print("Je neemt de lift niet aan")
        auto()
def begin():
    print("Je moet uit je land vluchten, wat doe je: A, Je vlugt niet, B, je vlucht zonder hulp C, je vlugt met hulp")
    keuze1 = input()
    if keuze1 == "A":
        print("Je vlucht niet")
        badending()
    elif keuze1 == "B":
        print("Je vlucht zonder hulp")
        nohelp()
    elif keuze1 == "C":
        WithHelp()

print("welkom bij dit spelletje, de keuzes die je maakt hebben effect op het einde dat je krijgt en de loop van je verhaal")
begin()
