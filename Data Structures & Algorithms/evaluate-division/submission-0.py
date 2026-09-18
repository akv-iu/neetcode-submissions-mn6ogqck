from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        i = 0
        hash = defaultdict(list)
        for src, dest in equations:
            hash[src].append((dest, values[i]))       # Fixed: wrapped in tuple
            hash[dest].append((src, 1 / values[i]))   # Fixed: wrapped in tuple
            i += 1
        
        def bfs(src, dest):
            visit = set()                             # Fixed: moved inside so each query has fresh visit set
            q = deque()
            if src not in hash or dest not in hash:   # Fixed: check dest as well
                return -1.0
            visit.add(src)
            q.append([src, 1.0])
            while q:
                node, weight = q.popleft()

                if node == dest:
                    return weight                     # Fixed: typo 'wight' -> 'weight'
                for nex, w in hash[node]:
                    if nex not in visit:
                        visit.add(nex)                # Fixed: mark visited when queued
                        q.append([nex, w * weight]) 
            
            return -1.0

        ans = []
        for i in range(len(queries)):
            ans.append(bfs(queries[i][0], queries[i][1]))  # Fixed: removed inner []

        return ans