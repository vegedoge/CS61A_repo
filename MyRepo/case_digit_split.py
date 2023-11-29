def remove(n, digit):
    """Return all digits of non_negative N that are not DIGIT,
    for some non_negative digit less than 10.
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = 10 * kept if kept != 0 else 1 # kept=kept+last*10**digits
            digits = digits + kept * last # digits = digits + 1
    return digits                         # return kept

# a = remove(2518282, 2)
# print(a)

# implementation of recursion
def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return last + luhn_sum_doubled(all_but_last)
    
def luhn_sum_doubled(n):
    all_but_last, last = split(n)
    doubled = sum_digits(2 * last)
    if n < 10:
        return doubled
    else:    
        return luhn_sum(all_but_last) + doubled
        
test_number = 5105105105105100
sum = luhn_sum(test_number)
print(sum)
