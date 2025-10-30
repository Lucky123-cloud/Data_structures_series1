# python handles concurency and async tasks in the following ways:
# 1. Using the asyncio library for asynchronous programming.
# 2. Using threading for concurrent execution of code.
# 3. Using multiprocessing for parallel execution of code.

# lets start with asyncio


import asyncio

async def fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(2)  # Simulate a network delay
    print("Data fetched!")
    return {"data": 123}


async def main():
    print("Main started")
    data = await fetch_data()
    print(f"Received data: {data}")
    print("Main finished")

# Example usage:
if __name__ == "__main__":
    asyncio.run(main())



# runnig mutliple coroutines at once
import asyncio

async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")

async def main():
    await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 1),
        task("Task 3", 3)
    )

asyncio.run(main())
