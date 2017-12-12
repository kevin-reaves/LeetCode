#!/usr/bin/python

"""
Given an array of integers, every element appears three times except for one,
which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):

        ans = set(nums)
        ans = (sum(ans) * 3) - sum(nums)
        ans = ans/2

        return int(ans)

solution = Solution()

nums = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10]
print(solution.singleNumber(nums))