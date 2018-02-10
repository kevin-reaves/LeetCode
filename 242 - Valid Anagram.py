"""
Given two strings s and t, write a function to determine if t is an
anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your
solution to such case?

"""


class Solution:
    def isAnagram(self, s, t):
        s = s.lower()
        s = s.replace(" ", "")

        t = t.lower()
        t = t.replace(" ", "")
        return sorted(s) == sorted(t)

solution = Solution()
s = "Tom Marvolo Riddle"
t = "I am Lord Voldemort"
print(solution.isAnagram(s,t))
