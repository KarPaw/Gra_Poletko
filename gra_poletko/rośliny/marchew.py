from gra_poletko.rośliny.roślina import Roślina


class Marchew(Roślina):

    __slots__ = ["__nazwa", "__nasiono_cena", "__skup_cena", "__czas_wegetacji", "__woda_cena"]

    @staticmethod
    def wartosci():
        nazwa = "Marchew"
        nasiono_cena = 100
        skup_cena = 150
        czas_wegetacji = 3
        woda_cena = 5

        return [nazwa, nasiono_cena, skup_cena, czas_wegetacji, woda_cena]

    def __init__(self):
        w = self.wartosci()
        super().__init__(w[0], w[1], w[2], w[3], w[4])

    # @property
    @staticmethod
    def cenaWSklepie():
        #TODO Przydaloby sie zeby to zaciaglao te dane troche lepiej...
        return 100

    # def __str__(self):
    #     return self.getNazwa
