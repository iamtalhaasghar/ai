import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas

train_data = pandas.read_csv('train.csv')
train_data.fillna(0, inplace=True)
print(train_data.head)
train_features = train_data[['x']]
print(train_features)
train_labels = train_data[['y']].values.tolist()
print(train_labels)

test_data = pandas.read_csv('test.csv')
test_data.fillna(0, inplace=True)
test_features = train_data[['x']].values.tolist()
test_labels = train_data[['y']].values.tolist()

ai = linear_model.LinearRegression()
ai.fit(train_features, train_labels)
plt.scatter(test_features, test_labels)
plt.plot(test_features, ai.predict(test_features))
plt.show()
