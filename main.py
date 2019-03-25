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


def export_to_file(indices, value_of_knapsack):
    with open('output.txt', 'w') as file:
        file.write(str(value_of_knapsack) + '\n')
        file.write(str(len(indices)) + '\n')
        for index in indices:
            file.write(str(index) + '\n')


def kontrola(arr_index, matrix):
    value = 0
    for index in arr_index:
        for item in matrix:
            if item.index == index:
                value += item.value
    print('Kontrola:', value)


def get_items(K, matrix2, number_of_items, count_fragile, weight_knapsack):
    arr_index = []
    for m in range(number_of_items, 0, -1):
        if not K[m][weight_knapsack][count_fragile] == K[m - 1][weight_knapsack][count_fragile]:
            weight_knapsack = weight_knapsack - matrix2[m - 1].weight
            count_fragile = count_fragile - matrix2[m - 1].fragile
            arr_index.append(m - 1)
    return sorted(arr_index)


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
    return K[len(K) - 1][len(K[0]) - 1][len(K[0][0]) - 1], K


matrix, number_of_subjects, value_of_subjects, weight_of_subjects = load_file2()

start_time = time.time()
value, K = knapsack_ads_zad2(matrix, number_of_subjects, value_of_subjects, weight_of_subjects, start_time)
print(value)

arr_index = get_items(K, matrix, number_of_subjects, value_of_subjects, weight_of_subjects)
print(arr_index)
export_to_file(arr_index, value)
print("--- %s seconds ---" % (time.time() - start_time))