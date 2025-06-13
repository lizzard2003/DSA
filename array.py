# Arrays in python are dynamic and they are next to each other
# In C++ we have to expand the array for insertion
# Arrays have indexes

from typing import List

# 26. Remove Duplicates from Sorted Array


def removeDuplicates(nums: List[int]) -> int:

    l = 1  # left starts at 1
    for r in range(
        1, len(nums)
    ):  # for r in range starting at 1 and going throughtout the length of nums
        if nums[r] != nums[r - 1]:  # if the right does not equal to r-1
            nums[l] = nums[r]  # then l and right are equal
            l += 1  # then increment the left pointer by 1
    return l  # return all the numbers that are left


nums = [1, 1, 2, 3, 5, 5]
lenght = removeDuplicates(nums)
print(nums[:lenght])
