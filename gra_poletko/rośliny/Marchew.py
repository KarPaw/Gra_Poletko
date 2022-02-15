from gra_poletko.rośliny import Roślina


class Marchew(Roślina):

    def __init__(self):
        nazwa = "Marchew"
        nasiono_cena = 100
        skup_cena = 150
        czas_wegetacji = 3
        woda_cena = 5
        super().__init__(nazwa, nasiono_cena, skup_cena, czas_wegetacji, woda_cena)

    def pusta(self):
        pass
