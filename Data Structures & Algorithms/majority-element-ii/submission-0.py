class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        has = {}
        n = len(nums)

        for i in range(len(nums)):
            has[nums[i]] = 1 + has.get(nums[i],0)
        
        ans = []

        for key in has:
            if has[key] > n/3:
                ans.append(key)
        return ans



        