#GIL Global intrepreter lock using threading
import threading
import time

def fetch_weapon():
    print(f"{threading.current_thread().name} Started fetching..")
    count = 0 
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished fetching . .")

thread1 = threading.Thread(target=fetch_weapon,name="M416")
thread2 = threading.Thread(target=fetch_weapon, name ="AUG")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()

end = time.time()

print(f"total time taken: {end-start:2f} seconds")