from abc import ABC, abstractmethod

# class Roślina(ABC):
class Roślina:

    def __init__(self, nazwa, nasiono_cena, skup_cena, czas_wegetacji, woda_cena): #, szkodniki):

        self.nazwa = nazwa
        self.__nasiono_cena = nasiono_cena
        self.__skup_cena = skup_cena
        self.__czas_wegetacji = czas_wegetacji # ile dni rośnie, aż będzie gotowa do zbioru
        self.__woda_cena = woda_cena

        # self.__szkodniki = szkodniki

    def blah(self):
        pass
