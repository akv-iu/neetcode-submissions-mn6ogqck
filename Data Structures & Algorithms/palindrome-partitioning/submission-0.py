class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        palin = []

        def dfs(i):
            if i >= len(s):
                res.append(palin.copy())
                return
            
            for j in range(i,len(s)):
                if self.palindrome(s,i,j):
                    palin.append(s[i:j+1])
                    dfs(j+1)
                    palin.pop()
        
        dfs(0)
        return res

    def palindrome(self,s,i,j):

        while i<j:
            if s[i] != s[j]:
                return False
            else:
                i +=1
                j -= 1
        
        return True

        