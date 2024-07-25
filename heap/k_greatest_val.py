# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        #transforms list into a heap
        heapq.heapify(self.heap)
        #shortens the lest to length of k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        #adds the val and then removes smallest val to get to k values
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        #returns the lowest of the k values
        return self.heap[0]
    
#time complexity: O(LogK) for Add, O(N+Klogk) for Init
#space complexity: O(K) for both add and init

