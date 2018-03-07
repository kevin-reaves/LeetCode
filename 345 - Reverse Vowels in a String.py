class Solution:
    def reverseVowels(self, s):
        s = list(s)
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        index = []
        word = []
        for i in range(len(s)):
            if s[i] in vowels:
                index.append(i)
                word.append(s[i])
        for i in index:
            s[i] = word.pop()
        return "".join(s)


solution = Solution()
s = "This is a long string with several vowels"
print(solution.reverseVowels(s))
