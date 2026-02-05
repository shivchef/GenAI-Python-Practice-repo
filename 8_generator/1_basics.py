def serve_coffee():
    yield "Cup 1:Dark coffee"
    yield "Cup 2:capecchino"
    yield "Cup 3:regular coffee"

stall = serve_coffee()

for cup in stall:
    print(cup)


def get_chai_list():
    return ["cup1","cup2","cup3"]

#generator function
def get_chai():
    yield "cup1"
    yield "cup2"
    yield "cup3"

chai = get_chai()
print(next(chai))
print(next(chai))
print(next(chai))
#gives error below statement
print(next(chai))