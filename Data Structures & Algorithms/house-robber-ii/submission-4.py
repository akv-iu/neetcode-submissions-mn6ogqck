class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if not nums:
            return

        def rob2(nums):
            n = len(nums)
            print(nums)
            curr = 0
            nums[1] = max(nums[0],nums[1])
            for i in range(2,n):
                nums[i] = max(curr,nums[i] + nums[i-2])
                curr = max(curr,nums[i])
            
            return nums[n-1]
        n = len(nums)
        first = rob2(nums[1:])
        second = rob2(nums[:n-1])

        return (max(first,second))
                



        