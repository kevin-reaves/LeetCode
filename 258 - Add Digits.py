"""
Given a non-negative integer num, repeatedly add all its digits until the
result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only
one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

The hint given for this pointed to
https://en.wikipedia.org/wiki/Digital_root

Basically, any multi digit number % 9 returns its digital root
We just have to account for 0 and numbers less than 9
"""

class Solution:
    def addDigits(self, num):
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

solution = Solution()
num = 8675309
print(solution.addDigits(num))