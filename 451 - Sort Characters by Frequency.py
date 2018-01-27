"""
Given a string, sort it in decreasing order based on the frequency of
characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""


from collections import Counter

class Solution:
    def frequencySort(self, s):
        if not s:
            return ""
        s = s.strip().lower()
        countLetters = Counter(s)
        sortLetters = countLetters.most_common()

        printLetters = ""
        for i in sortLetters:
            #("e", 12)
            printLetters += i[0] * i[1]
        return printLetters

s = "This is a very long string that contains several characters. I might " \
    "even make it a multi line string to make it even longer"

solution = Solution()
print(solution.frequencySort(s))