def GCD(x, y):
    while x!= y:
        X, Y = max(x, y), min(x, y)
        X = X - Y
        x, y = max(X, Y), min(X, Y)
    return x
