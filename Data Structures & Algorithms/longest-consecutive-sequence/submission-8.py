class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash = {}
        for i in nums:
            hash[i] = i
        long = 1
        for i in nums:
            if i-1 not in hash:
                length = 1
                while (i + length) in hash:
                
                    length += 1
                    long = max(long,length)
            
        
        return long
                

        