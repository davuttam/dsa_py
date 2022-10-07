# Question 2
"""
Write a function that takes 2 strings and returns whether or not they are anagrams of each other.

A word is an anagram of another if:
One word can have the letters rearranged in order to create the other.
ie:
Both words are made up of the same letters and same number of each. 

Note: If the 2 words are the exact same word, they do count as anagrams of each other.

Use the examples below to test the correctness of your function.
"""

examples = [
  ["hello", "lelho",      True],
  ["rasp",  "spar",       True],
  ["hello", "leho",       False],
  ["hello", "hello",      True],
  ["hello", "diffi",      False],
  ["hello", "hellothere", False],
  ["hellothere", "hello", False],
  ["hello", "heloj",      False],
  ["hello", "hhelo",      False]
]

TOT_ALPHABETS_CHARS_LIMIT = 58

def anagram(word1, word2):
    len_word1, cap_a_ascii_val = len(word1), ord('A')

    if( len_word1 != len(word2)):
        return False

    char_count_arr = [0] * TOT_ALPHABETS_CHARS_LIMIT

    for ind in range(len_word1):
        char_count_arr[ord(word1[ind])-cap_a_ascii_val] += 1
        char_count_arr[ord(word2[ind])-cap_a_ascii_val] -= 1
    
    for val in char_count_arr:
        if val != 0:
            return False
    return True

for ex in examples:
    print(anagram(ex[0], ex[1]))