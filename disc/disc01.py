from doctest import testmod
# 1.1
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return temp < 60 or raining


from math import sqrt
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    x = 2
    while x <= sqrt(n):
        if n % x != 0:
            x = x + 1
        else:
            return False
    return True

def f(x):
    # me = 1
    # def g(y):
    #     return me
    # me = 2
    # print(g(7))
    return x + y 
y = 1
z = f(2)
print(z)
# testmod()
# test = is_prime(29)
# print(test)
show = (lambda: 3)()
print(show)

