from gra_poletko.bcolors import bcolors
from gra_poletko.sklep.sklep import Sklep
from gra_poletko.rośliny.roślina import Roślina
from gra_poletko.plansza.poleJedno import PoleJedno


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
                return  # TODO Narazie Środki ochrony są niewidoczne.
                # print("Srodki Ochrony Roslin:")

            nazwy_roślin = [roślina.nazwa for roślina in self.__ekwipunek[i].keys()]

            pary = zip(nazwy_roślin, self.__ekwipunek[i].values())
            for para in pary:
                print(f"\t{bcolors.OKBLUE}{para}{bcolors.ENDC}")
            # for para in self.__ekwipunek[i]:
            #     print(f"\t{bcolors.OKBLUE}{para}{bcolors.ENDC}")

    def zakupy(self, sklep: Sklep):
        # Otwieranie
        oferta = sklep.getOferta
        ziarna = sklep.getZiarna

        def pobierz_odpowiedz():
            while True:
                odp = input("Czy chcesz kupić coś jeszcze T/N:\n>").lower()
                if odp == "t" or odp == "n":
                    break
            return odp

        # Kupowanie
        def kupZiarna(produkt, liczba):
            # Szukanie Indeksu W krotce
            roślinyWszystkie = tuple(self.getZiarna.keys())
            j = -1

            if liczba <= 0:
                return j

            for ros in roślinyWszystkie:
                if ros.getNazwa.__get__(ros) == produkt.capitalize():
                    j = roślinyWszystkie.index(ros)

            if j == -1:
                print(bcolors.FAIL + "Nie można dodać do ekwipunku..." + bcolors.ENDC)
                return j

            prodEkwipunek = roślinyWszystkie[j]

            doZaplaty = ziarna[f"{produkt.capitalize()}"] * liczba
            if doZaplaty == 0:
                print(f"Nie można sprzedać 0 sztuk")
                return j
            if self.__liczba_monet >= doZaplaty:
                self.__liczba_monet -= doZaplaty
                self.__ekwipunek[0][prodEkwipunek] += liczba
                print(f"{bcolors.WARNING}Zakupiono produkt: {produkt} x {liczba}.{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}Niewystarczająca liczba monet - masz ich {self.__liczba_monet}.{bcolors.ENDC}")

            return j

        def pojedynczyZakup():
            print(oferta)
            produkt = input("Podaj nazwę produktu, który chcesz zakupić (bez cudzysłowów):\n>")
            if not produkt:
                print("Nie wybrano produktu.")
                pojedynczyZakup()
            liczba = input("Podaj liczbę sztuk:\n>")
            # if not liczba or liczba == "0":
            #     print(f"{bcolors.FAIL}Nic nie kupiono.{bcolors.ENDC}")
            #     liczba = 0

            try:
                liczba = int(liczba)
            except ValueError:
                liczba = 0

            if liczba < 0:
                print(f"{bcolors.FAIL}Niepoprawna liczba sztuk {liczba}.{bcolors.ENDC}")

            czyKupiono = kupZiarna(produkt, liczba)
            return czyKupiono

        cK = pojedynczyZakup()
        if cK == -1:
            print(f"{bcolors.FAIL}Nie dokonano zakupu.{bcolors.ENDC}")

        odpowiedz = pobierz_odpowiedz()
        if odpowiedz == "t":
            self.zakupy(sklep)

    def zasiew(self):
        """Na którym polu: liczymy od 1."""
        # Sprawdza, czy masz taką roślinę w ekwipunku i odpowiednio zmniejsza liczbę sztuk
        # print(self.getEkwipunek)
        # print(f"{bcolors.WARNING}Twoje ziarna:{bcolors.ENDC}\n{bcolors.OKBLUE}{self.getZiarna}{bcolors.ENDC}")
        # znajdz rolisne z katalogu po nazwie. indeks katalogu...
        roślinyWszystkie = tuple(self.getZiarna.keys())

        def szuakanie_indeksu():
            roślinaInput = input("Wybierz roślinę do zasiania(bez cudzysłowów)\n>")
            # roślinyWszystkie = tuple(self.getZiarna.keys())
            for j in range(len(roślinyWszystkie)):
                roślina: Roślina = roślinyWszystkie[j]
                if roślina.getNazwa.__get__(roślina).lower() == roślinaInput.lower():
                    # iZnal = j
                    return j
                elif not roślinaInput:  # Pusty napis
                    return -1
                else:
                    print(f"{bcolors.FAIL}Nie posiadasz takiej sadzonki.\nWybierz inną lub wprowadź pusty napis.{bcolors.ENDC}")
                    szuakanie_indeksu()

        iZnal = szuakanie_indeksu()
        if iZnal == -1:
            return
        else:
            wybranaRoślina = roślinyWszystkie[iZnal]

        def zasiej_na_polach():
            polaDoZasiewu = tuple(int(x) for x in
                                  input("Podaj numery pól do zasiewu oddzielone spacją,\n>").split())

            # Sprawdza czy Wystarczy sadzonek
            ilePol = len(polaDoZasiewu)
            ileSadzonek = self.getZiarna[wybranaRoślina]
            if ilePol > ileSadzonek:
                print(f"{bcolors.FAIL}Zla liczba pól = {ilePol}. Masz tylko {ileSadzonek} sadzonek.{bcolors.ENDC}")
                zasiej_na_polach()
            elif not ilePol:
                print("Nie wybrano pól.")
            else:
                for i in polaDoZasiewu:
                    pj: PoleJedno = self.__poleRolnika.getPola()[i-1]
                    if not pj.coZasiano:
                        pj.zasiej_roślinę(wybranaRoślina)
                        self.getZiarna[wybranaRoślina] -= 1

                    else:
                        print(f"{bcolors.FAIL}Na polu {i} już coś rośnie.{bcolors.ENDC}")
                        continue
            print(f"{bcolors.WARNING}Zasiano {wybranaRoślina.nazwa} na możliwych polach spośród {polaDoZasiewu}{bcolors.ENDC}")

        zasiej_na_polach()
        odpowiedz = input("Czy chcesz siać dalej? T/N\n>")
        if odpowiedz.lower() == "t":
            self.zasiew()

    def zbiory(self):
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
            print(f"{bcolors.WARNING}Zarobek z plonów wynosi: {zarobek}.{bcolors.ENDC}")
        else:
            print(f"{bcolors.WARNING}Dziś zebrano żadnych plonów.{bcolors.ENDC}")

    def podlewanie(self):
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
            print(f"{bcolors.WARNING}Żande pola nie wymagały podlewania.{bcolors.ENDC}")
        else:
            print(f"{bcolors.WARNING}Twoje pola zostały podlane. Pobrano opłatę = {opłata} monet.{bcolors.ENDC}")
