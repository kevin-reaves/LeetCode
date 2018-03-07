"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    def romanToInt(self, s):
        romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5,
                  'I': 1}
        prevValue = 0
        runningTotal = 0

        for i in range(len(s)-1, -1, -1):
            intVal = romans[s[i]]
            if intVal < prevValue:
                runningTotal -= intVal
            else:
                runningTotal += intVal
            prevValue = intVal
        return runningTotal

solution = Solution()
s = "XXXIV"
print(solution.romanToInt(s))