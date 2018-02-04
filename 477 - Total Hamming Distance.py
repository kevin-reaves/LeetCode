"""
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the
given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is
0010 (just showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) +
HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.
"""

class Solution:
    def totalHammingDistance(self, nums):
        #zip(*map('{:032b}'.format, nums))
        #zip returns a generator object of a certain index for each item
        #('0', '0', '1') would be the output at a given location

        #sum(b.count('0') * b.count('1') for b in zip...
        #('1', '1', '0')
        #b.count("0") = 1, b.count("1") = 2. 2 * 1 = 1
        #('0', '0', '0')
        #b.count("0") = 3, b.count("1") = 0. 3 * 0 = 0
        #Only rows where something is different will change the sum

        return sum(b.count('0') * b.count('1') for b in zip \
            (*map('{:032b}'.format, nums)))



solution = Solution()
nums = [4, 14, 2]
print(solution.totalHammingDistance(nums))