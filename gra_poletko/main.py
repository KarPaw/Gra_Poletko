 # Główny plik gry

from gra_poletko.rośliny.marchew import Marchew
from gra_poletko.plansza.plansza import Plansza
from gra_poletko.sklep.sklep import Sklep
from gra_poletko.rolnik.rolnik import Rolnik


def ustaw_ceny_w_sklepie():
    ziarnaCeny = {
        "Marchew": Marchew.cenaWSklepie(),
        #"Ziemniak": Ziemniak.cenaWSklepie(),
    }
    skl.setZiarna(ziarnaCeny)

    # return "Ustaiwono ceny w sklepie"

def pustee():
    ...



if __name__ == "__main__":

    test = Marchew.cenaWSklepie()

    # mar = Marchew()
    # pla = Plansza(2)
    # ros = Roślina("Dąb")
    rol = Rolnik()
    skl = Sklep()
    ustaw_ceny_w_sklepie()
    # print(skl.getZiarna)

    rol.pokazStan()
    rol.zakupy(skl)
    rol.pokazStan()


    i=0
