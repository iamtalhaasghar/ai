import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas

df = pandas.read_csv('data.csv')
df.fillna(0, inplace=True)
x = df[['x']]
y = df[['y']]

ai = linear_model.LinearRegression()
ai.fit(x, y)
plt.scatter(x, y)
plt.plot(x, ai.predict(x))
plt.show()
