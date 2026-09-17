class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax, cmin = 1,1
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                cmax, cmin = 1,1
                continue
            n = nums[i]
            num = cmax * n
            cmax = max(cmax * n, cmin * n, n)
            cmin = min(num, cmin * n, n)

            res = max(cmax,res)
        
        return res
            


        