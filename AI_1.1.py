
def step():
    return 0.0001
def threshold():
    return 0.0000000001
def f_x(x1 = 0, x2 = 0):
    return 1.5 * x1 ** 2 + x2 ** 2 - 2 * x1 * x2 + 2 * x1 ** 3 + 0.5 * x1 ** 4
def d_dx1(x1, x2):
    return 3 * x1 - 2 * x2 + 6 * x1 ** 2 + 2 * x1 ** 3
def d_dx2(x1, x2):
    return 2 * (x2 - x1)
def gradient_descent(x1, x2):
    x1_new, x2_new = x1, x2
    while abs(d_dx1(x1, x2)) > threshold() and abs(d_dx2(x1, x2)) > threshold():
        print("%f\t%f\t%f\t%f\t%f" % (x1, x2, f_x(x1, x2), d_dx1(x1, x2), d_dx2(x1, x2)))
        x1 = x1 - step() * d_dx1(x1, x2)
        x2 = x2 - step() * d_dx2(x1, x2)
x1, x2 = 1, -3

gradient_descent(x1, x2)

