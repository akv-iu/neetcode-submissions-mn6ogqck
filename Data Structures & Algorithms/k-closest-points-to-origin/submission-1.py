from _heapq import heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            points[i].insert(0,-1 * (points[i][0]**2 +points[i][1]**2))
        print(points) 
        heapq.heapify(points)
        print(points) 
        i = len(points)
        while i > k:
            heapq.heappop(points)
            i -= 1
        for i in range(len(points)):
            points[i].pop(0)
        return points

