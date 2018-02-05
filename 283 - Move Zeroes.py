class Solution:
    def moveZeroes(self, nums):
        for x in range(0, len(nums)):
            if nums[x] == 0:
                nums.remove(nums[x])
                nums.append(0)
        return nums

solution = Solution()
nums = [1, 10, 100, 0, 2, 20, 200, 0, 0, 0, 3, 30, 300]
print(solution.moveZeroes(nums))
        
