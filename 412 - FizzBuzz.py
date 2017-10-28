#!/usr/bin/python
"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output 'Fizz' instead of the number and
for the multiples of five output 'Buzz'. For numbers which are multiples of
both three and five output 'FizzBuzz'.
"""

class Solution:
    def fizzBuzz(self, n):
        for count in range(1, n+1):
            print(count)

solution = Solution()
print(solution.fizzBuzz(100))