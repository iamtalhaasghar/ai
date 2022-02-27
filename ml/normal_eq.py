import pandas as pd
data = pd.read_csv('volume.csv')
vol = data['volume']
data = data.drop(['serial', 'volume'], axis = 1)
data.insert(0, 'theta_0', 1)
import sympy, numpy
x = sympy.Matrix(data).transpose()
# print(x)
# print( sympy.Matrix.inv(x.multiply(x.transpose())).multiply(x).multiply(sympy.Matrix(vol)))

x = sympy.Matrix(data)
# print(x)
theta = sympy.Matrix.inv(x.transpose().multiply(x)).multiply(x.transpose()).multiply(sympy.Matrix(vol))

print(theta.transpose())