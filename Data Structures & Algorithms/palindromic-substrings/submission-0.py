class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = ""
        res = set()
        reslen = 0
        count = 0

        for i in range(len(s)):
            l, r = i, i
            

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > reslen:
                    
                    ans = s[l:r+1]
                    # if ans not in res:
                    # res.add(ans)
                    count += 1
                l -= 1
                r += 1

            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > reslen:
                    
                    ans = s[l:r+1]
                    # if ans not in res:
                    # res.add(ans)
                    count += 1
                l -= 1
                r += 1
        return count

        