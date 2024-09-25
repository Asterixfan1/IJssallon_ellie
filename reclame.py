from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f'''Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro.'''
    smaak = "aardbei"
    prijs = 4
    korting = 0.1
    return uitvoer

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag
        btw_bedrag = totaal * btw
    uitvoer = f'''Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden.'''
    return uitvoer

inkomsten = inkomsten_totaal([10,5,3,2,1,2,9], 0.21)

def laag_en_hoog(mijn_lijst):
    uitvoer = max(mijn_lijst), min(mijn_lijst)
    return uitvoer

mijn_lijst = laag_en_hoog([9,5,7,1,2,3,6])                

def gemiddelde(mijn_lijst, bedrag):
    bedrag += mijn_lijst
    bedrag /= 7
    uitvoer = f'''De gemiddelde inkomsten deze week zijn {bedrag} euro.'''
    return uitvoer

mijn_lijst = gemiddelde([7,5,3,9,4,6,7])

def meervoudig(invoer_lijst):
    invoer_lijst = laag_en_hoog
    return max(invoer_lijst), min(invoer_lijst)

def combinatie(invoer_lijst2):
    invoer_lijst2 = meervoudig
    return invoer_lijst2

korte_lijst = combinatie

mijn_functie_2 = combinatie