# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

#loop through the array
#first instance of number, false
#second return false



def contains_duplicate(nums):
    num_dict = {}
    array_status = False
    for i in nums:
        if i in num_dict:
            array_status = True
            return array_status
        else:
            num_dict[i] = 0
    return array_status
print(contains_duplicate([1,2,3,1]))