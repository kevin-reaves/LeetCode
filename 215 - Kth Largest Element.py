"""
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

from random import shuffle

class Solution(object):
    def findKthLargest(self, nums, k):
        return sorted(nums)[-k]

solution = Solution()

nums = list(range(1,100))
shuffle(nums)
print(solution.findKthLargest(nums, 6))
