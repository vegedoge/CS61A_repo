from doctest import testmod

# Problem 1.1
'''
Write a function that takes in a number n and returns a one-argument function.
The returned function takes in a function that is used to update n. It should return
the updated n.
'''
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f

# Problem 2.2
'''
Fill in the lines below so that the variables in the global frame are bound to the
values below. Note that the image does not contain a full environment diagram.
You may only use brackets, commas, colons, p , and q in your answer.
'''
def mystery(p, q):
    p[1].extend(q)
    q.append(p[1:])
    
    
p = [2, 3]
q = [4, [p]]
mystery(q, p)

#Problem 2.3
'''
Write a function that takes in a sequence s and a function fn and returns
a dictionary.
The values of the dictionary are lists of elements from s. Each element e in a list
should be constructed such that fn(e) is the same for all elements in that list. The
key for each value should be fn(e). For each element e in s, check the value that
calling fn(e) returns, and add e to the corresponding group.
'''
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for element in s:
        key = fn(element)
        if key in grouped:
            grouped[key].append(element)
        else:
            grouped[key] = [element]
    return grouped

# Problem 2.4
'''
 Write a function that takes in a value x, a value el, and a list s and
adds as many el's to the end of the list as there are x's. Make sure to modify
the original list using list mutation techniques.
'''
def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs
    in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    for i in s[:]:
        if i == x:
            s.append(el)

# Problem 4.1
'''
Implement a generator function called filter(iterable, fn) that only yields elements of iterable for which fn returns True.
'''
def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    iter_input = iter(iterable)
    for item in iter_input:
        if fn(item):
            yield item

# Problem 4.2
'''
Write a generator function merge that takes in two infinite generators a
and b that are in increasing order without duplicates and returns a generator that
has all the elements of both generators, in increasing order, without duplicates
'''
def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    next_a = next(a)
    next_b = next(b)
    while True:
        if next_a < next_b:
            yield next_a
            next_a = next(a)
        elif next_a > next_b:
            yield next_b
            next_b = next(b) 
        else:
            yield next_a
            next_a = next(a)
            next_b = next(b)
    


testmod()