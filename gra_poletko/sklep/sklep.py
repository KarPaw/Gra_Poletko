

class Sklep:
    __slots__ = ["__ziarna", "__srodkiOchronyRoslin"]

    def __init__(self):
        self.__ziarna = None
        self.__srodkiOchronyRoslin = None

    def setZiarna(self, slownikZiarnoCena:dict):
        self.__ziarna = slownikZiarnoCena

    @property
    def getZiarna(self):
        return self.__ziarna

    # def setSrodkiOchrony(self, slownikSrodkowOchronyZCenami):
    #     self.__srodkiOchronyRoslin = slownikSrodkowOchronyZCenami



