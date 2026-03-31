class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = 0, 0
        res = 0
        l = 0
        r = len(height) - 1
        while l < r:
            lmax = max(height[l],lmax)
            rmax = max(height[r],rmax)

            if lmax < rmax:
                
                res += lmax - height[l]
                l += 1
            
            else:
                
                res += rmax - height[r]
                r -= 1
        
        return res


        