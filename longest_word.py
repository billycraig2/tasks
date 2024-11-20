from functools import reduce

# TASK 2 - Find the largest word from the given input statement
# gets the longest word from a string
def longest_word(message):
    # joins letters that are spaces or alphabet to a string
    words = "".join(filter(lambda c : c.isspace() or c.isalpha(), message))
    split_words = words.split() # split by space into a list

    # loops through words and compares lengths
    longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, split_words)
    return longest_word
    
message = input('Input: ')

print(longest_word(message))
