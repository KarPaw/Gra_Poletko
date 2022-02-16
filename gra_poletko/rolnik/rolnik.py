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
        print("Liczba monet i ekwipunek Rolnika")
        print("Monety:", self.__liczba_monet)
        print("Ekwipunek:\n", self.__ekwipunek)

    def zakupy(self, sklep: Sklep):
        # Otwieranie
        oferta = sklep.getOferta
        ziarna = sklep.getZiarna

        # Kupowanie
        def kupZiarna(produkt, liczba):
            # Szukanie Indeksu W krotce
            roślinyWszystkie = tuple(self.getZiarna.keys())

            j = -1
            for ros in roślinyWszystkie:
                if ros.getNazwa.__get__(ros) == produkt.capitalize():
                    j = roślinyWszystkie.index(ros)

            if j == -1:
                print(bcolors.FAIL + "Nie można dodać do ekwipunku.." + bcolors.ENDC)
                return

            prodEkwipunek = roślinyWszystkie[j]

            doZaplaty = ziarna[f"{produkt.capitalize()}"] * liczba
            if doZaplaty == 0:
                return
            if self.__liczba_monet >= doZaplaty:
                self.__liczba_monet -= doZaplaty
                self.__ekwipunek[0][prodEkwipunek] += liczba
                print(f"Zakupiono produkt: {produkt} x {liczba}.")
            else:
                print(f"{bcolors.FAIL}Niewystarczająca liczba monet - masz ich {self.__liczba_monet}.{bcolors.ENDC}")

        def pojedynczyZakup():
            print(oferta)
            produkt = input("Podaj nazwę produktu, który chcesz zakupić (bez cudzysłowów):\n>")
            liczba = int(input("Podaj liczbę sztuk:\n>"))
            if liczba <= 0:
                print(f"Niepoprawna liczba sztuk {liczba}. Zakup anulowany.\n")
                liczba = 0

            kupZiarna(produkt, liczba)

            odpowiedz = input("Czy chcesz kupić coś jeszcze T/N:\n>")
            return odpowiedz

        if pojedynczyZakup() == "T":
            pojedynczyZakup()

        print("Koniec zakupów.")

    def zasiew(self):
        """Na którym polu: liczymy od 1."""
        # Sprawdza, czy masz taką roślinę w ekwipunku i odpowiednio zmniejsza liczbę sztuk
        print(self.getEkwipunek)

        # znajdz rolisne z katalogu po nazwie. indeks katalogu...
        roślinyWszystkie = tuple(self.getZiarna.keys())

        def szuakanie_indeksu():
            roślinaInput = input("Wybierz roślinę do zasiania\n>")
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
            return "Koniec Fazy Siania."
        else:
            wybranaRoślina = roślinyWszystkie[iZnal]

        def zasiej_na_polach():
            polaDoZasiewu = tuple(int(x) for x in
                                  input("Podaj numery pól do zasiewu oddzielone spacją,\n>").split())

            # Sprawdza czy Wystarczy sadzonek
            ilePol = len(polaDoZasiewu)
            ileSadzonek = self.getZiarna[wybranaRoślina]
            if ilePol > ileSadzonek:
                print(f"Zla liczba pól = {ilePol}. Masz tylko {ileSadzonek} sadzonek.")
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
                        print(f"Na polu {i} już coś rośnie.")
                        continue
            print(f"Zasiano {wybranaRoślina} na możliwych polach spośród {polaDoZasiewu}")

        zasiej_na_polach()
        odpowiedz = input("Czy chcesz siać dalej? T/N\n>")
        if odpowiedz.lower() == "t":
            self.zasiew()
        else:
            print("Koniec fazy siania.")

    def zbiory(self):
        polaDoZbioru = self.__poleRolnika.polaGotoweDoZbioru()
        # TODO Opłata miała zależeć od rośliny... Ale jeszcze jest stała, odgórna.
        oplata = len(polaDoZbioru) * 10
        zarobek = 0
        for i in polaDoZbioru:
            p = self.__poleRolnika.getPola()[i]
            zarobek += p.zbierzPlon()
            p.resetuj()

        self.__liczba_monet += zarobek-oplata

    def podlewanie(self):
        pass
