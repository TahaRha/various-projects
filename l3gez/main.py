from math import *

def find_generators_order(n):

    orders = dict()
    for i in range(n):
        orders[str(i)] = int(n/gcd(i, n))

    return orders

print(find_generators_order(20))
