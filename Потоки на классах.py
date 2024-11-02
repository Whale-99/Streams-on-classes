from threading import Thread
from time import sleep

# Класс Knight, наследующий от Thread
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        days = 0
        while enemies > 0:
            sleep(1)
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f"{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.")
        print(f"{self.name} одержал победу спустя {days} день(дня)!")

# Создание экземпляров класса Knight
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения всех битв
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
