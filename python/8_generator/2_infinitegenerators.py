#infinite generators

def chai_code():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1
        

refill = chai_code()
user2 = chai_code()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))

    