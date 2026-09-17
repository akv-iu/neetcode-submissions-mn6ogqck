class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ash = defaultdict(set)
        for word in wordDict:
            length = len(word)
            ash[length].add(word)
        
        l,r = 0,0
        res = ''

        while r < len(s):
            if r-l+1 in ash:
                if s[l:r+1] in ash[r-l+1]:
                    res += s[l:r+1]
                    print(res)
                    l = r + 1
                    r = r + 1
                    
                
            r+=1
        
        return res == s
        


            