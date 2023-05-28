from random import randint
import re
import os
import numpy as np


def prepare_matrix():
    '''генерирует случайную матрицу'''
    n = randint(1, 10)
    m = randint(1, 10)
    print(f'Размер матрицы: {m}x{n}')
    matrix = np.array([[randint(-10, 10) for j in range(m)] for i in range(n)])
    return matrix


def get_sums(matrix):
    '''получает суммы положительных и отрицательных чисел'''
    print("Исходная матрица")
    print(np.array2string(matrix))
    print("#" * 20)
    negatives = np.abs(np.where(matrix < 0, matrix, 0).sum(0))
    print(f'отрицательные: {negatives}')
    positives = np.where(matrix > 0, matrix, 0).sum(0)
    print(f'положительные: {positives}')
    return negatives, positives


def calculate_diffs(negatives, positives):
    '''вычисляет, сколько необходимо добавить к столбцам'''
    diffs = []
    for i in range(len(negatives)):
        diff = negatives[i] - positives[i]
        diffs.append(diff)
    print(f'разницы: {diffs}')
    return diffs


def write_result(result_str):
    '''записывает выходную строку в файл'''
    output_str = re.sub("[\[\]]", " ", result_str)
    with open("output.txt", "w+") as f:
        f.write(output_str)


def main():
    matrix = prepare_matrix()
    # сохраняем исходную матрицу для вывода в файл
    source_matrix_str = np.array2string(matrix)
    negatives, positives = get_sums(matrix)
    diffs = calculate_diffs(negatives, positives)
    # добавляем строку с вычисленными элементами к матрице
    matrix = np.vstack([matrix, diffs])
    # следующие 2 строчки только для наглядного вывода, не обязательны
    negatives, positives = get_sums(matrix)
    diffs = calculate_diffs(negatives, positives)
    processed_matrix_str = np.array2string(matrix)
    result_str = source_matrix_str + os.linesep * 5 + processed_matrix_str
    result_str = re.sub('[\[\]]', "", result_str)
    write_result(result_str)

if __name__ == '__main__':
    main()
