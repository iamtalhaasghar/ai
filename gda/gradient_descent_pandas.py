import numpy


def gda(x, y):
    # h(x) = wx + b
    from matplotlib import pyplot as plt
    import random
    w = 0#random.random()
    b = 0#random.random()
    a = 0.0000003#random.random()
    print('Initial weight, biase and learning rate is:')
    print(w, b, a)
    w_list = []
    cost_list = []
    iterations = 10
    for i in range(iterations):
        loss = abs(y - (w * x + b))
        #print(loss)
        cost = sum(loss ** 2) / (2 * len(x))
        print('Cost is:', cost)

        w_new = w - a * (sum(loss * x) / (4 * len(x)))
        b_new = b - a * ( sum(loss) / (4 * len(x)) )

        w_list.append(w)
        cost_list.append(cost)

        w = w_new
        b = b_new

        print('New weight and bias', w, b)

    #plt.plot(w_list, cost_list)
    plt.plot([i for i in range(iterations)], cost_list)
    #plt.scatter(x, y)
    plt.show()

    return









if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv('../ml/data.csv')
    x = df['x']
    y = df['y']

    gda(x, y)