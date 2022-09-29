from math import sqrt


def sigma(*arg):
    while type(arg[0]) is tuple:
        arg = arg[0]
    ans = 0
    for i in range(len(arg)):
        ans += arg[i]
    return ans

def ave(*arg):
    while type(arg[0]) is tuple:
        arg = arg[0]
    return sigma(arg) / len(arg)

def squared_SEA(*arg):
    average = ave(arg)
    n = len(arg)
    RSS = 0
    for i in range(n):
        RSS += (arg[i] - average) ** 2
    return RSS / n * (n - 1)
