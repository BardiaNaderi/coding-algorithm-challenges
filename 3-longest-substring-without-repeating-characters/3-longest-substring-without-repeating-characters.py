class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        length = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[length])
                length += 1
            charSet.add(s[r])
            res = max(res, r - length + 1)
        return res