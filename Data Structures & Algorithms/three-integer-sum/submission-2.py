class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        print(nums)
    

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            print(target)
            high = len(nums)-1
            left = i + 1
            while left<high:
                
                if nums[left] + nums[high] == target:
                    res.append([nums[i],nums[left],nums[high]])
                    left = left + 1
                    high = high - 1
                    while left < high and nums[left] == nums[left - 1]:
                        left += 1
                    while left < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif nums[left] + nums[high] > target:
                    high = high - 1
                else:
                    left = left + 1
        
        return res



        