"""
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""


import re

class Solution(object):
    def findWords(self, words):
        topRow = set("qwertyuiop")
        midRow = set("asdfghjkl")
        botRow = set("zxcvbnm")
        answer = []

        # a & b returns values in both a and b
        """
            For Alaska:
            word comes out of set as alsk
            alsk & asdfghjkl = alsk
            Since word & row equals word, this one passes
        """

        for word in words:
            wordSet = set(word.lower())
            if wordSet & topRow == wordSet:
                answer.append(word)
            if wordSet & midRow == wordSet:
                answer.append(word)
            if wordSet & botRow == wordSet:
                answer.append(word)
        return answer


solution = Solution()
print(solution.findWords(["Hello", "Alaska", "Dad", "Peace"]))