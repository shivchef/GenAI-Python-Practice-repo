def meinItems():
    yield "pencil"
    yield "eraser"

def rareUsed():
    yield "set square"
    yield "divider"

def fullMenu():
    yield from meinItems()
    yield from rareUsed()

for chai in fullMenu():
    print(chai)

def instrumentBox():
    try:
        while True:
            order = yield "Waiting for fetching from box"
    except:
        print("box closed, no more fetching")

stall = instrumentBox()
print(next(stall))
stall.close()       #cleanup the memory