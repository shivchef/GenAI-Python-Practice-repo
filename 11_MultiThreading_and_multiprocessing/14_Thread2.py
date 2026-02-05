import threading
import time

def prepareWeapon(type_,wait_time):
    print(f"{type_} weapon: assembling..")
    time.sleep(wait_time)
    print(f"{type_} weapon: Ready.")

t1 = threading.Thread(target=prepareWeapon,args=("Mk14",3))
t2 = threading.Thread(target=prepareWeapon,args=("Ak 47",2))

t1.start()
t2.start()
t1.join()
t2.join()