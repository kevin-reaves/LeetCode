class Solution:
    def isPalindrome(self, x):
        return str(x)==str(x)[::-1]

solution = Solution()
x = 12345654321
print(solution.isPalindrome(x))
