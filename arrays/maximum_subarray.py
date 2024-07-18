#Given an integer array nums, find the subarray with the largest sum, and return its sum.
class Solution(object):
    def maxSubArray(self, nums):
        largest_number = None
        for i in range(len(nums)):
            largest_subarray = nums[i]
            current_subarray_total = nums[i]
            for j in range(i + 1, (len(nums) - 1)):
                current_subarray_total += nums[j]
                if current_subarray_total > largest_subarray:
                    largest_subarray = current_subarray_total
                else:
                    continue
            if largest_subarray > largest_number:
                largest_number = largest_subarray
            else:
                continue
        return largest_number


            
