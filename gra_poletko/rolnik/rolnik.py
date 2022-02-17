from gra_poletko.bcolors import bcolors
from gra_poletko.sklep.sklep import Sklep
from gra_poletko.rośliny.roślina import Roślina
from gra_poletko.plansza.poleJedno import PoleJedno


def zmienDodatniaNaInteger(elt):
    try:
        liczba = int(elt)
        if liczba <= 0:
            return None
    except ValueError:
        liczba = None

    return liczba


class Rolnik:

    def __init__(self, plansza):
        self.__liczba_monet = 10000  # na start
        self.__poleRolnika = plansza
        katalog = Roślina.__subclasses__()

        self.__ekwipunek = (
            # 0 = nasiona | 1 =  srodki ochrony roslin
            {
                katalog[0]: 5  # Marchew # Dajemy 5 sztuk na start
                # ,katalog[1]: 0 # Ziemniaki
            },
            {
                "SrodekNaStonki": 0
            })

    def przypiszPoletko(self, pole):
        self.__poleRolnika = pole

    def odejmijMonety(self, n):
        self.__liczba_monet -= n

    @property
    def getLiczbaMonet(self):
        return self.__liczba_monet

    @property
    def getEkwipunek(self):
        return self.__ekwipunek

    @property
    def getZiarna(self):
        return self.__ekwipunek[0]

    @property
    def getPoleRolnika(self):
        return self.__poleRolnika

    def pokazStan(self):
        print(f"{bcolors.BOLD}{bcolors.UNDERLINE}>> Przedmioty i Monety<<{bcolors.ENDC}")
        print(f"{bcolors.BOLD}Monety: {self.__liczba_monet}")
        print(f"Ekwipunek:{bcolors.ENDC}")
        # Ladne printowanie zawartosci
        for i in range(len(self.__ekwipunek)):
            if i == 0:
                print("\tZiarna:")
            elif i == 1:
                print(f"{bcolors.UNDERLINE}.........................{bcolors.ENDC}\n")

                return  # TODO Narazie Środki ochrony są niewidoczne. Jak beda trzeba zakomentowac zaznaczone
                # print("Srodki Ochrony Roslin:")

            nazwy_roślin = [roślina.nazwa for roślina in self.__ekwipunek[i].keys()]

            pary = zip(nazwy_roślin, self.__ekwipunek[i].values())
            for para in pary:
                print(f"\t{bcolors.OKBLUE}{para}{bcolors.ENDC}")
            # for para in self.__ekwipunek[i]:
            #     print(f"\t{bcolors.OKBLUE}{para}{bcolors.ENDC}")
        # print(f"{bcolors.UNDERLINE}........................{bcolors.ENDC}")

    def zakupy(self, sklep: Sklep):
        # Otwieranie
        oferta = sklep.getOferta
        ziarna = sklep.getZiarna
        spacja = "\t"

        def pobierz_odpowiedz():
            while True:
                odp = input(f"{bcolors.BOLD}{spacja}Czy chcesz kupić coś jeszcze T/N:\n>{bcolors.ENDC}").lower()
                if odp == "t" or odp == "n":
                    break
            return odp

        # Kupowanie
        def kupZiarna(produkt, liczba):
            # Szukanie Indeksu W krotce
            roślinyWszystkie = tuple(self.getZiarna.keys())
            j = -1
            if not liczba:
                return j
            elif liczba <= 0:
                return j

            for ros in roślinyWszystkie:
                if ros.getNazwa.__get__(ros) == produkt.capitalize():
                    j = roślinyWszystkie.index(ros)

            if j == -1:
                print(f"{spacja}{bcolors.FAIL}Nie można dodać do ekwipunku...{bcolors.ENDC}")
                return j

            prodEkwipunek = roślinyWszystkie[j]

            doZaplaty = ziarna[f"{produkt.capitalize()}"] * liczba
            if doZaplaty == 0:
                print(f"{spacja}Nie można sprzedać 0 sztuk")
                return j
            if self.__liczba_monet >= doZaplaty:
                self.__liczba_monet -= doZaplaty
                self.__ekwipunek[0][prodEkwipunek] += liczba
                print(f"{spacja}{bcolors.WARNING}Zakupiono produkt: {produkt} x {liczba}.{bcolors.ENDC}")
            else:
                print(f"{spacja}{bcolors.FAIL}Niewystarczająca liczba monet - masz ich {self.__liczba_monet}.{bcolors.ENDC}")

            return j

        def pojedynczyZakup():
            print(f"\n{oferta}")
            produkt = input(f"{bcolors.BOLD}{spacja}Podaj nazwę produktu, który chcesz zakupić (bez cudzysłowów):\n>{bcolors.ENDC}")
            if not produkt:
                print(f"{spacja}{bcolors.FAIL}Nie wybrano produktu.{bcolors.ENDC}")
                return -1
            liczba = input(f"{bcolors.BOLD}{spacja}Podaj liczbę sztuk:\n>{bcolors.ENDC}")
            # if not liczba or liczba == "0":
            #     print(f"{bcolors.FAIL}Nic nie kupiono.{bcolors.ENDC}")
            #     liczba = 0

            # try:
            #     liczba = int(liczba)
            # except ValueError:
            #     liczba = 0
            liczba = zmienDodatniaNaInteger(liczba)
            if not liczba:
                print(f"{spacja}{bcolors.FAIL}Nie podano liczby lub liczba = 0.{bcolors.ENDC}")
            elif liczba <= 0:
                print(f"{spacja}{bcolors.FAIL}Niepoprawna liczba sztuk {liczba}.{bcolors.ENDC}")

            czyKupiono = kupZiarna(produkt, liczba)
            return czyKupiono

        cK = pojedynczyZakup()
        if cK == -1:
            print(f"{spacja}{bcolors.FAIL}Nie dokonano zakupu.{bcolors.ENDC}")

        odpowiedz = pobierz_odpowiedz()
        if odpowiedz == "t":
            self.zakupy(sklep)

    def zasiew(self):
        """Na którym polu: liczymy od 1."""
        # Sprawdza, czy masz taką roślinę w ekwipunku i odpowiednio zmniejsza liczbę sztuk
        # print(self.getEkwipunek)
        # print(f"{bcolors.WARNING}Twoje ziarna:{bcolors.ENDC}\n{bcolors.OKBLUE}{self.getZiarna}{bcolors.ENDC}")
        # znajdz rolisne z katalogu po nazwie. indeks katalogu...
        spacja = "\t"
        roślinyWszystkie = tuple(self.getZiarna.keys())

        def szuakanie_indeksu():
            roślinaInput = input(f"{bcolors.BOLD}{spacja}Wybierz roślinę do zasiania(bez cudzysłowów)\n>{bcolors.ENDC}")
            # roślinyWszystkie = tuple(self.getZiarna.keys())

            if not roślinaInput:  # TODO Pusty napis
                print(f"{spacja}{bcolors.FAIL}Nie wprowadzono nazwy rośliny.{bcolors.ENDC}")
                return -1

            for j in range(len(roślinyWszystkie)):
                roślina: Roślina = roślinyWszystkie[j]
                if roślina.getNazwa.__get__(roślina).lower() == roślinaInput.lower():
                    return j
                else:
                    print(f"{spacja}{bcolors.FAIL}Nie posiadasz takiej sadzonki.\n{spacja}Wybierz inną lub wprowadź pusty napis.{bcolors.ENDC}")
                    return -1

        def zasiej_na_polach(wybranaRoślina):
            polaDoZasiewu = tuple(zmienDodatniaNaInteger(x)
                                  for x in
                                  input(f"{bcolors.BOLD}{spacja}Podaj numery pól do zasiewu oddzielone spacją,\n>{bcolors.ENDC}").split()
                                  if zmienDodatniaNaInteger(x) is not None)

            # Sprawdza czy Wystarczy sadzonek
            ilePol = len(polaDoZasiewu)
            ileSadzonek = self.getZiarna[wybranaRoślina]
            if not ilePol:
                print(f"{spacja}{bcolors.FAIL}Nie wybrano pól.{bcolors.ENDC}")
                return
            if ilePol > ileSadzonek:
                print(f"{spacja}{bcolors.FAIL}Zla liczba pól = {ilePol}. Masz tylko {ileSadzonek} sadzonek.{bcolors.ENDC}")
                zasiej_na_polach(wybranaRoślina)
            else:
                # indeks nal. [1, n]
                for indeks in polaDoZasiewu:
                    if indeks > len(polaDoZasiewu):
                        print(f"{bcolors.FAIL}{spacja}Zły numer pola = {indeks}. Przechodzę do kolejnego.{bcolors.ENDC}")
                        continue
                    pj: PoleJedno = self.__poleRolnika.getPola()[indeks-1]
                    if not pj.coZasiano:
                        pj.zasiej_roślinę(wybranaRoślina)
                        self.getZiarna[wybranaRoślina] -= 1
                        print(f"{spacja}{bcolors.WARNING}Zasiano {wybranaRoślina.nazwa} na polu {indeks}.{bcolors.ENDC}")
                    else:
                        print(f"{spacja}{bcolors.FAIL}Na polu {indeks} już coś rośnie.{bcolors.ENDC}")
                        continue

        def pobierz_odpowiedz():
            while True:
                odp = input(f"{bcolors.BOLD}{spacja}Czy chcesz siać dalej? T/N\n>{bcolors.ENDC}").lower()
                if odp == "t" or odp == "n":
                    break
            return odp

        iZnal = szuakanie_indeksu()
        if iZnal != -1:
            wybranaRoślina = roślinyWszystkie[iZnal]
            zasiej_na_polach(wybranaRoślina)

        odpowiedz = pobierz_odpowiedz()

        if odpowiedz.lower() == "t":
            self.zasiew()

    def zbiory(self):
        spacja = "\t"
        polaDoZbioru = self.__poleRolnika.polaGotoweDoZbioru()
        # TODO Opłata miała zależeć od rośliny... Ale jeszcze jest stała, odgórna.
        oplata = len(polaDoZbioru) * 10
        dochód = 0
        for i in polaDoZbioru:
            p = self.__poleRolnika.getPola()[i]
            dochód += p.zbierzPlon()
            p.resetuj()

        zarobek = dochód - oplata
        self.__liczba_monet += zarobek
        if zarobek > 0:
            print(f"{spacja}{bcolors.WARNING}Zarobek z plonów wynosi: {zarobek}.{bcolors.ENDC}")
        else:
            print(f"{spacja}{bcolors.WARNING}Dziś nie zebrano żadnych plonów.{bcolors.ENDC}")

    def podlewanie(self):
        spacja = "\t"
        wszystkiePola = self.__poleRolnika
        wszystkiePola.resetPodlaniaCalePole()
        doPodlania = wszystkiePola.ktoreNiepodlane()
        # opłata = doPodlania.podlej()
        opłata = 0
        for p in doPodlania:
            opłata += p.podlej()

        # TODO Na poczatku nowego dnia reset Podlania w <main>?
        # TODO Na ten moment reset podlania jest przed podlewaniem.
        self.odejmijMonety(opłata)
        # Można wejść w ujemne Saldo, bo najpierw podlewa, potem odejmuje.

        if opłata == 0:
            print(f"{spacja}{bcolors.WARNING}Żande pola nie wymagały podlewania.{bcolors.ENDC}")
        else:
            print(f"{spacja}{bcolors.WARNING}Twoje pola zostały podlane. Pobrano opłatę = {opłata} monet.{bcolors.ENDC}")
