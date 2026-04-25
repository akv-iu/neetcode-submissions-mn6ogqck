class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hash = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            hash[i].append(j)
        
        visit = set()
        res = []
        def dfs(curr):
            if hash[curr] == []:
                print(curr)
                res.append(curr)
                print(res)
                return res
            if curr in visit:
                return 
            visit.add(curr)
            for i in hash[curr]:
                if not dfs(i): return 
            visit.remove(curr)
            hash[curr] = []
            res.append(curr)  
            return res
        
        for i in range(numCourses):
            if not dfs(i):return []
        
        return res

        