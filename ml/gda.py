import pandas as pd

data = pd.read_csv('data.csv')
data['x'] = data['x'] / 100

theta_one = theta_zero = 0
learning_rate = 0.001
m = len(data['x'])
iterations = 12
for i in range(iterations):
    cost = sum(((theta_one * data['x'] + theta_zero) - data['y']) ** 2) / (2 * m)
    delta_theta_zero = sum((theta_one * data['x'] + theta_zero) - data['y']) / m
    delta_theta_one = sum(((theta_one * data['x'] + theta_zero) - data['y']) * data['x']) / m
    print('After iteration',i,'cost is', cost)
    theta_one = theta_one - learning_rate * delta_theta_one
    theta_zero = theta_zero - learning_rate * delta_theta_zero

theta_zero = -7717.7091
theta_one = 3.9227

print('Values of theta_zero & theta_one after', iterations, 'iterations are', theta_zero, theta_one, 'respectively')
# prediction
for i in [2010, 2020, 2025]:
    print('Median price in', i, 'will be',theta_one * i + theta_zero)
