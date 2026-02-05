from multiprocessing import Process
import time
def arrange_weapon(type):
    print(f"Start of {type} weapon arrangement")
    time.sleep(3)
    print(f"End of {type} weapon arrangement")

if __name__ == "__main__":
    weapon_maker = [
        Process(target=arrange_weapon,args=(f"Weapon maker #{i+1}", ))
        for i in range(3)
    ]


    # Start all process
    for p in weapon_maker:
        p.start()

    # wait for all to complete
    for p in weapon_maker:
        p.join()

    print("All weapons arranged")


