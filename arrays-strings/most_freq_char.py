# Write a function, most_frequent_char, that takes a non-empty string and returns its most frequent character. If there is a tie, return the one that appears first.

def most_frequent_chars(s):
    lookup = {}

    for char in s:
        if char not in lookup:
            lookup[char] = 0
        lookup[char] += 1
    
    most_frequent = None 

    for char in s:
        # if most_frequent is None, set it to the current character as the initial value
        # OR if the current character's count is greater than the count of the current most_frequent character
        if most_frequent is None or lookup[char] > lookup[most_frequent]:
            most_frequent = char
    return most_frequent


    

print(most_frequent_chars("potato"))