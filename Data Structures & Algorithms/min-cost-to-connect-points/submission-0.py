class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points) - 1
        visit = set()
        
        ans = 0

        def bfs(src,ans,edg,local_visit):
            if edg == n:
                
                return ans
            visit.add((src[0],src[1]))
            local_visit.append([src[0],src[1]])
            arr = []
            for j in range(len(local_visit)):
                for i in range(len(points)):
                    if tuple(points[i]) not in visit:
                        dist = abs(local_visit[j][0] - points[i][0]) + abs(local_visit[j][1] - points[i][1])
                        arr.append([dist,i])
            print(heapq.heapify(arr))
            dist, index = heapq.heappop(arr)
            ans += dist
            edg+= 1
            new_src = points.pop(index)
            print(ans,points,edg)
            return bfs(new_src,ans,edg,local_visit)
        src = points.pop(0)
        
        return bfs(src,0,0,[])


        