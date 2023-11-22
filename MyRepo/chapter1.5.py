# from doctest import testmod
# from doctest import run_docstring_examples

# def sum_naturals(n):
#     """Return the sum of n numbers
#     >>> sum_naturals(10)
#     55
#     >>> sum_naturals(100)
#     5050
#     """
#     total, k = 0, 1
#     while k <= n:
#         total, k = total + k, k + 1
#     return total

# testmod()
# run_docstring_examples(sum_naturals, globals(), True)
'''
positive = 28
k = 1
while positive:
    print("positive?")
    print(positive)
    positive -= 3
    k = k+1
'''
a = True and 1/0 and False
print(a)
