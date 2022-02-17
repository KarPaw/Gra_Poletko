from gra_poletko.rośliny.roślina import Roślina
from gra_poletko.StałeUniwersalne import Singleton as S


class PoleJedno:
    __slots__ = ["__zasianaRoslina", "__kiedyZasiano", "__czyPodlane", "__gotowe", "__id"]

    def __init__(self, ID):
        self.__id = ID
        self.__zasianaRoslina = None
        self.__kiedyZasiano = None
        self.__czyPodlane = True
        self.__gotowe = False

    @property
    def ID(self):
        return self.__id

    @property
    def coZasiano(self):
        return self.__zasianaRoslina

    @property
    def kiedyZasiano(self):
        return self.__kiedyZasiano

    @property
    def czyPodlano(self):
        return self.__czyPodlane

    def podlej(self):
        # Opłata za podlewanie:
        opłata = self.__zasianaRoslina.getCenaWoda.__get__(self.__zasianaRoslina)
        self.__czyPodlane = True
        return opłata

    def resetPodlania(self):
        if self.__zasianaRoslina:
            self.__czyPodlane = False

    def zasiej_roślinę(self, roślina: Roślina):
        self.__zasianaRoslina: Roślina = roślina
        self.__kiedyZasiano = S.dzienSymulacji

    def czy_gotowe_do_zbioru(self):
        posiana = self.__zasianaRoslina
        if not posiana:
            return self.__gotowe
        potrzebneDni = posiana.getCzasWegetacji.__get__(posiana)
        obecnyDzien = S.dzienSymulacji
        ileMinelo = obecnyDzien - self.kiedyZasiano

        if ileMinelo >= potrzebneDni:
            self.__gotowe = True

        return self.__gotowe

    def resetuj(self):
        self.__zasianaRoslina = None
        self.__kiedyZasiano = None
        self.__czyPodlane = True
        self.__gotowe = False

    def zbierzPlon(self):
        # Zwrcaca zarobioną kwotę z pojedynczego pola

        r = self.__zasianaRoslina
        zarobek = int(r.getCenaSkup.__get__(r))
        self.resetuj()

        return zarobek
