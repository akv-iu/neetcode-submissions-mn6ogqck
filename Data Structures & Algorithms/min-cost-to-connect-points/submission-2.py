class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visit = set()
        ans = 0
        adj = {i:[] for i in range(n)} #This holds starting node = dist,ending node
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j]) 
                adj[j].append([dist,i]) # The dist is same along both sides {0->1 = 1->0}
        print(adj)

        minh = [[0,0]] #This will be our starting point
        while len(visit) < n:
            dist, node = heapq.heappop(minh)
            if node in visit:
                continue
            visit.add(node)
            ans += dist
            print(node)

            for neicost, nxt in adj[node]:
                if nxt not in visit:
                    heapq.heappush(minh,[neicost,nxt])
            
        return ans





        