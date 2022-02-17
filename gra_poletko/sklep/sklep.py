from gra_poletko.bcolors import bcolors
from gra_poletko.StałeUniwersalne import Singleton as S


class Sklep:
    __slots__ = ["__ziarna", "__srodkiOchronyRoslin"]

    def __init__(self):
        self.__ziarna = None
        self.__srodkiOchronyRoslin = None

    def setZiarna(self, slownikZiarnoCena: dict):
        self.__ziarna = slownikZiarnoCena

    # def setSrodkiOchrony(self, slownikSrodkowOchronyZCenami: dict):
    #     self.__srodkiOchronyRoslin = slownikSrodkowOchronyZCenami

    @property
    def getZiarna(self):
        # Do implementacji
        return self.__ziarna

    @property
    def getOferta(self):
        # Ladnie sie wyswietla uzytkownikowi
        # TODO spacja = "\t"
        c = "W sklepie znajdują sie nastepujace produkty:"
        d = "Produkt | Cena za sztukę"
        return f"{bcolors.WARNING}{S.spacja}{c}\n" \
               f"{S.spacja}{d}{bcolors.ENDC}\n\n" \
               f"{bcolors.OKBLUE}{S.spacja}{self.getZiarna}{bcolors.ENDC}\n"
