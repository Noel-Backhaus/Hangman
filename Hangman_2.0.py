# Ersteller: Noel Backhaus

from random import randint
from turtle import *
import turtle

# Variablen

sprache = ""
modus = ""
wort = ""
eingabe = ""
ratebuchstabe = ""
kleinbuchstabe = " "
grossbuchstabe = " "
ratewort = ""
geheimwort = ""
buchstabenliste = ""
galgenindex = 0
galgenkontrolle = False
galgenstand = ""
spielen = True

# Unterprogramme

def spracheauswaehlen():
    global sprache
    
    # Eingabe
    print("")
    sprache = input("Englisch oder Deutsch? Bitte wählen Sie eine Sprache: ")

    # Plausibilitätskontrolle
    sprache = sprache.lower()
    optionen = ["english", "englisch", "german", "deutsch", "de", "en"]
    while not sprache in optionen:
        print("")
        sprache = input("Ungültige Eingabe. Bitte geben Sie Englisch oder Deutsch ein: ")
        sprache = sprache.lower()
    if sprache == "english" or sprache == "englisch" or sprache == "en":
        sprache = "englisch"
    elif sprache == "german" or sprache == "deutsch" or sprache == "de":
        sprache = "deutsch"

def modusauswaehlen():
    global modus

    # Eingabe
    print("")
    modus = input("1- oder 2-Spielermodus? Bitte geben Sie 1 oder 2 ein: ")

    # Plausibilitätskontrolle
    while modus != "1" and modus != "2":
        print("")
        modus = input("Ungültige Eingabe. Bitte geben Sie 1 oder 2 ein: ")

def wortauswaehlen():
    global wort
    
    # Modus überprüfen
    if modus == "1":
        # deutsches Wort
        if sprache == "deutsch":
            # Zufallsgenerator
            x = randint(1, 239650)
            # Liste auslesen
            with open("deutsch_wortliste.txt", "r") as wortliste:
                for i, zeile in enumerate(wortliste):
                    if i+1 == x:
                        wort = zeile
            # Sonderzeichen ersetzen
            sonderzeichen = ["ÃŸ", "Ã„", "Ã–", "Ãœ", "Ã¤", "Ã¶", "Ã¼"]        #(Umlaute: ß,Ä,Ö,Ü,ä,ö,ü)
            buchstaben = ["ss", "Ae", "Oe", "Ue", "ae", "oe", "ue"]
            for x in range(len(sonderzeichen)):
                wort = wort.replace(sonderzeichen[x], buchstaben[x])
        # englisches Wort
        if sprache == "englisch":
            #Zufallsgenerator
            x = randint(53, 354297)
            #Liste auslesen
            with open("englisch_wortliste.txt", "r") as wortliste:
                for i, zeile in enumerate(wortliste):
                    if i+1 == x:
                        wort = zeile     
        # Leerstellen entfernen
        wort = wort.strip()

def worteingeben():
    global wort
    korrekt = False

    # Modus überprüfen
    if modus == "2":
        # Eingabe des Wortes
        print("")
        wort = input("Bitte geben Sie das gewünschte Wort ein: ")
        # Leerstellen entfernen
        wort = wort.strip()
        
        # Plausibilitätskontrolle
        sonderzeichen = [223, 196, 214, 220, 228, 246, 252]
        while korrekt == False:
            for i in wort:
                x = ord(i)
                if (x >= 65 and x <= 90) or (x >= 97 and x <= 122) or x in sonderzeichen:
                    korrekt = True
                    continue
                else:
                    korrekt = False
                    break
            if korrekt == False:
                print("")
                wort = input("Ungültige Eingabe. Bitte geben Sie ein Wort ein: ")
                # Leerstellen entfernen
                wort = wort.strip()
                
        # Sonderzeichen ersetzen
        sonderzeichen = ["ß", "Ä", "Ö", "Ü", "ä", "ö", "ü"]
        buchstaben = ["ss", "Ae", "Oe", "Ue", "ae", "oe", "ue"]
        for x in range(len(sonderzeichen)):
            wort = wort.replace(sonderzeichen[x], buchstaben[x])

def verschluesseln():
    global geheimwort
    for i in wort:
        geheimwort += "*"

def raten():
    global eingabe
    global ratebuchstabe
    global ratewort
    korrekt = False

    # Eingabe
    eingabe = input("Raten Sie einen Buchstaben oder ein Wort: ")

    # Plausibilitätskontrolle
    while korrekt == False:
        for i in eingabe:
            x = ord(i)
            if (x >= 65 and x <= 90) or (x >= 97 and x <= 122):
                korrekt = True
                continue
            else:
                korrekt = False
                break
        if korrekt == False:
            print("")
            eingabe = input("Ungültige Eingabe. Bitte geben Sie einen Buchstaben oder ein Wort ein: ")

    # Unterscheidung zwischen Wort und Buchstabe
    if len(eingabe) > 1:
        ratewort = eingabe
    if len(eingabe) == 1:
        ratebuchstabe = eingabe   
     
def buchstabeauswerten():
    global kleinbuchstabe
    global grossbuchstabe
    global buchstabenliste
    global galgenindex
    global galgenkontrolle

    # Kontrolle zur Ausführung der Funktion
    if ratebuchstabe == eingabe:
        # Überprüfung ob Buchstabe schon geraten wurde
        if ratebuchstabe.upper() in buchstabenliste:
            print("")
            print("Der Buchstabe", ratebuchstabe, "wurde schon geraten!")
            galgenkontrolle = False
        else:
            # Umwandlung in Klein- oder Großbuchstabe
            kleinbuchstabe = " "
            grossbuchstabe = " "
            kleinbuchstabe = ratebuchstabe.lower()
            grossbuchstabe = ratebuchstabe.upper()
            # Überprüfung des Buchstabens
            if kleinbuchstabe in wort or grossbuchstabe in wort:
                print("")
                print("Gratulation! Der Buchstabe", ratebuchstabe, "ist richtig!")
                galgenkontrolle = False
            else:
                print("")
                print("Der Buchstabe", ratebuchstabe, "ist falsch!")
                galgenindex += 1
                galgenkontrolle = True
                
            buchstabenliste += grossbuchstabe
            buchstabenliste += kleinbuchstabe
            buchstabenliste += " "
            
def alphabetisieren():
    global buchstabenliste
    
    hilfsliste = []
    hilfsliste = buchstabenliste.split()
    hilfsliste.sort()
    buchstabenliste = " ".join(hilfsliste)
    buchstabenliste += " "

def alphabetisieren1():
    global buchstabenliste

    hilfsliste = ""
    i = 0
    while i <= 26:
        
        x = x.upper()
        index = (ord(x) - 65) * 3
        if i == index:
            hilfsliste += x
            hilfsliste += x.lower()
            hilfsliste += " "
        else:
            hilfsliste += " " * 3
    i += 1

def alphabetisieren2():
    global buchstabenliste
    hilfsliste = ""

    # Aktualisierung des aktuellen Stands vom Wort
    x = 0
    y = 0
    for i in buchstabenliste:
        
        if i == kleinbuchstabe:
            hilfsliste += kleinbuchstabe
        elif i == grossbuchstabe:
            hilfsliste += grossbuchstabe
        else:
            hilfsliste += buchstabenliste[x]
            hilfsliste += buchstabenliste[x + 1]
            hilfsliste += buchstabenliste[x + 2]
        x += 3
    buchstabenliste = hilfsliste
                
    
def wortauswerten():
    global geheimwort
    global galgenindex
    global galgenkontrolle

    # Kontrolle zur Ausführung der Funktion
    if ratewort == eingabe:
        # Überprüfung des Wortes
        if ratewort == wort:
            print("")
            print("Das Wort", ratewort, "ist richtig! Sie haben gewonnen!")
            geheimwort = wort
            galgenkontrolle = False
        else:
            print("")
            print("Das Wort", ratewort, "ist falsch. Das können Sie besser!")
            galgenindex += 1
            galgenkontrolle = True

def entschluesseln():
    global geheimwort
    hilfswort = ""

    # Kontrolle zur Ausführung der Funktion
    if eingabe == ratebuchstabe:
        # Aktualisierung des aktuellen Stands vom Wort
        x = 0
        for i in wort:
            if i == kleinbuchstabe:
                hilfswort += kleinbuchstabe
            elif i == grossbuchstabe:
                hilfswort += grossbuchstabe
            else:
                hilfswort += geheimwort[x]
            x += 1
        geheimwort = hilfswort

    # Kontrolle des Spielendes
    if geheimwort == wort:
        print("")
        print("Sie haben's geschafft! Sie haben alle Buchstaben erraten!")

def screen():
    global s
    global t
    s = turtle.getscreen()
    t = turtle.Turtle()
    turtle.hideturtle()

def screenleeren():
    global s
    global t
    t.clear()
    t.reset()
    t.hideturtle()

def galgen():
    global galgenstand
    fertigergalgen = ["Hügel", "Längsbalken", "Querbalken", "Stützbalken", "Strick", "Kopf", "Oberkörper", "linker Arm", "rechter Arm", "linkes Bein", "rechtes Bein"]
    unfertigergalgen = []

    # Kontrolle zur Ausführung der Funktion
    if galgenkontrolle == True:
        # Speicherung des Galgens
        for i in range(galgenindex):
            unfertigergalgen.append(fertigergalgen[i])
        galgenstand = unfertigergalgen[i]

    # Kontrolle des Spielendes
    if unfertigergalgen == fertigergalgen:
        galgenstand = "fertig"
        print("")
        print("Der Galgen ist fertig. Sie haben verloren... ")
        print("")
        print("Das Wort war:", wort)

def rueckmelden():
    if ratewort == wort or geheimwort == wort or galgenstand == "fertig":
        print("")
        print("Das ist Ihr finaler Stand: ")
    else:
        print("")
        print("Das ist Ihr aktueller Stand: ")
    print("")
    print("Wort:", geheimwort)
    print("")
    print("Galgen:", galgenstand)
    print("")
    print("Buchstaben: ", buchstabenliste)
    print("")

def wiederholen():
    global spielen

    # Eingabe
    abfrage = input("Wollen Sie nochmal spielen? ")
    abfrage = abfrage.lower()
    
    # Plausibilitätskontrolle
    while abfrage != "ja" and abfrage != "nein":
        print("")
        abfrage = input("Ungültige Eingabe. Bitte geben Sie ja oder nein ein: ")
        abfrage = abfrage.lower()

    # Festlegung
    if abfrage == "ja":
        spielen = True
        leeren(100)
        zuruecksetzen()
    elif abfrage == "nein":
        zuruecksetzen()
        spielen = False

def zuruecksetzen():
    global sprache
    global modus
    global wort
    global eingabe
    global ratebuchstabe
    global kleinbuchstabe
    global grossbuchstabe
    global ratewort
    global geheimwort
    global buchstabenliste
    global galgenindex
    global galgenkontrolle
    global galgenstand
    global spielen

    sprache = ""
    modus = ""
    wort = ""
    eingabe = ""
    ratebuchstabe = ""
    kleinbuchstabe = " "
    grossbuchstabe = " "
    ratewort = ""
    geheimwort = ""
    buchstabenliste = ""
    galgenindex = 0
    galgenkontrolle = False
    galgenstand = ""
    spielen = True

def leeren(laenge):
    for i in range(laenge):
        print("")

        
# Hauptprogramm

while spielen == True:
    # Vorbereitung
    #screen()
    #screenleeren()
    spracheauswaehlen()
    modusauswaehlen()
    wortauswaehlen()
    worteingeben()
    verschluesseln()
    leeren(200)
    print("Los geht's!")
    rueckmelden()
    # Spielstart
    while ratewort != wort and geheimwort != wort and galgenstand != "fertig":
        raten()
        leeren(100)
        buchstabeauswerten()
        alphabetisieren()
        entschluesseln()
        wortauswerten()
        galgen()
        rueckmelden()
    wiederholen()
    
