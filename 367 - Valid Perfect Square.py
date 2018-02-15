"""
Given a positive integer num, write a function which returns True
if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""

class Solution:
    def isPerfectSquare(self, num):
        return num**0.5 == int(num**0.5)

solution = Solution()
num = 17
print(solution.isPerfectSquare(num))