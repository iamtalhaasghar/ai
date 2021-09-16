def multiply_row_with_scalar(row, scalar):
    return [element * scalar for element in row]


def divide_row_with_scalar(row, scalar):
    from fractions import Fraction
    return [ Fraction(element / scalar ) for element in row]


def add_rows(first_row, second_row):
    if len(first_row) == len(second_row):
        return [first_row[i] + second_row[i] for i in range(len(first_row))]
    else:
        raise Exception('Size of the rows does not match')


def duplicate_matrix(matrix):
    'returns duplicate of a matrix'
    copy = []
    for row in matrix:
        duplicate_row = []
        for element in row:
            duplicate_row.append(element)
        copy.append(duplicate_row)
    return copy


def swap_rows(matrix, index_one, index_two):
    'in-place swapping of two rows of a matrix'
    temp_row = matrix[index_one]
    matrix[index_one] = matrix[index_two]
    matrix[index_two] = temp_row


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            text = str(element)
            print(text, end='\t\t\t')
        print()
    print()

def to_echelon_form(matrix):
    'a function which returns the echelon form of the given input matrix'
    dup_matrix = duplicate_matrix(matrix)
    print_matrix(dup_matrix)
    pivot = (-1, -1)
    for j in range(0, len(dup_matrix[0])):
        for i in range(pivot[0] + 1, len(dup_matrix)):
            if pivot[1] != j:
                h = i
                while h < len(dup_matrix) and dup_matrix[h][j] == 0:
                    h += 1
                if h != len(dup_matrix):
                    if h != i:
                        print('Swapping row#%d with row#%d' % (h + 1, i + 1))
                        swap_rows(dup_matrix, h, i)
                        print_matrix(dup_matrix)
                    pivot = (i, j)
                    if dup_matrix[i][j] != 1:
                        divider = dup_matrix[i][j]
                        print('Dividing row#%d by %d' % (i + 1, divider))
                        dup_matrix[i] = divide_row_with_scalar(dup_matrix[i], divider)
                        print_matrix(dup_matrix)

            else:
                if dup_matrix[i][j] != 0:
                    print(
                        'Multiplying row#%d with %d and adding it to row#%d' % (pivot[0] + 1, -dup_matrix[i][j], i + 1))
                    dup_matrix[i] = add_rows(dup_matrix[i],
                                             multiply_row_with_scalar(dup_matrix[pivot[0]], -dup_matrix[i][j]))
                    print_matrix(dup_matrix)


to_echelon_form([[2, 4, 6], [8, 10, 14], [12, 18, 20]])




