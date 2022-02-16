# Główny plik gry

from gra_poletko.rośliny.marchew import Marchew
from gra_poletko.plansza.plansza import Plansza
from gra_poletko.sklep.sklep import Sklep
from gra_poletko.rolnik.rolnik import Rolnik


def ustaw_ceny_w_sklepie(sklep):
    ziarnaCeny = {
        "Marchew": Marchew.cenaWSklepie(),
        # "Ziemniak": Ziemniak.cenaWSklepie(),
    }
    sklep.setZiarna(ziarnaCeny)

    # return "Ustaiwono ceny w sklepie"

def pustee():
    ...



if __name__ == "__main__":

    # test = Marchew.cenaWSklepie()

    rol = Rolnik(Plansza(10))

    def test_siania_marchwi():

        mar = Marchew()
        # plansza.zasiej(mar, 1)

        rol.zasiew()

    # test_siania_marchwi()

    def test_sklepu():
        skl = Sklep()
        ustaw_ceny_w_sklepie(skl)
        rol.pokazStan()
        rol.zakupy(skl)
        rol.pokazStan()

    test_sklepu()

    def slownik_z_obiektem():

        m1 = Marchew()
        s = {
            m1: 1,
            "poz. 2.": 3
        }

        return s


    # test_siania_marchwi()

    i=0
