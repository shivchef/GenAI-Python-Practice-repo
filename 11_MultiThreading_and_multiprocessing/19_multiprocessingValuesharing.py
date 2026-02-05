from multiprocessing import Process , Value


def shared_value(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)

    Processes=[Process(target=shared_value, args=(counter, ))for _ in range(4)]
    [p.start() for p in Processes]
    [p.join() for p in Processes]

    print("Final counter value is  ", counter.value)
#here the value is shared among all the 4 processes 