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
    
dogs = about(['dogs', 'hounds'])
dogs('A paragraph about cats.')
dogs('A paragraph about dogs.') 