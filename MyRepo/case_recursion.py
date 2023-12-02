# cascade
# reverse cascade

def reverse_cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        reverse_cascade(n // 10)
        print(n)
        
def inverse_cascade(n):
    
    def f_then_g(f, g, n):
        if n:
            f(n)
            g(n)
            
    grow = lambda n: f_then_g(grow, print, n // 10)    
    shrink = lambda n: f_then_g(print, shrink, n // 10)   
     
    grow(n)
    print(n)
    shrink(n)
    
    
# reverse_cascade(12345)
# inverse_cascade(12345)

# hanoi problem
def move(plate, start, end):
    print("move plate", plate, "from stick", start, "to stick", end)
    
def hanoi(n, start, end):
    if n == 1:
        move(n, start, end)
    else:
        spare = 6 - start - end
        hanoi(n-1, start, spare)
        move(n, start, end)
        hanoi(n-1, spare, end)
        
# hanoi(3, 1, 3)

# Counting Partitions problem
# break one positive integer into sums of a series of integers smaller 
# than one designated number in increasing order

def count_partition(n, m):
    '''default mode return all partitions
    >>> count_partition(2, 1)
    >>> 1
    >>> count_partition(3, 2)
    >>> 2
    '''
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        count = count_partition(n, m-1) + count_partition(n-m, m)
        return count 
        
# test = count_partition(6, 4)
# print(test)

# reverse a string
def reverse_str(in_string):
    if len(in_string) == 1:
        return in_string
    else:
        return reverse_str(in_string[1:]) + in_string[0]
    
test = reverse_str("my seu")
print(test)