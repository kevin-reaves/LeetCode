"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        # & returns values in both a and b.
        # using a and b here would return values in both
        return list(nums1 & nums2)

solution = Solution()
nums1 = [1, 1, 1, 1, 1 ,2,3,4,5,6,7,8,9,10]
nums2 = [1,1,1,6,5,11]
print(solution.intersection(nums1, nums2))
