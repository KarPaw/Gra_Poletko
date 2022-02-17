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

    # return "Ustaiwono ceny w sklepie"


def ustawienia_początkowe():
    S.dzienSymulacji = 1
    global rol
    rol = Rolnik(Plansza(10))
    global skl
    skl = Sklep()
    ustaw_ceny_w_sklepie(skl)


def faza_siania():
    print(f"{bcolors.HEADER}Faza siania.{bcolors.ENDC}")
    rol.zasiew()


def faza_kupna():
    print(f"{bcolors.HEADER}Faza kupna.{bcolors.ENDC}")
    rol.pokazStan()
    rol.zakupy(skl)
    rol.pokazStan()


def faza_zbiorów():
    print(f"{bcolors.HEADER}Faza zbirów.{bcolors.ENDC}")
    rol.zbiory()


def faza_podlewania():
    print(f"{bcolors.HEADER}Faza podlewania.{bcolors.ENDC}")
    rol.podlewanie()


def dzien():
    faza_kupna()
    faza_siania()
    # print(f"Liczba monet: {rol.getLiczbaMonet}")
    faza_zbiorów()
    faza_podlewania()
    print(f"{bcolors.WARNING}Liczba monet na koniec {S.dzienSymulacji}. dnia: {rol.getLiczbaMonet}{bcolors.WARNING}")
    S.dzienSymulacji += 1


def symuluj(liczbaDni):
    print(f"{bcolors.HEADER}Gra trwająca {liczbaDni} dni rozpoczyna się.\n{bcolors.ENDC}")
    for k in range(liczbaDni):
        print(f"{bcolors.HEADER}Dzień dobry!\nJest dzień:{S.dzienSymulacji}.")
        dzien()


if __name__ == "__main__":

    ustawienia_początkowe()
    symuluj(3)

    i = 0
