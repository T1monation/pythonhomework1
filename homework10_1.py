class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        matrix_string = f'Матрица вида:\n'
        for el in self.matrix_list:
            matrix_string += f'|{el}|\n'
        return matrix_string

    def __add__(self, other):
        temp_list = []
        for i in range(len(self.matrix_list)):
            if range(len(self.matrix_list)) != range(len(other.matrix_list)):
                raise ValueError('В слогаемых матрицах не совпадают количество строк')
            else:
                temp_list.append([])
                for j in range(len(self.matrix_list[i])):
                    if range(len(self.matrix_list[i])) != range(len(other.matrix_list[i])):
                        raise ValueError('В слогаемых матрицах не совпадают количество столбцов')
                    else:
                        temp_list[i].append(self.matrix_list[i][j] + other.matrix_list[i][j])
        return Matrix(temp_list)


some_matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
some_matrix_2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
some_matrix_3 = Matrix([[9, 8, 7, 6], [6, 5, 4, 3], [3, 2, 1, 0]])
some_matrix_4 = Matrix([[1, 2, 3, 4], [4, 5, 6, 5], [7, 8, 9, 6]])
some_matrix_5 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(some_matrix_1)
# some_matrix = some_matrix_1 + some_matrix_2
some_matrix = some_matrix_3 + some_matrix_4
print(some_matrix)
# Несовпадение количества столбцов:
# some_matrix = some_matrix_3 + some_matrix_2
# Несовпадение количества строк:
# some_matrix = some_matrix_3 + some_matrix_5
