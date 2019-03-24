import numpy as np
import time


class Item():
    index = None
    value = None
    weight = None
    fragile = None

    def __init__(self, index, value, weight, fragile):
        self.index = index
        self.value = value
        self.weight = weight
        self.fragile = fragile


def load_file2():
    # matrix = np.zeros((1000, 4), dtype=np.int)
    matrix2 = []
    with open('predmety.txt') as file:
        for index, line in enumerate(file):
            pole = np.asarray(line.strip().split(' '))
            if index == 0:
                number_of_subjects = int(pole[0])
            elif index == 1:
                weight_of_subjects = int(pole[0])
            elif index == 2:
                value_of_subjects = int(pole[0])
            else:
                # matrix[index] = pole
                # numbers = [int(x) for x in numbers]
                item = Item(int(pole[0]), int(pole[1]), int(pole[2]), int(pole[3]))
                matrix2.append(item)

    return matrix2, number_of_subjects, value_of_subjects, weight_of_subjects


def knapsack(W, data, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            if data[i - 1][3] <= w and data[i - 1][1] <= w:
                K[i][w] = max(data[i - 1][0] + K[i - 1][w - data[i - 1][3]],
                              data[i - 1][2] + K[i - 1][w - data[i - 1][1]],
                              K[i - 1][w])
            elif data[i - 1][1] <= w < data[i - 1][3]:
                K[i][w] = max(data[i - 1][0] + K[i - 1][w - data[i - 1][1]], K[i - 1][w])

            elif data[i - 1][3] <= w < data[i - 1][1]:
                K[i][w] = max(data[i - 1][2] + K[i - 1][w - data[i - 1][3]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]

def export_to_file():
    print()

def knapsack_ads_zad2(matrix, number_of_items, count_fragile, weight_knapsack, start_time):
    K = [[[0 for k in range(count_fragile + 1)] for j in range(weight_knapsack + 1)] for i in
         range(number_of_items + 1)]
    arr_index = []

    for l in range(1, number_of_items + 1):
        for m in range(weight_knapsack + 1):
            for n in range(count_fragile + 1):
                if matrix[l - 1].weight > m:
                    K[l][m][n] = K[l - 1][m][n]

                elif matrix[l - 1].fragile > n:
                    K[l][m][n] = K[l - 1][m][n]

                else:
                    values = (K[l - 1][m][n],
                                     K[l - 1][m - matrix[l - 1].weight][n - matrix[l - 1].fragile] + matrix[
                                         l - 1].value)

                    K[l][m][n] = max(values)
                    index = values.index(max(values))
                    print()

    return K[len(K) - 1][len(K[0]) - 1][len(K[0][0]) - 1]


matrix, number_of_subjects, value_of_subjects, weight_of_subjects = load_file2()

start_time = time.time()
print(knapsack_ads_zad2(matrix, number_of_subjects, value_of_subjects, weight_of_subjects, start_time))
print("--- %s seconds ---" % (time.time() - start_time))
