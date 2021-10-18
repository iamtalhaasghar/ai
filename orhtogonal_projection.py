# Given a full column rank 4x2 matrix, B=[b1 b2].
# Create a python code that would return the matrix P,
# the matrix representation "π : R4 -> span{b1, b2}"
# We can calculate matrix of Orthogonal Projection using:
# P(π) = B * (1 / (B_t * B)) * B_t where B_t means transpose of B

import numpy

b = [[1, 0],
      [1, 1],
      [1, 2],
      [1, 2]]

# check if the matrix is full col. rank matrix or not
if numpy.shape(b)[1] == numpy.linalg.matrix_rank(b):
      b_transpose = numpy.transpose(b)
      p = numpy.matmul(numpy.matmul(b,  numpy.linalg.inv(numpy.matmul(b_transpose, b))), b_transpose)
      print(p)
else:
      pass


