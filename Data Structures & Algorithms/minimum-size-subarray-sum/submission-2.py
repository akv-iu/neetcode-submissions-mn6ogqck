class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        r = 0
        ans = n + 10
        curr = 0

        while r < n:
            curr = curr + nums[r]
            while curr >= target:
                ans = min(ans,r-l+1)
                curr = curr - nums[l]
                l += 1
                print(l,r,ans)
            r += 1
            
        return ans if ans != n+10 else 0

        