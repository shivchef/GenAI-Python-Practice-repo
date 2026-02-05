from multiprocessing import Process
import time

def complexProcess():
    total = 0
    print("Processesing started:")
    for i in range(10**7):
        total += 1
    print("DOne!")

if __name__ == "__main__":
    start = time.time()
    p = [Process(target=complexProcess) for _ in range(2)]
    [t.start() for t in p]
    [t.join() for t in p]
    end = time.time()
    print(f'Total time it took to process 10**7 is {end - start:.2f}')
