class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        if target == nums[low]:
            return(low)
        if target == nums[high]:
            return(high)
        while(low<=high):
            mid = (low+high)//2
            if target == nums[mid]:
                return(mid)

            if nums[mid]>=nums[low]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
                    print(high,low)
            
            else:
                if target <nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return(-1)

        