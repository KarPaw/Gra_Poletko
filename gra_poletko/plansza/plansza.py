from gra_poletko.plansza.poleJedno import PoleJedno as p
from gra_poletko.rośliny.roślina import Roślina


class Plansza():
    __slots__ = ["__pola", "__czyje"]

    def __init__(self, liczba_pól):
        # Lista o N polach
        self.__pola = tuple(p(k) for k in range(liczba_pól))

    def ktorePodlane(self):
        return [pole.czyPodlano() for pole in self.__pola]

    def polaGotoweDoZbioru(self):

        gotowePola = []
        # for pole in self.__pola:
        #     if pole.czy_gotowe_do_zbioru():
        #         gotowePola.append(pole.__id)

        for i in range(len(self.__pola)):
            p = self.__pola[i]
            if p.czy_gotowe_do_zbioru():
                gotowePola.append(i)

        print(gotowePola)
        return gotowePola

    def getPola(self):
        return self.__pola

    # def zasiej(self, roślina:Roślina, na_którym_polu:int):
    #     """Na którym polu: liczymy od 1."""
    #     #TODO Musi sprawdzac, czy masz taką roślinę w ekwipunku i odpowiednio zmniejszyć liczbę sztuk
    #
    #     pole = self.__pola[na_którym_polu-1]
    #     pole.zasiej_roślinę(roślina)
    #     print("zasiano")
