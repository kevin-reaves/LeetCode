#!/usr/bin/python

"""
You are given a string representing an attendance record for a student.
The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than
one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his
attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""

import re

class Solution(object):

    def checkRecord(self, s):
        threeLate = "LLL"
        if re.search(threeLate, s):
            return False
        if len(re.findall("A", s)) > 1:
            return False
        else:
            return True

solution = Solution()


records = ["PPALLP", "PPALLL", "AAAAAA", "LLLLLL", "PPPPPP", "PLPLPL"]
for record in records:
   print(solution.checkRecord(record))