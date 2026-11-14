class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        find = set()
        for i in nums:
            if i in find:
                return True
            else:
                find.add(i)
        
        return False

        