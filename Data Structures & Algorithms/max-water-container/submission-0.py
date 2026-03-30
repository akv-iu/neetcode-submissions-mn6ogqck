class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        print(end)
        ans = 0

        while start<end:
            width = end - start
            if heights[start]>heights[end]:
                height = heights[end]
                end -=1
                
            
            else:
                height = heights[start]
                start += 1
            
            print(width,height)
            curr_volume = height * width

            ans = max(ans,curr_volume)
        
        return(ans)

        