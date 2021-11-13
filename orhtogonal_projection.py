# Given a full column rank 4x2 matrix, B=[b1 b2].
# Create a python code that would return the matrix P,
# the matrix representation "π : R4 -> span{b1, b2}"
# We can calculate matrix of Orthogonal Projection using:
# P(π) = B * (1 / (B_t * B)) * B_t where B_t means transpose of B

import numpy
import sympy


def get_orthogonal_projection_matrix(basis_matrix):
    b_transpose = numpy.transpose(basis_matrix)
    p = numpy.matmul(numpy.matmul(basis_matrix, numpy.linalg.inv(numpy.matmul(b_transpose, basis_matrix))),
                     b_transpose)
    print('The desired matrix for orthogonal projection is: ')
    print(p)


def main():
    basis = numpy.array([[1, 1, 1, 1], [2, 2, 2, 2]])
    basis_matrix = numpy.transpose(basis)
    print('The matrix constructed from given basis vectors is:\n', basis_matrix)
    rank = numpy.linalg.matrix_rank(basis_matrix)
    print('The rank of matrix is: ', rank)
    # check if the matrix is full col. rank matrix or not
    if numpy.shape(basis_matrix)[1] == rank:
        print('Thus, The matrix IS already a full column rank matrix.')
        get_orthogonal_projection_matrix(basis_matrix)
    else:
        # detect and remove linearly dependent columns
        print('The matrix is NOT a full column rank matrix.')
        rref, pivots = sympy.Matrix(basis_matrix).rref()
        print('The reduced row echelon form of the matrix is:\n', rref)
        print('The pivots are in these columns:', pivots)
        lin_ind_basis = []
        for p in pivots:
            lin_ind_basis.append(basis[p])
        print('The linearly independent basis are:\n', lin_ind_basis)
        basis_matrix = numpy.transpose(lin_ind_basis)
        print('The new matrix after removing dependent columns is:\n', basis_matrix)
        get_orthogonal_projection_matrix(basis_matrix)


if __name__ == "__main__":
    main()
