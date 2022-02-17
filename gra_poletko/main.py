# Główny plik gry

from gra_poletko.rośliny.marchew import Marchew
from gra_poletko.plansza.plansza import Plansza
from gra_poletko.sklep.sklep import Sklep
from gra_poletko.rolnik.rolnik import Rolnik

from gra_poletko.StałeUniwersalne import Singleton as S


def ustaw_ceny_w_sklepie(sklep):
    ziarnaCeny = {
        "Marchew": Marchew.cenaWSklepie(),
        # "Ziemniak": Ziemniak.cenaWSklepie(),
    }
    sklep.setZiarna(ziarnaCeny)

    # return "Ustaiwono ceny w sklepie"


if __name__ == "__main__":
    czas = S.dzienSymulacji

    rol = Rolnik(Plansza(10))

    def faza_siania():
        rol.zasiew()

    def faza_kupna():
        skl = Sklep()
        ustaw_ceny_w_sklepie(skl)
        rol.pokazStan()
        rol.zakupy(skl)
        rol.pokazStan()

    def faza_zbiorów():
        rol.zbiory()

    def faza_podlewania():
        rol.podlewanie()

    faza_kupna()

    faza_siania()

    print(f"Liczba monet: {rol.getLiczbaMonet}")
    S.dzienSymulacji = 10
    faza_zbiorów()

    print(f"Liczba monet: {rol.getLiczbaMonet}")

    faza_podlewania()

    i = 0
