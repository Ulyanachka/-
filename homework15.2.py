import logging
import argparse

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height is not None else width
        logging.info(f"Создан {self.__repr__()}")

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):  # Сложение
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)

    def __sub__(self, other):  # Вычитание
        new_width = abs(self.width - other.width)
        new_height = abs(self.height - other.height)
        return Rectangle(new_width, new_height)

    def __lt__(self, other):  # <
        return self.width * self.height < other.width * other.height

    def __le__(self, other):  # <=
        return self.width * self.height <= other.width * other.height

    def __eq__(self, other):  # ==
        return self.width * self.height == other.width * other.height

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

def main(width, height=None):
    rect1 = Rectangle(width, height)
    print(rect1)
    logging.info(f"Периметр: {rect1.perimeter()}, Площадь: {rect1.area()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Работа с прямоугольниками")
    parser.add_argument("width", type=float, help="Ширина прямоугольника")
    parser.add_argument("--height", type=float, help="Высота прямоугольника, если не указана, считается равной ширине")

    args = parser.parse_args()


#python homework15.2.py 4 --height 5