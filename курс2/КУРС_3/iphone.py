class Phone:
    def __init__(self, number,model,weight="80"):
        self.__number__=number
        self.__model__=model
        self.weight=weight
    
    def printg_data(self):
        print(self.__number__)
    
number_mother=Phone("+78005553535","apple")
number_my=Phone("+74567942645","apple","800")
number_brouther=Phone("+79988531225","samsung","884")
number_brouther.printg_data()
number_my.printg_data()
number_mother.printg_data()