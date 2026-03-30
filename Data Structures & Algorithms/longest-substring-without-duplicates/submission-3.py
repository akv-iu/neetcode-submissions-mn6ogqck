class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        op = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in op:
                op.remove(s[l])
                l +=1
            
            op.add(s[r])
            res = max(res, r-l+1)
        
        return(res)

            

        