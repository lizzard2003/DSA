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


# 28. Find the Index of the First Occurrence in a String


def strStr(haystack: str, needle: str) -> int:

    for i in range(
        len(haystack) - len(needle) + 1
    ):  # for i in rangeof the lenght of the haystack minus the len of needle plus1
        if (
            haystack[i : i + len(needle)] == needle
        ):  # the string from haystack is the same as needle
            return i  # then return it here

    return -1  # if there is no comparison just return -1 , this is a test case


haystack = "Hero"
needle = "ro"
result = strStr(haystack, needle)
print(result)
