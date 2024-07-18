# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def firstUniqChar(s):
        letter_dict = {}
        for letter in s:
            if letter in letter_dict:
                letter_dict[letter] = False
            else:
                letter_dict[letter] = True
        for i in range(len(s)):
            if letter_dict[s[i]] == True:
                return i
        return -1