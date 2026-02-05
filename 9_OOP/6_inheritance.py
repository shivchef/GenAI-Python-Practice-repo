class BaseChai:
    def __init__(self,type_):
        self.type = type_
    def prepare(self):
        print(f"Preparing {self.type} chai....")


class MasalaChai(BaseChai):
    def add_spices(self):
        print("adding cloves and ginger")

class ChaiShop:
    chai_cls = BaseChai         #Composition here chai_cls will take reference to BaseChai

    def __init__(self):
        self.chai = self.chai_cls("regular")
    
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()

fancy.serve()
shop.serve()
fancy.chai.add_spices()  
#we cannot use chai_cls.add_spices() because of constructor FancyChaiShop is initialize from.
fancy.chai.prepare()

