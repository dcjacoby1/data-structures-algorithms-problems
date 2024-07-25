# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


#build a dict to count the 
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
            #returns k items, sorted by the values (key=), returns the keys (middle portion)
        return heapq.nlargest(k, freq_dict.keys(), key=freq_dict.get)
    


#time complexity: O(n) for for loop, O(klogn) for k most frequent
#total is O(n + klogn)

#space complexity: dictionary is O(n), heap uses O(k). overall O(n)