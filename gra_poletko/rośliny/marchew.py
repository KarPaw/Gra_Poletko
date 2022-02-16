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

    # @property
    @staticmethod
    def cenaWSklepie():
        # TODO Przydaloby sie zeby to zaciaglao te dane troche lepiej...
        return Marchew.nasiono_cena

    @property
    def getNazwa(self):
        return Marchew.nazwa

    # def __str__(self):
    #     return self.getNazwa
