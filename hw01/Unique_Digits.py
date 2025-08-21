def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    flag = 0
    while(n > 0):
        x = n % 10
        n = n // 10 
        if x == k:
            flag = 1
    if flag == 1: return True
    else: return False

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    i = 0
    cnt = 0
    while(i <= 9):
        if (has_digit(n, i)): cnt += 1
        i += 1
    print(cnt)     
