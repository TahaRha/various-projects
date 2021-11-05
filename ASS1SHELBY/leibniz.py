# Name: Abderrahmane Chebli
# Student ID:260965432


# Write function below including a docstring

def compute_pi(n):
    """
    :param n: step
    :return: int

    >>> compute_pi(1))
    4.0
    >>> compute_pi(4)) == 2.8952380952380956
    True
    >>> compute_pi(100))
    3.1315929035585537
    """

    #setting the counting variable
    sum = 0

    #looping through the n and adding sequence term to sum
    for s in range(n):
        sum += ((-1)**s)/(2*s+1)

    #the sum is equal to pi/4, so we multiply it by 4
    pi = 4*sum

    return pi






# Test cases:
print(compute_pi(1))  # 4.0
print(compute_pi(4))  # 2.8952380952380956
print(compute_pi(100))  # 3.1315929035585537
