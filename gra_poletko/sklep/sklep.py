from gra_poletko.bcolors import bcolors


class Sklep:
    __slots__ = ["__ziarna", "__srodkiOchronyRoslin"]

    def __init__(self):
        self.__ziarna = None
        self.__srodkiOchronyRoslin = None

    def setZiarna(self, slownikZiarnoCena: dict):
        self.__ziarna = slownikZiarnoCena

    @property
    def getZiarna(self):
        # Do implementacji
        return self.__ziarna

    @property
    def getOferta(self):
        # Ladnie sie wyswietla uzytkownikowi
        spacja = "\t"
        c = "W sklepie znajdują sie nastepujace produkty:"
        d = "Produkt | Cena za sztukę"
        return f"{bcolors.WARNING}{spacja}{c}\n" \
               f"{spacja}{d}{bcolors.ENDC}\n\n" \
               f"{bcolors.OKBLUE}{spacja}{self.getZiarna}{bcolors.ENDC}\n"
    # def setSrodkiOchrony(self, slownikSrodkowOchronyZCenami):
    #     self.__srodkiOchronyRoslin = slownikSrodkowOchronyZCenami
