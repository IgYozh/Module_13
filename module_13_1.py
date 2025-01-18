import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    t = 1 / power
    for i in range(5):
        await asyncio.sleep(t)
        print(f"Силач {name} поднял {i+1} шар.")
    print(f"Силач {name} закончил соревнования")

async def start_tournament():
    task1 = asyncio.create_task(start_strongman(name='Паша', power=3))
    task2 = asyncio.create_task(start_strongman(name='Денис', power=2))
    task3 = asyncio.create_task(start_strongman(name='Аполлон', power=1))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())

# 'Pasha', 3
# 'Denis', 4
# 'Apollon', 5
