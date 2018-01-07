"""
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to
ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.


"""

import string

class Solution(object):
    def isPalindrome(self, s):
        #I'd never used translators and wanted to try them out
        #s = ''.join(letter for letter in s if letter not in string.punctuation)
        #s = s.replace(" ", "")
        #s = s.lower()

        s = "".join([str.lower() for str in s if str.isalnum()])
        return s == s[::-1]


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("T@@@A###C$$$O%%%C%^^^A!@#$T!!!"))
print(solution.isPalindrome(""))
print(solution.isPalindrome("12345"))