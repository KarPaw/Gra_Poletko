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
        c = "\nW sklepie znajdują sie nastepujace produkty:"
        d = "\n{Produkt: Cena za sztukę}\n"
        return f"{bcolors.WARNING}{c}{d}{bcolors.ENDC}{bcolors.OKBLUE}{self.getZiarna}{bcolors.ENDC}\n"
    # def setSrodkiOchrony(self, slownikSrodkowOchronyZCenami):
    #     self.__srodkiOchronyRoslin = slownikSrodkowOchronyZCenami
