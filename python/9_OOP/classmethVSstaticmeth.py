class ChaiOrder:
    def __init__(self, teaType , sweetness, size):
        self.teaType = teaType
        self.sweetness =sweetness
        self.size = size

    @classmethod
    def fromDict(cls, orderData):
        return cls(
            orderData["teaType"],
            orderData["sweetness"],
            orderData["size"]
        )
    @classmethod
    def fromString(cls, orderString):
        teaType,sweetness,size = orderString.split("-")
        return cls(teaType,sweetness,size)

class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["small","medium","Large"]
    

print(ChaiUtils.is_valid_size("medium"))



order1 = ChaiOrder.fromDict({"teaType":"masala","sweetness":"medium", "size":"small"})

order2 = ChaiOrder.fromString("Ginger-Low-Small")
print(order1.__dict__)
print(order2.__dict__)
