import numpy
import sympy


def is_orthogonal_matrix(vectors):
    matrix = sympy.Matrix(vectors)
    if matrix.inv() == matrix.transpose():
        return True
    return False


basis = numpy.array([[2, 3, 2, -2], [1, 0, 0, 1], [-1, 0, 2, 1], [-1, 2, -1, 1]], dtype=numpy.int64)
basis_vectors = (numpy.transpose(basis))
matrix = sympy.Matrix(basis_vectors)
print('The given basis vectors are:\n', basis_vectors)
print('The matrix constructed from given basis is:\n', matrix)
print('The transpose of given matrix is:\n', matrix.transpose())
print('The inverse of given matrix is:\n', matrix.inv())
if is_orthogonal_matrix(basis_vectors):
    print('The given matrix (shown below) is an orthogonal matrix:\n', matrix)
    print('Multiplying matrix with its transpose also yields identity matrix:\n', matrix * matrix.transpose())
else:
    print('As given matrix is not an orthogonal matrix. Lets convert it first to an orthogonal matrix Q and then '
          'prove Q_transpose = Q_Inverse')
    print('Converting given matrix to orthogonal matrix... ')
    vecs = [sympy.Matrix(i) for i in basis]
    orthogonal_basis = sympy.Matrix.orthogonalize(*vecs,
                                                  normalize=True)
    orthogonal_basis_vectors = numpy.transpose(numpy.array([list(i) for i in orthogonal_basis]))
    print('The orthonormal basis for required matrix are:\n', orthogonal_basis_vectors)
    orthogonal_matrix = sympy.Matrix(orthogonal_basis_vectors)
    print('The required orthogonal matrix is:\n', orthogonal_matrix)
    print('Is orthogonal: ', is_orthogonal_matrix(orthogonal_matrix))
    print('The transpose of given matrix is:\n', orthogonal_matrix.transpose())
    print('The inverse of given matrix is:\n', orthogonal_matrix.inv())
    print('Multiplying matrix with its transpose also yields identity matrix:\n',
          orthogonal_matrix * orthogonal_matrix.transpose())
