class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        ans = [[0 for _ in range(n+1)] for _ in range(m+1)]
        ans[m-1][n-1] = 1
        print(ans)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                ans[i][j] = ans[i][j] + ans[i+1][j] + ans[i][j+1]
        print(ans)
        return ans[0][0]

        