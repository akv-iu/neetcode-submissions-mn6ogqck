class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        valid = set()

        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in valid:
                while s[r] in valid:
                    valid.remove(s[l])
                    l +=1

            valid.add(s[r]) 
            res = max(res,len(valid))

        return res

            

        