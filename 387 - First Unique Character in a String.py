"""
Given a string, find the first non-repeating character in it and return its
index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

class Solution(object):
    def firstUniqChar(self, s):
        # can use s.replace to ignore spaces. I think counting them makes sense
        #s = s.replace(" ", "")
        # for letter in s:
        #     if s.count(letter) == 1:
        #         return s.index(letter)
        # else:
        #     return -1

        # My original solution was too slow. Iterating over letters
        # is better since it can happen in constant time
        letters = "abcdefghijklmnopqrstuvwxyz"
        index = [s.index(let) for let in letters if s.count(let) == 1]
        return min(index) if len(index) > 0 else -1

solution = Solution()
print(solution.firstUniqChar("leetcode"))