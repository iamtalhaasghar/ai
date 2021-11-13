def multiply_row_with_scalar(row, scalar):
    """elementary operation which allows you to multiply a vector .i.e. vector row of matrix in this case with a
    scalar """
    return [element * scalar for element in row]


def divide_row_with_scalar(row, scalar):
    """elementary operation which allows you to divide a vector .i.e. vector row of matrix in this case with a scalar"""
    from fractions import Fraction
    return [Fraction(element / scalar).limit_denominator() for element in row]


def add_rows(first_row, second_row):
    """elementary operation which allows you to add two vectors .i.e. two rows of a matrix in this case"""
    if len(first_row) == len(second_row):
        # number of entries in both rows shall be equal
        return [first_row[i] + second_row[i] for i in range(len(first_row))]
    else:
        # addition of two rows undefined if number of entries are not equal
        raise Exception('Size of the rows does not match')


def swap_rows(matrix, index_one, index_two):
    """elementary operation which allows in-place swapping of two rows of a matrix"""
    temp_row = matrix[index_one]
    matrix[index_one] = matrix[index_two]
    matrix[index_two] = temp_row


def print_matrix(matrix):
    """print rows of the matrix in humand readable form"""
    for row in matrix:
        for element in row:
            text = str(element)
            print('%-30s' % text, end='')
        print()
    print('-' * 10)


def to_echelon_form(dup_matrix, reduce_as_well=False):
    """a function which returns the echelon form of the given input matrix and reduces it as well if "reduce_as_well"
    is set to True """

    print('Original Matrix')
    print_matrix(dup_matrix)
    pivot = (-1, -1)  # assume that currently there is no pivot found yet
    for j in range(0, len(dup_matrix[0])):  # iterate over columns of the matrix
        for i in range(pivot[0] + 1,
                       len(dup_matrix)):  # skip rows which already have a pivot and iterate over the rest of the rows
            if pivot[1] != j:
                # find the pivot element in current column
                h = i
                while h < len(dup_matrix) and dup_matrix[h][j] == 0:
                    # skip zeros
                    h += 1
                if h != len(dup_matrix):
                    # first non zero element found
                    if h != i:
                        # swap with the current row
                        print('After Swapping row#%d with row#%d we have' % (h + 1, i + 1))
                        swap_rows(dup_matrix, h, i)
                        print_matrix(dup_matrix)
                    pivot = (i, j)  # now current row,col is the pivot element
                    if dup_matrix[i][j] != 1:
                        # convert pivot element to 1
                        divisor = dup_matrix[i][j]
                        print('After Dividing row#%d by %s we have' % (i + 1, divisor))
                        dup_matrix[i] = divide_row_with_scalar(dup_matrix[i], divisor)
                        print_matrix(dup_matrix)

            else:
                # pivot element was already found
                if dup_matrix[i][j] != 0:
                    # use pivot element to convert rest of the entries to zero
                    print('After Multiplying row#%d with %s and adding it to row#%d we have' % (
                        pivot[0] + 1, -dup_matrix[i][j], i + 1))
                    dup_matrix[i] = add_rows(dup_matrix[i],
                                             multiply_row_with_scalar(dup_matrix[pivot[0]], -dup_matrix[i][j]))
                    print_matrix(dup_matrix)

        if reduce_as_well:
            # if user wants to further reduce the row echelon form
            for i in range(pivot[0] - 1, -1, -1):  # move backwards from the pivot
                if dup_matrix[i][j] != 0:
                    # use pivot element to convert rest of the entries to zero
                    print('After Multiplying row#%d with %s and adding it to row#%d we have' % (
                        pivot[0] + 1, -dup_matrix[i][j], i + 1))
                    dup_matrix[i] = add_rows(dup_matrix[i],
                                             multiply_row_with_scalar(dup_matrix[pivot[0]], -dup_matrix[i][j]))
                    print_matrix(dup_matrix)


def create_matrix_of_random_size(min_size=3, max_size=6, min_element=0, max_element=99):
    """returns a matrix M of size (m,n) where min_size <= no. of rows or cols <= max_size and min_element <= element
    <= max_element """

    import random
    m = random.randint(min_size, max_size)  # random number of rows
    n = random.randint(min_size, max_size)  # random number of cols
    print('Creating random elements for matrix of size (%d, %d)...' % (m, n))
    test_matrix = []
    for i in range(m):
        random_row = []
        for j in range(n):
            random_row.append(random.randint(min_element, max_element))
        test_matrix.append(random_row)

    return test_matrix


# use this if you want to test the algorithm with your own matrix
test_matrix = [[12, 4, 6, 21],
               [8, 10, 14, 45],
               [12, 18, 20, 45],
               [12, 18, 20, 78],
               [12, 18, 20, 10]]

random_matrix = create_matrix_of_random_size()

to_echelon_form(random_matrix, reduce_as_well=True)
