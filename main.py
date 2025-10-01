
"""Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number """

def increment_string(strng):
    if strng == "":
        return "1"
    
    #TODO implement here
    i =len(strng)-1
    while i >=0 and strng[i].isdigit():
        i-=1

    prefix=strng[:i+1]
    number=strng[i+1:]

    if number == "":
        return prefix + "1"
    
    new_number=str(int(number)+1).zfill(len(number))
    return prefix + new_number

"""
implement the function below to :
    return a diction with the count of each letter in the string
    example: "aba" -> {"a": 2, "b": 1}
"""
def count_letters(string):
    counts={}
    for char in string:
        counts[char]=counts.get(char, 0)+1
    return counts
    
"""implement the function below to :
    return a list of sums of each consecutive pair in the list
    example: [1, 2, 3] -> [3, 5]
    """
    
def sum_consecutives(s):
    if len(s)<2:
        return []
    return [s[i]+s[i+1]for i in range(len(s)-1)]
    
"""implement the function below to :
    return the number of unique words in a string
    and throw a value-exception if the input is not a string
    example: 'no example ;)'
    """
    
def count_unique(string):
       
    #TODO implement here
    return 0