# Arrays in python are dynamic and they are next to each other
# In C++ we have to expand the array for insertion
# Arrays have indexes

from typing import List

# 26. Remove Duplicates from Sorted Array


def removeDuplicates(nums: List[int]) -> int:

    l = 1  # left starts at 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    return l


nums = [1, 1, 2]
lenght = removeDuplicates(nums)
print(nums[:lenght])
