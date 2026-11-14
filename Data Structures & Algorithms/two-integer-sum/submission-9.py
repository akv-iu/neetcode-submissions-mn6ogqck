class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            req = target - nums[i]

            if req in hash:
                return([hash[req],i])
            
            hash[nums[i]] = i
        
        return []
        
        