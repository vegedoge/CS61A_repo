from utils import lower, split, remove_punctuation, lines_from_file

def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    
    def pre_process(input):
        
        input = lower(input)
        input = remove_punctuation(input)  
        words = split(input)
        return words
    
    def select(input):
        words = pre_process(input)
        for keyword in topic:
            if any([keyword == x for x in words]):
                return True
        return False     
    
    return select
    # END PROBLEM 2
    
# dogs = about(['dogs', 'hounds'])
# dogs('A paragraph about cats.')
# dogs('A paragraph about dogs.') 


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    
    # created a list containing all gap scores
    if any([user_word == valid_word for valid_word in valid_words]):
        return user_word
    # created a list containing all gap scores
    gap = [diff_function(user_word, valid_word, limit)
           for valid_word in valid_words]
    address = -1
    # gap = reversed(gap)
    for index, score in enumerate(gap):
        if score < limit:
            limit = score
            # reversed index
            address = index
        elif score == limit and address == -1:
            address = index
    if address == -1:
        return user_word
    else:
        return valid_words[address] 
    
# first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
# autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    def shift_helper(start, goal, score):
        if score > limit:
            return score
        elif len(start) == 1:
            if start[0] != goal[0]:
                return score + 1
            else:
                return score
        else:
            if start[0] != goal[0]:
                return shift_helper(start[1:], goal[1:], score + 1)
            else:
                return shift_helper(start[1:], goal[1:], score)
                
    gap = len(start) - len(goal)
    if gap > 0:
        goal = goal + gap * ' '
    elif gap < 0:
        start = start + (-gap) * ' '
    
    return shift_helper(start, goal, 0)

big_limit = 10
shifty_shifts("awe", "awesome", big_limit) 