class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = set()

        res = 0
        l = 0
        valid = set()
        for i in range(len(s)):
            if s[i] in valid:
                res = max(res,len(valid))
                valid = set()
            
            valid.add(s[i])
        
        return res
