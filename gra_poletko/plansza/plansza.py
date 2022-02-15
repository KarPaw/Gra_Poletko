from gra_poletko.plansza.poleJedno import PoleJedno as p


class Plansza():
    __slots__ = "__pola"

    def __init__(self, liczba_pól):
        # Lista o N polach
        self.__pola = tuple(p(k) for k in range(liczba_pól))

    def ktorePodlane(self):
        return [pole.czyPodlano() for pole in self.__pola]

    def dojrzewanie(self):
        for pole in self.__pola:
            pole.czy_gotowe_do_zbioru()
