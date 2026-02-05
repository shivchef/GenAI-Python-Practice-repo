import threading
import time
#This is the example for concurrency!

def take_orders():
    for i in range(1,4):
        print(f"taking order for #{i}")
        time.sleep(2)

def arrange_weapon():
    for i in range(1,4):
        print(f"Arranging weapon #{i}")
        time.sleep(3)

#create threads
order_thread = threading.Thread(target=take_orders)
arrange_thread = threading.Thread(target=arrange_weapon)

order_thread.start()
arrange_thread.start()

#for waiting to both threads to finish execution

order_thread.join()
arrange_thread.join()

print(f"All order taken and weapons arranged!..")

