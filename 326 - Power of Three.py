"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""

class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n/3

        if n == 1:
            return True
        else:
            return False

    def isPowerOfThreeCheat(self, n):
        #For the cheating version here, our huge number is 3^19
        #largest power of three that can be stored in signed 32 bit integer
        #if needed, we could pick another absurdly large number
        if n <= 0:
            return False
        return 1162261467 % 3 == 0

solution = Solution()
#3^10
n = 59049
print(solution.isPowerOfThree(n))
print(solution.isPowerOfThreeCheat(n))