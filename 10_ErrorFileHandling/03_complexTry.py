def fetch_weapon(nameWeapon):
    try:
        print(f"Fetching {nameWeapon} ...")
        if nameWeapon == 'unknown':
            raise ValueError("We dont have that weapon")
    except ValueError as e:
        print('Error: ',e)
    else:
        print(f"{nameWeapon} is fetched")
    finally:
        print("Next order?")

fetch_weapon("unknown")
