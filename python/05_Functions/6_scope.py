def serve_chai():
    chai_type = "coffee" #local scope
    print(f"{chai_type} this is local to serve_chai")

chai_type ="lemon"
serve_chai()
print(f"{chai_type} this is outside of serve_chai")


def chai_counter():
    chai_order ="Lemon" #Enclosing scope
    def print_order():
        chai_order = "ginger"
        print("Inner: ", chai_order)
    print_order()
    print("Outer:", chai_order)
chai_order = "maggie" #global scope
print("Global:", chai_order)


chai_counter()