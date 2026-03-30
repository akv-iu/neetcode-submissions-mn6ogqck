class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums) - 1
        if n == 0:
            return nums[0]
        if n == 1:
            return max(nums[0],nums[1])
        dp = {0: nums[0], 1:max(nums[0],nums[1])}

        

        def dfs(n):
            if n in dp:
                return dp[n]
            else:
                dp[n] = max(nums[n]+dfs(n-2), dfs(n-1))
                return dp[n]
            
        
        return dfs(n)
