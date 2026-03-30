class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for i,n in enumerate(nums):
            num[n] = i
        for i in range(len(nums)):
            out = nums[i]
            expect = target - out
            if expect in num:
                if i == num[expect]:
                    continue
                else:
                    return([i,num[expect]])
            else:
                print(False)

