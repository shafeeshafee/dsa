# Write a function, anagrams, that takes two strings and returns True if they are anagrams (contain the same characters in any order), otherwise False.

# restful fluster -> true
# cats tocs -> false

def anagrams(str1, str2):
    # in python, dict checks it checks if it has the same keys and values. It doesn't hold any inherent order
    char_count(str1) == char_count(str2)


# helper function
# returns a dict containing the count of each letter
def char_count(s):
    count = {}

    for char in s:
        if char not in count:
            # initialize it in dict
            count[char] = 0
        # add 1 occurence
        count[char] += 1

    return count

