class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        if not s or s[0] == '0':
            return 0

        dp[1] = 1
        dp[0] = 1

        for i in range(2,n+1):

            if int(s[i-1]) in range(1,10):
                dp[i] += dp[i-1]
            
            if int(s[i-2:i]) in range(10,27):
                dp[i] += dp[i-2]
        
        return dp[n]
        