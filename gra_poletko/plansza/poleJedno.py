from gra_poletko.rośliny.roślina import Roślina

class PoleJedno():
    __slots__ = ["__zasianaRoslina", "__kiedyZasiano", "__czyPodlane", "__gotowe", "__id"]

    def __init__(self, id):
        self.__id = id
        # self.__zasianaRoslina:Roślina = Roślina()
        self.__kiedyZasiano = None
        self.__czyPodlane = True
        self.__gotowe = False

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
        self.__czyPodlane = True

    def zasiej_roślinę(self, roślina: Roślina):
        self.__zasianaRoslina:Roślina = roślina
        # TODO Stworzyc zegar gry i tu podawac dzien zasiania
        self.__kiedyZasiano = 0

    def czy_gotowe_do_zbioru(self):
        posiana = self.__zasianaRoslina
        potrzebneDni = posiana.getCzasWegetacji
        # TODO ObecnyDzien
        obecnyDzien = 0
        ileMinelo = obecnyDzien - self.kiedyZasiano

        if ileMinelo >= potrzebneDni:
            self.__gotowe = True
