# problem 1.1
''' You want to go up a flight of stairs that has n steps. You can either take 1
or 2 steps each time. How many different ways can you go up this flight of
stairs? Write a function count_stair_ways that solves this problem. Assume
n is positive.
'''
def count_stair_ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)
    
'''
1.2 Tutorial: Consider a special version of the count_stairways problem,
where instead of taking 1 or 2 steps, we are able to take up to and including
k steps at a time.
Write a function count_k that figures out the number of paths for this scenario.
Assume n and k are positive.
'''
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif k == 0:
        return 0
    else:
        total = 0
        for i in range(1, k+1):
            total += count_k(n-i, k)
        return total
# test = count_k(10, 3)
# print(test)
'''
Tutorial: Write a function that takes a list s and returns a new list
that keeps only the even-indexed elements of s and multiplies them by their
corresponding index.
'''
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[x]*x for x in range(len(s)) if x % 2 == 0 ]

# s = [1,2,3,4,5,6]
# test = even_weighted(s)
# print(test)

'''
2.3 Write a function that takes in a list and returns the maximum product that
can be formed using nonconsecutive elements of the list. The input list will
contain only numbers greater than or equal to 1.
'''
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not s:
        return 1
    include = s[0]  # 包含当前元素时的最大乘积
    exclude = 1  # 不包含当前元素时的最大乘积
    for i in range(1, len(s)):
        # 当前的最大乘积，要么是包含上一个的最大乘积，
        # 要么是不包含上一个的最大乘积乘当前元素
        # 该步骤保证了相邻的不能同时选取
        new_include = max(include, exclude * s[i])
        # 不包含当前的最大乘积，选要么包含上一个，要么不包含上一个
        exclude = max(include, exclude)
        # 更新包含当前的最大乘积
        include = new_include
        
    return max(include, exclude)
test = max_product([5,10,5,10,5])
print(test)