import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = pd.read_csv('volume.csv')
scaler = MinMaxScaler()
data[['girth', 'height']] = scaler.fit_transform(data[['girth', 'height']].values)
data['volume'] = scaler.fit_transform(data[['volume']].values)

theta_one = theta_zero = theta_two = 0
iterations = 25
a = 0.001
m = len(data['volume'])
for i in range(iterations):
    #print('Parameters',theta_zero, theta_one, theta_two)
    cost = sum((( theta_one*data['girth'] + theta_two * data['height'] + theta_zero) - data['volume']) ** 2) / (2 * m)

    delta_zero = sum((theta_one*data['girth'] + theta_two * data['height']+theta_zero) - data['volume'])/m
    delta_one = sum(((theta_one*data['girth'] + theta_two * data['height']+theta_zero) - data['volume']) * data['girth']) /m
    delta_two = sum(((theta_one*data['girth'] + theta_two * data['height']+theta_zero) - data['volume']) * data['height']) /m

    print('After iteration',i,'cost is', cost)
    theta_one = theta_one - a * delta_one
    theta_zero = theta_zero - a * delta_zero
    theta_two = theta_two -a * delta_two
print('Optimum Values of theta_zero, theta_one & theta_two after', iterations, 'iterations are\n',
      theta_zero, theta_one, theta_two, 'respectively')
