class InvalidWeaponError(Exception):pass

def bill(type, stock):
    menu  = {"glock43":32, "AK 47": 23}
    try:
        if type not in menu:
            raise InvalidWeaponError("That weapon is not available")
        if not isinstance(stock, int):
            raise TypeError("Number of stocks must be an integer")
        total =menu[type]*stock
        print(f"Your bill for {stock} stock of {type} weapon : Rupees {total}cr.")
    except Exception as e:
        print("Error: ",e)
    finally:
        print("Thank you for purchase. Bharat mata ki jai!")

bill("aug",3)
bill("AK 47",13)
bill("glock",0)
