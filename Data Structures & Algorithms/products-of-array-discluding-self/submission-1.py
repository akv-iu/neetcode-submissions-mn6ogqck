class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = [1] * n
        count = 1
        for i in range(len(nums)):
            
            if i == 0:
                print(i)
                prefix[i] *= count
                
            else:
                count *= nums[i-1]
                prefix[i] *= count

        print(prefix)
        count = 1
        for i in range(len(nums)-1,-1,-1):
            
            if i == len(nums) - 1:
                suffix[i] *= count
                print(suffix)
            else:
                count *= nums[i+1]
                suffix[i] *= count
                print(suffix)
        print(suffix)
        
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        
        return res
        

        