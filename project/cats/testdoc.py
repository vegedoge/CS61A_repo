from utils import lower, split, remove_punctuation, lines_from_file
from cats import game, game_string, time_per_word, all_words, all_times, word_at, time 

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

###################################
# problem  05
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


###############################
# problem 06 

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

# big_limit = 10
# shifty_shifts("awe", "awesome", big_limit) 



####################################
# problem 09

def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    players = len(times_per_player)
    words_num = len(words)
    times = [[0 for _ in range(words_num)] for _ in range(players)]
    for i in range(players):
        for j in range(words_num):
            times[i][j] = times_per_player[i][j + 1] - times_per_player[i][j]
    return game(words, times)
        
    # END PROBLEM 9
    
p = [[1, 4, 6, 7], [0, 4, 6, 9]]
words = ['This', 'is', 'fun']
game = time_per_word(p, words)