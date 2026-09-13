class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        ans = 1000000

        while l <= h:
            m = (l+h) // 2
            ans = min(ans,nums[m])
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m - 1
        
        return ans
        