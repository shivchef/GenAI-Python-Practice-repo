# Attribute shadowing
#is_hot in previous code i.e. a variable called attributes of the class

class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()

print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"

print("after changing ", cutting.temperature)
print("Cup size is ", cutting.cup)
print("Direct look into the class ", Chai.temperature)

print(f"/n/n chai strenght before :{Chai.strength}")
del cutting.temperature
del cutting.cup
del Chai.strength

print(f"/n/n chai strenght after :{Chai.strength}")
print("after changing again ", cutting.temperature)
