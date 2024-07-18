# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

#loop through the array
#if the number is a zero -> move it to then end position
#cant just place it at the end bc it will mess with the loop
# must have some sort of counter that keeps track of zeroes

def move_zeroes(nums):
    counter = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            counter += 1
        else:
            nums[i - counter] = nums[i]
    for j in range(counter):
        nums[-1 * (j + 1)] = 0
    return nums

print(move_zeroes([0,1,0,3,12]))

