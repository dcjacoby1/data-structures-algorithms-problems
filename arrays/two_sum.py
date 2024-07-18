# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



nums = [2,7,11,15]
target = 9
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            elif nums[i] + nums[j] == target:
                return [i , j]
            
print(two_sum(nums, target))
            