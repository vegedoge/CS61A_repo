from case_trees import *
from doctest import testmod

# Problem 1.1
'''
Write a function that returns the height of a tree. Recall that the height of a tree
is the length of the longest path from the root to a leaf.
'''
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(5,[tree(2)]), tree(3,[tree(4, [tree(2, [tree(4), tree(6)])]), tree(7)])])
    >>> height(t)
    4
    """
    assert is_tree(t), "t is not a tree"
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(branch) for branch in branches(t)])   

# problem 1.2
"""
Write a function that takes in a tree and returns the maximum sum 
of the values along any path in the tree. Recall that a path is
from the tree's root to any leaf.
"""
def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    assert is_tree(t), "t is not a tree"
    if is_leaf(t):
        return label(t)
    else:
        return label(t) + max([max_path_sum(branch) for branch in branches(t)])


# Problem 1.3
'''
Tutorial: Write a function that takes in a tree and 
squares every value. It should return a new tree. 
You can assume that every item is a number.
'''
def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...                 [tree(2,
    ...                     [tree(3),
    ...                     tree(4)]),
    ...                 tree(5,
    ...                     [tree(6,
    ...                         [tree(7)]),
    ...                     tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
     4
      9
      16
     25
      36
       49
      64
    """
    # from top to bottom design    
    assert is_tree(t), "t is not a tree"
    if is_leaf(t):
        return tree(label(t) ** 2)
    else:
        squared_branches = [square_tree(branch) for branch in branches(t)]
        return tree(label(t) ** 2, squared_branches) 


# Problem 1.3
'''
Tutorial: Write a function that takes in a tree and a value x and returns 
a list containing the nodes along the path required to get from the root 
of the tree to a node containing x. If x is not present in the tree, return 
None. Assume that the entries of the tree are unique. For the following tree,
find path(t, 5) should return [2, 7, 6, 5]    
'''
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree) == x:
        return [label(tree)]
    for branch in branches(tree):
        path = find_path(branch, x)
        if path:
            return [label(tree)] + path

# problem 2.2
'''
Write a function that takes in a tree consisting of '0's and '1's t and 
a list of "binary numbers" nums and returns a new tree that contains only 
the numbers in nums that exist in t. If there are no numbers in nums that 
exist in t, return None.
Definition: Each binary number is represented as a string. A binary number 
n exists in t if there is some path from the root to leaf of t whose values 
are equal to n.
For example, if t is as follows:
tree('1', 
        [tree('0',
                [tree('0'), tree'1']),
        tree('1',
                [tree('0')])])
# path: 100, 101, 110                
Then prune binary(t, ['01', '110', '100']) should return the following tree.
tree('1', 
        [tree('0',
                [tree('0')]),
        tree('1',
                [tree('0')])])
'''
def prune_binary(t, nums):
    """
    Return pruned tree t that only contains binary numbers 
    existing in nums
    """
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [x[1:] for x in nums if x[0] == label(t)]
        new_branches = []
        for branch in branches(t):
            pruned_branch = prune_binary(branch, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
        return tree(label(t), new_branches)


testmod()