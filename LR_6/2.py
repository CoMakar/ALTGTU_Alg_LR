import random as rnd
import lib.list_functions as lfunc
from lib.matrix_functions import print_matrix
from typing import List


def count_not_0_col(matrix: List[List]):
    not_0_col_count = len(matrix[0])

    for col_idx in range(len(matrix[0])):
        for row_idx in range(len(matrix)):
            if matrix[row_idx][col_idx] == 0:
                not_0_col_count -= 1
                break

    return not_0_col_count


def calc_characteristics(matrix: List[List]):
    characteristics = [[-1, 0] for _ in range(len(matrix))]
    # [0] -> row index
    # [1] -> characteristic

    for row_idx in range(len(matrix)):
        characteristics[row_idx][0] = row_idx
        for col_idx in range(len(matrix[0])):
            elem = matrix[row_idx][col_idx]
            if elem > 0 and elem % 2 == 0:
                characteristics[row_idx][1] += elem

    return characteristics


def sort_by_characteristic(matrix: List[List], characteristics: list):
    characteristics = lfunc.insort(characteristics, lambda x, y: x[1] > y[1])

    matrix_sorted = []

    for pair in characteristics:
        matrix_sorted.append([col for col in matrix[pair[0]]])

    return matrix_sorted


def main():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    zeros_amount = 3

    if rows <= 0 or columns <= 0:
        print("Matrix should contain at least one row and one column")
        return

    matrix = [
        [rnd.randint(-100, 100) for i in range(columns)] for j in range(rows)
    ]

    for _ in range(zeros_amount):
        matrix[rnd.randint(0, rows - 1)][rnd.randint(0, columns - 1)] = 0

    print_matrix(matrix)

    characteristics = calc_characteristics(matrix)

    print("Number of columns without zeros:", count_not_0_col(matrix))
    print("Characteristics values of rows [row, value]:")
    print_matrix(characteristics)
    print("Sorted by characteristics  values:")
    print_matrix(sort_by_characteristic(matrix, characteristics))


if __name__ == "__main__":
    main()
