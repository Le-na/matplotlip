from random import choice

class RandomWalk():
    """ Класс для генерирования слуйчайнных блуужданий"""

    def __init__(self, num_points=50000):
        """ Инициализирует атрибуты блужданий"""
        self.num_points = num_points

        # Все блуждания начинаются с точки (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ Вычисляет вссе точки блуждания"""
        while len(self.x_values) < self.num_points:
            # Определение направления и длины перемещения
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Отклонение нулевых перемещений
            if x_step == 0 and y_step == 0:
                continue

            # Вычисленик следующих значений x и y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            x = self.x_values.append(x)
            y = self.y_values.append(y)
