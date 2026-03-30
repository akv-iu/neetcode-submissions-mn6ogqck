from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = defaultdict()
        for i in nums:
            if i in x.keys():
                return True
            else:
                x[i] = i
        return False        
                
        
         