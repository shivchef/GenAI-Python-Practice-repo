import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    return f"Your data is encrypted {data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool :
        result = await loop.run_in_executor(pool,encrypt,"9277499827893")
    print(result)

#this main section is required whenever we use Processes 

if __name__ == "__main__":
    asyncio.run(main())
