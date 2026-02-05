import threading
import time

def monitor_task():
    while True:
        print("monitering ...")
        time.sleep(2)
    
t = threading.Thread(target=monitor_task,daemon=False)
t.start()