 # Główny plik gry

# from gra_poletko.rośliny import *
from gra_poletko.rośliny.marchew import Marchew
from gra_poletko.plansza.plansza import Plansza
from gra_poletko.sklep.sklep import Sklep


def ustaw_ceny_w_sklepie():
    ziarnaCeny = {
        "Marchew": Marchew.cenaWSklepie(),
        #"Ziemniak": Ziemniak.cenaWSklepie(),
    }
    skl.setZiarna(ziarnaCeny)

    # return "Ustaiwono ceny w sklepie"




if __name__ == "__main__":

    test = Marchew.cenaWSklepie()
    print(test)

    # mar = Marchew()
    # pla = Plansza(2)
    # ros = Roślina("Dąb")

    skl = Sklep()
    print(skl.getZiarna)
    ustaw_ceny_w_sklepie()
    print(skl.getZiarna)

    i=0
