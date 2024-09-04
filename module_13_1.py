import asyncio
import time

async def start_strongman(name, power):
    start_time = time.time()  # Засекаем время начала соревнований
    print(f'Силач {name} начал соревнования.')
    for i in range(1,6):
        await asyncio.sleep(5 / power)  # Задержка обратно пропорциональная силе
        print(f'Силач {name} поднял {i} шар.')
    end_time = time.time()  # Засекаем время окончания соревнований
    print(f'Силач {name} закончил соревнования в {end_time - start_time:.2f} секунд.')

async def start_tournament():
    tasks = [
        start_strongman('Pasha', 3),
        start_strongman('Denis', 4),
        start_strongman('Apollon', 5)
    ]
    await asyncio.gather(*tasks)

def main():
    asyncio.run(start_tournament())

if __name__ == "__main__":
    main()