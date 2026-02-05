# chai = "kashmiri"

# def prepare_chai(order):
#     print("preparing",order)

# prepare_chai(chai)

# CHAI = [1,2,4]

# def edit_chai(cup):
#     cup[1] = 43

# edit_chai(CHAI)
# print(CHAI) #Lists are mutable date type


#Two types of arguments can be passed in python 
# * args  2. *kwargs



def make_chai(tea, milk, sugar):
    print(tea,milk,sugar)

make_chai("Darjeeling", "yes","low") #positional
make_chai(tea="Green",sugar = "high", milk = "No")


def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras",extras)
special_chai("Cinnamon", "Cardmom", sweetner = "Honey", foam="Yes") 

def chai_order(order=None):
    if order is None:
        order = []
    print(order)
    
chai_order()
chai_order() 
#it will return that the lists are empty both time as it will update the order if it is none
