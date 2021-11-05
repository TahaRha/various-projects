import math

n = int(input("Enter n: "))

for c in range(2, n):
    for b in range(2, c):
        for a in range(2, b):
            if (math.gcd(a, b, c) == 1) and (1<a<b<c<n):
                if (a**2+b**2 == c**2):
                    print(a, b, c)






