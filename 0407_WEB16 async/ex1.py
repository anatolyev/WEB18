import time
from datetime import datetime
import asyncio
import os

COEF = 1

async def dish(num, prepare, wait):
    print(f"Начинаем в {datetime.now().strftime('%H:%M:%S')} "
          f"готовить блюдо №{num} у нас уйдет на это {prepare} минут")
    time.sleep(COEF * prepare)
    print(f"Ждём {wait} минут с {datetime.now().strftime('%H:%M:%S')} "
          f"пока приготовится блюдо №{num}")
    await asyncio.sleep(COEF * wait)
    print(f"Закончили в {datetime.now().strftime('%H:%M:%S')} "
          f"готовить блюдо №{num}\n")

async def main():
    task = [
    asyncio.create_task(dish(2, 5,10)),
    asyncio.create_task(dish(3, 3, 5)),
    asyncio.create_task(dish(1, 2, 3)),
    ]
    await asyncio.gather(*task)

if __name__ == '__main__':
    t0 = time.time()
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    delta = int(time.time() - t0) / COEF
    print(f"Всё готово в {datetime.now().strftime('%H:%M:%S')} "
          f"Всего потрачено {delta} минут.\n")
