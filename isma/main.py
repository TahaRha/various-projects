import random
import statistics

list =[]

for i in range(200):
    list.append(random.random())

print(statistics.variance(list))

def avg(list):
    s = 0
    for num in list:
        s += num

    return s/len(list)

print(avg(list))


def calculate_variance(k):

    sum = 0
    for num in list:
        sum += (num - avg(list))**k

    return sum

print(calculate_variance(2))





