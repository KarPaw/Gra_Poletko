from gra_poletko.plansza.poleJedno import PoleJedno as pJ


class Plansza:
    __slots__ = ["__pola", "__czyje"]

    def __init__(self, liczba_pól):
        # Lista o N polach
        self.__pola = tuple(pJ(k) for k in range(liczba_pól))

    def ktoreNiepodlane(self):
        niepodlane = []
        for p in self.__pola:
            if not p.czyPodlano:
                niepodlane.append(p)
        return niepodlane

    def polaGotoweDoZbioru(self):

        gotowePola = []
        for i in range(len(self.__pola)):
            p = self.__pola[i]
            if p.czy_gotowe_do_zbioru():
                gotowePola.append(i)
        return gotowePola

    def getPola(self):
        return self.__pola

    def resetPodlaniaCalePole(self):
        for p in self.__pola:
            p.resetPodlania()

    def podlejWszystkie(self):
        opłataCałkowita = 0
        for p in self.__pola:
            opłataCałkowita += p.podlej()
        return opłataCałkowita
