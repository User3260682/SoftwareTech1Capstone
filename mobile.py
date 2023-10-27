class Phone:
    def __init__(self, Manufacturer, Model, RetailPrice):
        self.__manufact = Manufacturer
        self.__model = Model
        self.__retail_price = RetailPrice

    def get_Manufacturer(self):
        return self.__manufact

    def get_Model(self):
        return self.__model

    def get_RetailPrice(self):
        return self.__retail_price

    def set_Manufacturer(self, string):
        self.__manufact = string

    def set_Model(self, string):
        self.__model = string

    def set_RetailPrice(self, string):
        self.__retail_price = string
