import logging
import argparse
import json
import sys

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data is None:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            self.data = data
        logging.info(f"Создана матрица: {self.__repr__()}")

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            logging.error("Попытка сложения матриц разных размеров")
            raise ValueError("Matrices must have the same dimensions")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        logging.info("Матрицы успешно сложены")
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            logging.error("Ошибка в размерах матриц для умножения")
            raise ValueError("Number of columns of the first matrix must be equal to the number of rows of the second matrix")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
        logging.info("Матрицы успешно умножены")
        return result

def create_matrix_from_args():
    parser = argparse.ArgumentParser(description="Математические операции с матрицами")
    parser.add_argument("--rows", type=int, required=True, help="Количество строк в матрице")
    parser.add_argument("--cols", type=int, required=True, help="Количество столбцов в матрице")
    parser.add_argument("--data", type=json.loads, required=False, help="Данные матрицы в формате JSON")

    args = parser.parse_args()
    return Matrix(args.rows, args.cols, args.data)

if __name__ == "__main__":
    matrix = create_matrix_from_args()
    print(matrix)
#python homework15.3.py --rows 2 --cols 3 --data "[[1,2,3],[4,5,6]]"