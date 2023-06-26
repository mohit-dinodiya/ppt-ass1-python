def moveZeroes(nums):
    left = 0  

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[left] = nums[i]
            left += 1

    
    for i in range(left, len(nums)):
        nums[i] = 0

    return nums

nums1 = [0, 1, 0, 3, 12]
print(moveZeroes(nums1))  

nums2 = [0]
print(moveZeroes(nums2))  