# Домашнее задание по теме "Логирование"
# Код создан в учебных целях с полными комментариями для себя.

import unittest  # Импортируем модуль unittest для проведения юнит-тестирования
import logging  # Импортируем модуль logging для регистрации событий в файле логов
from rt_with_exceptions import Runner  # Импортируем класс Runner из модуля rt_with_exceptions

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,  # Устанавливаем уровень логирования на INFO, чтобы регистрировать информационные сообщения
    filename='runner_tests.log',  # Указываем файл для записи логов
    filemode='w',  # Открываем файл в режиме записи с очисткой файла перед записью
    encoding='UTF-8',  # Устанавливаем кодировку для записи в файл
    format='%(asctime)s | %(levelname)s | %(message)s'  # Определяем формат записи: время, уровень логирования, сообщение
)

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Атрибут, указывающий, можно ли замораживать тесты в данном классе

    def test_walk(self):
        try:
            runn = Runner("Олег", speed=-5)  # Создаем объект Runner с отрицательной скоростью
            for _ in range(10):  # Выполняем действие walk десять раз
                runn.walk()  # Вызываем метод walk для объекта Runner
            logging.info('"test_walk" выполнен успешно')  # Регистрируем информационное сообщение о завершении теста
            self.assertEqual(runn.distance, 50)  # Проверяем, что расстояние составляет 50 единиц
        except ValueError as e:  # Перехватываем исключение ValueError
            logging.warning(f"Неверная скорость для Runner: {str(e)}")  # Регистрируем предупреждение о неправильной скорости

    def test_run(self):
        try:
            runn = Runner(123, speed=10)  # Создаем объект Runner с неверным типом данных для имени
            for _ in range(10):  # Выполняем действие run десять раз
                runn.run()  # Вызываем метод run для объекта Runner
            logging.info('"test_run" выполнен успешно')  # Регистрируем информационное сообщение о завершении теста
            self.assertEqual(runn.distance, 100)  # Проверяем, что расстояние составляет 100 единиц
        except TypeError as e:  # Перехватываем исключение TypeError
            logging.warning(f"Неверный тип данных для объекта Runner: {str(e)}", exc_info=True)  # Регистрируем предупреждение о неверном типе данных

    def test_challenge(self):
        runn1 = Runner("Никита")  # Создаем объект Runner с именем "Никита"
        runn2 = Runner("Алиса")  # Создаем объект Runner с именем "Алиса"
        for _ in range(10):  # Выполняем действия run и walk десять раз
            runn1.run()  # Вызываем метод run для объекта Runner
            runn2.walk()  # Вызываем метод walk для объекта Runner
        self.assertNotEqual(runn1.distance, runn2.distance)  # Проверяем, что расстояния отличаются

if __name__ == "__main__":
    unittest.main()  # Запускаем тестирование, если запущена основная функция
