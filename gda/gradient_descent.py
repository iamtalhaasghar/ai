import numpy

def cost(x, y, w, b, m):
    total_loss = 0.0
    for i in range(m):
        tmp_x = x[i]
        tmp_y = y[i]
        total = (((w * tmp_x + b) - tmp_y) ** 2)
        total_loss += total
    return (total_loss) / (2 * m)


def step_gradient(x, y, w, b, m):
    grad_w, grad_b = 0, 0

    for i in range(m):
        grad_w += -(1/m)*((y[i] - (w * x[i] + b)) * x[i])
        grad_b += -(1/m) * (y[i] - (w * x[i] + b))

    return (grad_w, grad_b)


def gradient(x, y, w, b, m):
    grad_w, grad_b = 0, 0

    for i in range(m):
        grad_w += (((y[i] - (w * x[i]) + b)) * x[i])
        grad_b += ((y[i] - (w * x[i]) + b))

    #return grad_w, grad_b
    return (grad_w / m) , (grad_b / m)

def gda(x, y, m, learning_rate, iterations):

    w = 0
    b = 0

    c_list = []
    b_list = []
    w_list = []
    for i in range(iterations):
        c = cost(x, y, w, b, m)
        c_list.append(c)
        b_list.append(b)
        w_list.append(w)
        print('Iteration', i, c)
        grad_w, grad_b = gradient(x, y, w, b, m)
        w_new = w - (learning_rate * grad_w)
        b_new = b - (learning_rate * grad_b)
        w = w_new
        b = b_new
        print('new parameters', w, b)

    from matplotlib import pyplot as plt
    plt.plot(b_list, w_list, c_list)
    plt.show()
    return w, b

if __name__ == "__main__":
    from sklearn.preprocessing import MinMaxScaler

    #scaler = MinMaxScaler()
    import pandas as pd
    df = pd.read_csv('../ml/data.csv')

    #df[['x', 'y']] = scaler.fit_transform(df[['x', 'y']].values)
    #df['y'] = scaler.fit_transform(df['y'].values)

    x = df['x'].values.tolist()
    y = df['y'].values.tolist()

    print(df['x'])
    print(df['y'])

#    print([(x[i], y[i]) for i in range(len(x))])

    m = len(x)
    learning_rate = 0.35
    iterations = 8
    print('\n>', x,'\n', y)


    print(cost(x,y, 3.9227, -7717.7091, m))

    w, b = gda(x, y, m, learning_rate, iterations)
    # Ŷ = -7717.7091 + 3.9227X
    b = -7717.7091
    w = 3.9227

    print((w * 1910 + b))
    print(w * 1970 + b)
    print(w * 2000 + b)

    print((w * 2010 + b))
    print(w * 2020 + b)
    print(w * 2025 + b)
