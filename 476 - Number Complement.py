class Solution:
    def findComplement(self, num):
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num

solution = Solution()
num = 1000
print(solution.findComplement(num))
