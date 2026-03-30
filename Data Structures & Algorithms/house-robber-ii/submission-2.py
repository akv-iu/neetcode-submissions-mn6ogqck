class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = nums[0:n-1]
        dp2 = nums[1:]
        if n == 1:    
            return nums[0]
        if n == 2:      
            return max(nums[0],nums[1])
        
        def helper(nums1):
            n = len(nums1)
            dp = [0] * (n) 
            if n == 1:    
                return nums1[0]
            if n == 2:      
                return max(nums1[0],nums1[1])
            dp[0] = nums1[0]
            dp[1] = max(nums1[0],nums1[1])
            for i in range(2,n):
                dp[i] = max(dp[i-1], nums1[i] + dp[i-2])
            print(dp)
            return dp[n-1]
        
        return max(helper(dp1),helper(dp2))

        