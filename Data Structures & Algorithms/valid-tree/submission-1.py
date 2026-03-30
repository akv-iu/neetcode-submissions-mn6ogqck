class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hash = {i:[] for i in range(n)}

        for i,j in edges:
            hash[i].append(j)
            hash[j].append(i)
        print(hash)
        visit = set()
        
        def dfs(curr,prev):
            if curr in visit:
                return False
            visit.add(curr)
            print(visit)

            for next in hash[curr]:
                if next == prev:
                    continue
                if not dfs(next,curr) : return False
            return True
        
        return dfs(0,-1) and n == len(visit)
        