from gra_poletko.plansza.poleJedno import PoleJedno as p
from gra_poletko.rośliny.roślina import Roślina
from gra_poletko.rolnik.rolnik import Rolnik


class Plansza():
    __slots__ = ["__pola", "__czyje"]

    def __init__(self, liczba_pól, czyje:Rolnik):
        # Lista o N polach
        self.__pola = tuple(p(k) for k in range(liczba_pól))
        # self.__czyje = czyje
        czyje.przypiszPoletko(self)

    def ktorePodlane(self):
        return [pole.czyPodlano() for pole in self.__pola]

    def dojrzewanie(self):
        for pole in self.__pola:
            pole.czy_gotowe_do_zbioru()

    # def zasiej(self, roślina:Roślina, na_którym_polu:int):
    #     """Na którym polu: liczymy od 1."""
    #     #TODO Musi sprawdzac, czy masz taką roślinę w ekwipunku i odpowiednio zmniejszyć liczbę sztuk
    #
    #     pole = self.__pola[na_którym_polu-1]
    #     pole.zasiej_roślinę(roślina)
    #     print("zasiano")
