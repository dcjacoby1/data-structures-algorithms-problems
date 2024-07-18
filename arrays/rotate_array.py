
#O(k*n)
def rotate(nums, k):
        #makes sure that the amount of movements doesn't exceed a full lab
        k %= len(nums)
        for _ in range(k):
            #takes the last element
            previous = nums[-1]
            #swaps it with the first element
            #does for for each element
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]



#O(n)
def rotate2(nums, k):
        n = len(nums)
        #creates new empty array, a
        a = [None] * n
        for i in range(n):
            #modulo of n to get placement and sets the value of a
            a[(i + k) % n] = nums[i]
        #makes nums equal to a
        nums[:] = a