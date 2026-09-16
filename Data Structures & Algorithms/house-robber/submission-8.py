class Solution:
    def rob(self, nums: List[int]) -> int:
        curr = 0
        n = len(nums)
        nums.append(0)
        nums.append(0)
        
        for i in range(n-1,-1,-1):
            nums[i] = nums[i] + nums[i+2]
            nums[i] = max(curr,nums[i])
            curr = max(curr,nums[i])
        
        return nums[0]