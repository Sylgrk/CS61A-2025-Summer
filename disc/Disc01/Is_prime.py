import math
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    i = 2
    flag = 0
    while (i <= math.sqrt(n)):
        if (n % i == 0): flag = 1
        i += 1
    if (flag == 0 and n != 1): print('True')
    else: print('False')
    
x = int(input())
is_prime(x)