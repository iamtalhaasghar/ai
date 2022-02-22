import numpy

def cost(x, y, w, b, m):
    total_loss = 0.0
    for i in range(m):
        total_loss += (y[i] - (w * x[i] + b)) ** 2
    return total_loss / 2 * m

def gradient(x, y, w, b, m):
    grad_w, grad_b = 0, 0

    for i in range(m):
        grad_w += (y[i] - (w * x[i] + b)) * x[i]
        grad_b += (y[i] - (w * x[i] + b))

    return (grad_w / 4 * m) , (grad_b / 4 * m)

def gda(x, y, m, learning_rate, iterations):

    w = 0
    b = 0

    for i in range(iterations):
        c = cost(x, y, w, b, m)
        print('Iteration', i, c)
        grad_w, grad_b = gradient(x, y, w, b, m)
        w_new = w - (learning_rate * grad_w)
        b_new = b - (learning_rate * grad_b)
        w = w_new
        b = b_new
        print('new parameters', w, b)
    return w, b

if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv('data.csv')
    x = df['x'].values.tolist()
    y = df['y'].values.tolist()
    m = len(x)
    learning_rate = 0.0000000001
    iterations = 100
    print(x, y)
    print(gda(x, y, m, learning_rate, iterations))