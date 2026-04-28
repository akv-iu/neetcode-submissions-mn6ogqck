class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dict = {i:[] for i in range(1,n+1)}
        for u,v,w in times:
            dict[u].append([w,v])
        
        minheap = [[0,k]]
        t = 0
        visit = set()

        while minheap:
            nextdist, nextnode = heapq.heappop(minheap)
            if nextnode in visit:
                continue
            visit.add(nextnode)
            t = max(t,nextdist)
            print(t)
            for w,v in dict[nextnode]:
                if v not in visit:
                    heapq.heappush(minheap,[w+nextdist,v])
        
        return t if n==len(visit) else -1

        