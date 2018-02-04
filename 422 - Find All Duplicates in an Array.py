"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

used the below link for algorithm help
https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

This one took about 45 minutes to figure out even with looking at the answer.
The solution is interesting, the abs(x) isn't concerned with the
location of x's actual value

4 4 3 2 1
it's going to loop through and use the pigeonhold principle
to mark numbers we've seen as negative, and when we hit a
negative number that means we've seen it before

for the 4s here, 2 is going to be marked negative on the
first four and checked on the second four

nums(abs(4)) -> nums[3]. 4 may not be nums[3], but we're
using that location as a marker

The -1 deals with the n in 1≤a[i]≤n
"""

class Solution:
    def findDuplicates(self, nums):
        result = []
        for x in nums:
            if nums[abs(x) -1] < 0:
                result.append(abs(x))
            else:
                nums[abs(x) -1] *= -1
        
        return result

solution = Solution()
#nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2]
nums = [4,4,3,2,1,]
print(solution.findDuplicates(nums))
