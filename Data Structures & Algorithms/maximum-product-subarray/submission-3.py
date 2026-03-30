class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmin, curmax = 1,1
        res = max(nums)

        for n in nums:
            if n == 0:
                curmin, curmax = 1,1
            
            temp = curmax
            curmax = max(n* curmax, n * curmin, n)
            curmin = min(n* temp, n * curmin, n)
            res = max(res,curmax)
        
        return res

        
        # dp = [0] * len(nums)
        # if len(nums) == 1:
        #     return nums[0]
        # dp[0] = nums[0]
        # for i in range(1,len(nums)):
        #     dp[i] = max(nums[i], nums[i] * dp[i-1])
        #     print(dp)
        
        # return max(dp)