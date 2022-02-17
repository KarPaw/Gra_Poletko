from gra_poletko.rośliny.roślina import Roślina


class Marchew(Roślina):
    nazwa = "Marchew"
    nasiono_cena = 100
    skup_cena = 150
    czas_wegetacji = 3
    woda_cena = 5

    __slots__ = ["__nazwa", "__nasiono_cena", "__skup_cena", "__czas_wegetacji", "__woda_cena"]

    def __init__(self):
        super().__init__(
            Marchew.nazwa
            , Marchew.nasiono_cena
            , Marchew.skup_cena
            , Marchew.czas_wegetacji
            , Marchew.woda_cena
        )

    # bez powstania obiektu
    @staticmethod
    def cenaWSklepie():
        return Marchew.nasiono_cena

    @property
    def getNazwa(self):
        return Marchew.nazwa

    @property
    def getCzasWegetacji(self):
        return Marchew.czas_wegetacji

    @property
    def getCenaSkup(self):
        return Marchew.skup_cena

    @property
    def getCenaWoda(self):
        return Marchew.woda_cena

    def __str__(self):
        return Marchew.nazwa
