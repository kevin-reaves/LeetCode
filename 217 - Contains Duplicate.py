"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.
"""


class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
solution = Solution()
print(solution.containsDuplicate(nums))