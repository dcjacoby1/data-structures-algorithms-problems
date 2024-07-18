# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


def groupAnagrams(strs):
        word_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in word_dict:
                word_dict[sorted_word].append(word)
            else:
                word_dict[sorted_word] = [word]
        anagram_array = [word for word in word_dict.values()]
        return anagram_array
        

#time complexity:
#sorting each wordO(mlogm)
#join is O(m)
#Dictionary Lookup is O(1)
#combined is (mlogm + m + 1)
# list comprehension is O(n)
#together is O(n*(mlogm + m + 1)) = O(n*mlogm)
#multiplied bc for each word, we do all the operations

#space complexity
#each word used in the dictionary key m 
# each value of the dictionary (lists) is n
#so its n * m