import numpy as np

def gradient_descent(x, y):
    tzc = toc = 0
    counter = 15
    n = len(x)
    a = 0.0000003

    c_list = []
    for i in range(counter):
        y_pred = tzc + toc * x
        c = (1/(2 * n)) * sum([val**2 for val in y_pred - y])
        print('Cost', c)
        c_list.append(c)
        dtz = (1/n) * sum(y_pred - y)
        dto = (1/n) * sum(y_pred - y) * x

        tzc = tzc - a * dtz
        toc = toc - a * dto
        print('New parameters are:', tzc, toc)
    from matplotlib import pyplot as plt
    plt.plot([i for i in range(counter)], c_list)
    plt.show()

if __name__ == "__main__":
    import pandas as pd
    import numpy
    df = pd.read_csv('../ml/data.csv')
    x = np.array(df['x'].values.tolist())
    y = np.array(df['y'].values.tolist())
    gradient_descent(x, y)
