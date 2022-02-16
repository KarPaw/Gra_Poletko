from abc import ABC


class Roślina(ABC):
    __slots__ = ["__nazwa", "__nasiono_cena", "__skup_cena", "__czas_wegetacji", "__woda_cena"]

    def __init__(self, nazwa, nasiono_cena, skup_cena, czas_wegetacji, woda_cena):  # , szkodniki):

        self.__nazwa = nazwa
        self.__nasiono_cena = nasiono_cena
        self.__skup_cena = skup_cena
        self.__czas_wegetacji = czas_wegetacji  # ile dni rośnie, aż będzie gotowa do zbioru
        self.__woda_cena = woda_cena
        # self.__szkodniki = szkodniki

    @property
    def getNazwa(self):
        return self.__nazwa

    @property
    def getCzasWegetacji(self):
        return self.__czas_wegetacji

    @property
    def getCenaNasiono(self):
        return self.__nasiono_cena

    @property
    def getCenaSkup(self):
        return self.__skup_cena

    @property
    def getCenaWoda(self):
        return self.__woda_cena

    def __str__(self):
        return self.getNazwa
