class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        ans = right
        if len(piles) == h:
            return right
        while left < right:

            hours = 0
            mid = (left + right) // 2
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/mid)
            
            if hours > h:
                left = mid + 1
            elif hours <= h:
                right = mid - 1
                ans = min(ans,mid)

           
        return ans


        