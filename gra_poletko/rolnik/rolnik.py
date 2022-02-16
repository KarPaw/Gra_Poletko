from gra_poletko.sklep.sklep import Sklep
from gra_poletko.rośliny.roślina import Roślina
from gra_poletko.rośliny.marchew import Marchew
from gra_poletko.plansza.poleJedno import PoleJedno
# from gra_poletko.plansza.plansza import Plansza

class Rolnik:

    def __init__(self):
        self.__liczba_monet = 10000  # na start
        self.__poleRolnika = None
        katalog = [
            Marchew()
            # ,Ziemniak()
        ]

        self.__ekwipunek = (
            # 0 = nasiona | 1 =  srodki ochrony roslin
            {
                katalog[0]: 5  # Marchew #TODO Dajemy 5 sztuk na start?
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
                if ros.getNazwa == produkt.capitalize():
                    j = roślinyWszystkie.index(ros)

            if j == -1:
                return Exception("Nie można dodać do ekwipunku..")

            prodEkwipunek = roślinyWszystkie[j]

            doZaplaty = ziarna[f"{produkt}"] * liczba
            if doZaplaty == 0:
                return
            if self.__liczba_monet >= doZaplaty:
                self.__liczba_monet -= doZaplaty
                # TODO Tutaj trzeba produkt String -> Roślina
                self.__ekwipunek[0][prodEkwipunek] += liczba
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
        # TODO Musi sprawdzac, czy masz taką roślinę w ekwipunku i odpowiednio zmniejszyć liczbę sztuk
        print(self.getEkwipunek)

        # TODO To musi przeksztalcac String -> Roślina

        # znajdz rolisne z katalogu po nazwie. indeks katalogu...
        roślinyWszystkie = tuple(self.getZiarna.keys())
        def szuakanie_indeksu():
            roślinaInput = input("Wybierz roślinę do zasiania\n>")
            # roślinyWszystkie = tuple(self.getZiarna.keys())
            for j in range(len(roślinyWszystkie)):
                roślina: Roślina = roślinyWszystkie[j]
                if roślina.getNazwa.lower() == roślinaInput.lower():
                    # iZnal = j
                    return j
                elif not roślinaInput: # Pusty napis
                    return -1
                else:
                    print(
                        Exception("Nie posiadasz takiej sadzonki.\nWybierz inną lub wprowadź pusty napis."))
                    szuakanie_indeksu()

        iZnal = szuakanie_indeksu()
        if iZnal == -1:
            return "Koniec Fazy Siania."
        else:
            wybranaRoślina = roślinyWszystkie[iZnal]

        def zasiej_na_polach():
            polaDoZasiewu = tuple(int(x) for x in
                                  input("Podaj numery pól do zasiewu oddzielone spacją,\n>").split())

            # pDZ = (3, 5, 6, 1, 10)
            #TODO Sprawdz czy Wystarczy sadzonek
            ilePol = len(polaDoZasiewu)
            ileSadzonek = self.getZiarna[wybranaRoślina]
            if ilePol > ileSadzonek:
                print(f"Zla liczba pól = {ilePol}. Masz tylko {ileSadzonek} sadzonek.")
                zasiej_na_polach()
            elif not ilePol:
                print("Nie wybrano pól.")
            else:
                for i in polaDoZasiewu:
                    pj:PoleJedno = self.__poleRolnika.getPola()[i-1]
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





        # pole = self.__pola[na_którym_polu-1]
        # pole.zasiej_roślinę(roślina))

    def podlewanie(self):
        pass

    def zbiory(self):
        pass
