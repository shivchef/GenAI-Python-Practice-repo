from multiprocessing import Process, Queue

def prepare_weapon(queue):
    queue.put("Weapon is prepared!")

if __name__ == "__main__":
    queue = Queue()

    p = [Process(target=prepare_weapon, args=(queue, )) for _ in range(2)]
    [t.start() for t in p]
    [t.join() for t in p]
    print(queue.get())
