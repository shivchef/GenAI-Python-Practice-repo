seat_type = input("Please choose your preferred seat type (sleeper/AC/general/luxury):").lower()


match seat_type :
    case "sleeper" :
        print("Sleeper contains beds but no AC")
    case "AC":
        print("AC is included with sleeper facilities")

    case "general" :
        print("no seats for sleeping ")
    case "luxury":
        print("all facilites of AC along with meals and seperate room.")
    case _:
        print("Invalid seat type.")