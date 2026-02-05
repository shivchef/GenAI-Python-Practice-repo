class TeaLeaf:
    def __init__(self,age):
        self._age = age 
        # "_name" tells us that it is an important property so be cautious while reading and editing it.

    @property
    def age(self):
        return self._age + 2
    
    # this will be responsible how we set the value inside the class
    @age.setter
    def age(self,age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea  leaf age must be between 1 and 5 years")

leaf = TeaLeaf(2)
print(leaf.age)
leaf.age = 6
print(leaf.age)