import asyncio

async def f1():
    print(f"print the name of the thing: tonight: ")
    await asyncio.sleep(2)
    print("This is done")

async def f2():
    await asyncio.gather(
        f1()
    )
f2()