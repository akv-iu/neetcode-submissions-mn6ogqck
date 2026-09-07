class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = set()

        res = 0
        l = 0
        valid = set()
        for i in range(len(s)):
            while s[i] in valid:
                valid.remove(s[l])
                l += 1
            valid.add(s[i])
            res = max(res,len(valid))
        return res

