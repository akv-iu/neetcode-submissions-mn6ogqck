class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dict =  {i:[] for i in range(1,n+1)}
        for u,v,t in times:
            dict[u].append([t,v])
        print(dict)
        visit = set()

        def bfs(node,dist):
            visit.add(node)
            print(visit)
            if len(visit) == n:
                print(dist)
                return dist
            array = dict[node]
            heapq.heapify(array)
            print(array)
            if not array:
                return -1
            nextdist,nextnode = heapq.heappop(array)
            return bfs(nextnode,dist+nextdist)

        return bfs(k,0)



        