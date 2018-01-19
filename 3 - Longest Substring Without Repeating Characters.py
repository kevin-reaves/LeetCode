"""
Given a string, find the length of the longest substring without repeating
characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the
answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # My solution was close, I just needed to handle cases like pwwkew better
        # used = []
        # count = 0
        # countTemp = 0
        #
        # for letter in s:
        #     if letter not in used:
        #         countTemp += 1
        #         used.append(letter)
        #     else:
        #         if countTemp > count:
        #             count = countTemp
        #         countTemp = 1
        #         used = [letter]
        #
        #     if countTemp > count:
        #         count = countTemp
        #
        # return count

        result = 0
        temp = []

        for item in s:
            if item in temp:
                if len(temp) > result:
                    result = len(temp)
                temp = temp[temp.index(item)+1:]
                temp.append(item)
            else:
                temp.append(item)
        return max(len(temp), result)


solution = Solution()

longStr = "P3cUCMxQKWr2mTa60h2Zh9MYeOrdDghcU98yUqCwlrpsBhZ6wPW9GabcdefghijklmnopxxcgFyVOWzPCXKbdAS1dkpiOjY4MRL4OPa8csgApfWTrvfVMNWhXR3gNqqEtkvTJvMAxKM8vXNf7e4jQ7SJEvpuuZwEZTUFr7NvEOCLQ8CA202R9gm43jdLwg90k5ZD38udB5GUBKV6xN9c4WmgevC1jQg4oZNZ7Vytk0qv8V2UyieyWy21i4YlvaMRAGAQrVqfeFSJKCToUWq8Ali1Aak0PyUczrtnElfPpyCgC6PstFexHbqOUg8yerFW5CGb7z8X35lkFuJRYiKFbQADpyxqX7SXIQR65bBxWMJ6tOpMrs77qv82Cf07Y9BHNH0ZBPVDqvtjxg6l4xtfhIKjEXNDqdcLEc2edA8eaRcfHlUN2UKMf42lvgE3dw7zNmMptLM60eWH51enBdmufK0auZZIy2ty9G1QqyGVb51ZRlfLSboaWJkPY4QwpfjXg1Rt2wsTkMDrQ5Dzib7ecTiAlQtxgms9i5GnQBIEgxYGLZiyTwTPnds4cjovnl4GWRXI0jTji29Gs5xgsfH5wseVO52GOQSE5kgdxMd4BgcOB2JrIizUFqD20org8Cv98RKy4O2oicoThaaG9Juf0zU0CICQIbCJEsV2ISUYxSdv5NS40GX7YXkFrmPRcqMIO0p2ST2w4F8zjo88dV3V0CNb1cGXEZU7IWifJJiqAFGvePyTVv2YOtFnhxZEhqKmMvboFoOzugQaDeFul2OaKfhC8qiRLsSq3sVPzN2DQNpxnYINfUE9OG4OznmCul3QdRhpiHF2Rabfra69CoXaIFlsfhdNJYclzD7cpJXG55miV2FRvBksUJ4rWgqhXdtAYpE49NoqXwbmhPiMCNn5x1LLhKdzLsvfFHJTb2VfLZwWKLQjrvYZuCllpFV421deKqHWoWnuyHZwx4Pr1Dx8IyDwrVA9huL8x4raasePTew1y4T0WywVqLv5"
#longStr = "pwwkew"
print(solution.lengthOfLongestSubstring(longStr))