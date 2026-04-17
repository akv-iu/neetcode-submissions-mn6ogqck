class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = ""
        res = set()
        count = 0

        for i in range(len(s)):
            l,r = i,i
            reslen = 0
            while l>=0 and r < len(s):
                if s[l] == s[r] and (r-l+1) > reslen:
                    # reslen = r - l + 1
                    res.add(s[l:r+1])
                    count += 1

                l -= 1
                r += 1

        for i in range(len(s)):
            l,r = i,i+1
            reslen = 0
            while l>=0 and r < len(s):
                if s[l] == s[r] and (r-l+1) > reslen:
                    # reslen = r - l + 1
                    res.add(s[l:r+1])
                    count += 1

                l -= 1
                r += 1
        
        return count