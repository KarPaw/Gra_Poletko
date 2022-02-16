from gra_poletko.sklep.sklep import Sklep
from gra_poletko.rośliny.roślina import Roślina
from gra_poletko.plansza.poleJedno import PoleJedno


class Rolnik:

    def __init__(self):
        self.__liczba_monet = 10000  # na start
        self.__poleRolnika = None
        self.__ekwipunek = (
            # 0 = nasiona | 1 =  srodki ochrony roslin
            {
                "Marchew": 0,
                "Ziemniaki": 0
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
            doZaplaty = ziarna[f"{produkt}"] * liczba
            if doZaplaty == 0:
                return
            if self.__liczba_monet >= doZaplaty:
                self.__liczba_monet -= doZaplaty
                self.__ekwipunek[0][produkt] += liczba
                print(f"Zakupiono produkt: {produkt} x {liczba}.")
            else:
                print(
                    Exception(f"Niewystarczająca liczba monet - masz ich {self.__liczba_monet}.")
                )

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
        # (self, roślina:Roślina, na_którym_polu:int):
        """Na którym polu: liczymy od 1."""
        #TODO Musi sprawdzac, czy masz taką roślinę w ekwipunku i odpowiednio zmniejszyć liczbę sztuk
        print(self.getEkwipunek)
        roślinaInput = input("Wybierz roślinę do zasiania")
        #TODO To musi
        roślina = self.getEkwipunek[0][roślinaInput]
        polaDoZasiewu = tuple(int(x) for x in input("Podaj numery pól do zasiewu oddzielone spacją,\n").split())
        # pDZ = (3, 5, 6, 1, 10)
        for i in polaDoZasiewu:
            pj:PoleJedno = self.__poleRolnika[i-1]
            pj.zasiej_roślinę(roślina)

        # pole = self.__pola[na_którym_polu-1]
        # pole.zasiej_roślinę(roślina)
        print(f"Zasiano {roślina} na polach {polaDoZasiewu}")

    def podlewanie(self):
        pass

    def zbiory(self):
        pass