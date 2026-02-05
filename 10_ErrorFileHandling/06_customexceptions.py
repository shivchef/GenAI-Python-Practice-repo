class OutOfWeaponError(Exception):
    pass

def create_weapon(gunPowder,metal):
    if gunPowder == 0 or metal == 0:
        raise OutOfWeaponError("Missing key ingredient ")
    print("weapon is ready")

create_weapon(0,2)
