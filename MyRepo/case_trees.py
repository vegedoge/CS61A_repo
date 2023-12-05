# tree data type
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

def count_leaves(t):
    '''count leaves of Tree T'''
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])
    
def leaves(tree):
    '''return all the labels for leaves in a list
    >>> leaves(fib_tree(5))
    [1,0,1,0,1,1,0,1]
    '''
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])
    
# creating trees
def increment_tree(t):
    '''return a tree like t but leaf labels incremented'''
    if is_leaf(t):
        return tree(label(t)+1)
    else:
        bs = [increment_tree(b) for b in branches(t)]
        return tree(label(t), bs)
    
def increment(t):
    '''return a tree like t but all labels incremented'''
    return tree(label(t)+1, [increment(b) for b in branches(t)])

def print_tree(t, indent=0):
    print(' '* indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)
        
def print_sums(t, so_far):
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far) 
    
# testing              
# t = fib_tree(5)
# print(t)
# t1 = increment_tree(t)
# print(t1)
# t2 = increment(t)
# print(t2)
# print_tree(t2)
t = fib_tree(3)
print_sums(t, 0)