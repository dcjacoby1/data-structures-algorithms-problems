def min_eq_sum(nums1, nums2):
    k_1 = 0
    k_2 = 0
    total_1 = 0
    total_2 = 0
    min_total = None
    for i in nums1:
        if i == 0:
            k_1 += 1
        else:
            total_1 += i
    for i in nums2:
        if i == 0:
            k_2 += 1
        else:
            total_2 += i
    if (total_2 - total_1) % (k_1 - k_2) != 0:
        return -1
    if (k_1 + total_1 > k_2 + total_2):
        min_total = k_1 + total_1
    else:
        min_total = k_2 + total_2
    return min_total        

nums1 = [2,0,2,0]
nums2 = [1,4]
print(min_eq_sum(nums1, nums2))