# initial variables of our regression line

def cost(x, y, w, b, m):
    total_loss = 0.0
    for i in range(m):
        tmp_x = x[i]
        tmp_y = y[i]
        total = (((w * tmp_x + b) - tmp_y) ** 2)
        total_loss += total
    return (total_loss) / (2 * m)

def gda(x, y):
    b_current = 0
    m_current = 0

    # amount to update our variables for our next step
    update_to_b = 0
    update_to_m = 0
    learning_rate = .0000001
    def error_at(x_point, y_point, b, m):
        return (m*x_point + b - y_point)

    n = len(x)
    for i in range(3):
        for i in range(0, len(x)):
            # update_to_b += -2*(error_at(x[i], y[i], b_current, m_current))
            # update_to_m += -2*(error_at(x[i], y[i], b_current, m_current)*x[i])
            update_to_b += (error_at(x[i], y[i], b_current, m_current))
            update_to_m += (error_at(x[i], y[i], b_current, m_current) * x[i])

        c = cost(x, y, m_current, b_current, n)
        print('Iteration', i, c)

        new_b = b_current - (learning_rate * update_to_b / n)
        new_m = m_current - (learning_rate * update_to_m / n)
        # new_b = b_current - update_to_b
        # new_m = m_current - update_to_m
        b_current = new_b
        m_current = new_m
        print(b_current, m_current)

    print((m_current * 1910 + b_current))
    print((m_current * 1950 + b_current))
    print((m_current * 1970 + b_current))
    print((m_current * 2010 + b_current))
    print((m_current * 2020 + b_current))
    print((m_current * 2025 + b_current))
if __name__ == "__main__":
    import pandas as pd

    df = pd.read_csv('../ml/data.csv')

    x = df['x'].values.tolist()
    y = df['y'].values.tolist()
    gda(x, y)