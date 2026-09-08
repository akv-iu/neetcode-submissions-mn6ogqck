class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        has = {}
        for i in nums:
            has[i] = i
        
        res = 0
        

        for num in has:              
            if (num - 1) in has:
                continue
            else:
                k = 1
                leng = 1
                while (num + k) in has:
                    leng += 1
                    k += 1
                res = max(res, leng)
        
        return res
                


        