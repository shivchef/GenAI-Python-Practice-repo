class Chai:
    origin = "India"  #This is colled properties


print(Chai.origin)

Chai.is_hot = True

print(Chai.is_hot)

# creating Objects from class Chai

masala = Chai()
print(masala.origin)
print(masala.is_hot)

masala.is_hot = False
print("Class : ", Chai.is_hot)
print("masala : ",masala.is_hot)
masala.flavour = "margarita"
print(masala.flavour)
