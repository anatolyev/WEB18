import time
from datetime import datetime


COEF = 1

def dish(num, prepare, wait):
    print(f"Начинаем в {datetime.now().strftime('%H:%M:%S')} "
          f"готовить блюдо №{num} у нас уйдет на это {prepare} минут")
    time.sleep(COEF * prepare)
    print(f"Ждём {wait} минут с {datetime.now().strftime('%H:%M:%S')} "
          f"пока приготовится блюдо №{num}")
    time.sleep(COEF * wait)
    print(f"Закончили в {datetime.now().strftime('%H:%M:%S')} "
          f"готовить блюдо №{num}\n")

def main():
    dish(1, 2, 3)
    dish(2, 5,10)
    dish(3, 3, 5)

if __name__ == '__main__':
    t0 = time.time()
    main()
    delta = int(time.time() - t0) / COEF
    print(f"Всё готово в {datetime.now().strftime('%H:%M:%S')} "
          f"Всего потрачено {delta} минут.\n")
