# Główny plik gry
from gra_poletko.bcolors import bcolors
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


def ustawienia_początkowe(wielkosc_planszy: int):
    S.dzienSymulacji = 1
    global rol
    rol = Rolnik(Plansza(wielkosc_planszy))
    global skl
    skl = Sklep()
    ustaw_ceny_w_sklepie(skl)


def faza_siania():
    print(f"{bcolors.HEADER}\nFaza siania.{bcolors.ENDC}")
    rol.pokazStan()
    rol.zasiew()


def faza_kupna():
    print(f"{bcolors.HEADER}\nFaza kupna.{bcolors.ENDC}")
    rol.pokazStan()
    rol.zakupy(skl)


def faza_zbiorów():
    print(f"{bcolors.HEADER}\nFaza zbirów.{bcolors.ENDC}")
    rol.zbiory()


def faza_podlewania():
    print(f"{bcolors.HEADER}\nFaza podlewania.{bcolors.ENDC}")
    rol.podlewanie()


def dzien():
    faza_kupna()
    faza_siania()
    faza_zbiorów()
    faza_podlewania()
    print(f"{bcolors.OKBLUE}Liczba monet na koniec {S.dzienSymulacji}. dnia: {rol.getLiczbaMonet}{bcolors.ENDC}\n")
    S.dzienSymulacji += 1


def symuluj(liczba_dni: int):
    print(f"{bcolors.HEADER}Gra trwająca {liczba_dni} dni rozpoczyna się.\n{bcolors.ENDC}")
    for k in range(liczba_dni):
        print(f"{bcolors.HEADER}Dzień dobry!\nJest dzień {S.dzienSymulacji}.")
        dzien()


if __name__ == "__main__":

    ustawienia_początkowe(wielkosc_planszy=10)
    symuluj(liczba_dni=5)

    i = 0
