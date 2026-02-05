def process_order(item, quantity):
    try:
        price = {"glock": 10}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that gun is not on arsenal")
    except TypeError:
        print("Quantity must be number.")

process_order("Kar98",3)
process_order("glock","nine")