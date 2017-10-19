# Schrijf onderstaande functies.
# Elke functie heeft één parameter van het datatype String.
# - Functie ‘tel_cijfers’: geeft het aantal cijfers uit de string terug
# - Functie ‘tel_kleine_letters’: geeft het aantal kleine letters terug
# - Functie ‘tel_hoofdletters’: geeft het aantal hoofdletters terug.

zin = ("HELLO world! 123")
print("De onderzochte string is \"{0}\"".format(zin))

def tel_cijfer(string):
    count = 0
    for zin in range(len(string)):
        if string[zin].isdigit():
            count += 1
    return count
print("Het aantal cijfers in deze zin is: {0}".format(tel_cijfer(zin)))

def tel_kleine_letters(string):
    count = 0
    for zin in range(len(string)):
        if string[zin].islower():
            count += 1
    return count
print("Het aantal kleine letters in deze zin is: {0}".format(tel_kleine_letters(zin)))

def tel_hoofdletters(string):
    count = 0
    for zin in range(len(string)):
        if string[zin].isupper():
            count += 1
    return count
print("Het aantal hoofletters in deze zin is: {0}".format(tel_hoofdletters(zin)))