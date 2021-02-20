class Config():
    __config = None
    __token = ""

    def __init__(self):
        self.__token = "1652367342:AAEQa_ReDHQSVnK6Q9A7Ks67anJd6X7VlXI"

    @classmethod
    def getInstance(cls):
        if not cls.__config:
            cls.__config = Config()
        return cls.__config

    def getToken(self):
        return self.__token