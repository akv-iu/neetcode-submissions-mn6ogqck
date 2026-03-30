from _heapq import heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x,y in points:
            dis = (x**2) + (y**2)
            heapq.heappush(res, [-dis,x,y])
            if len(res)>k:
                heapq.heappop(res)
        ans = []
        for i,x,y in res:
            ans.append([x,y])
        
        return ans

