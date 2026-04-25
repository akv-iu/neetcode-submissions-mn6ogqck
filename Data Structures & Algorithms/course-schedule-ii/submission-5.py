class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hash = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            hash[i].append(j)
        
        visit = set() #This helps for DfS
        global_visit = set() #This holds all the visited numbers
        res = []
        def dfs(curr):
            if hash[curr] == []:
                res.append(curr)
                global_visit.add(curr)  
                return res

            if curr in visit:
                return 
            visit.add(curr)

            for i in hash[curr]:
                if i not in global_visit:
                    if not dfs(i): return 

            visit.remove(curr)
            hash[curr] = []
            res.append(curr)
            global_visit.add(curr)  
            return res
        
        for i in range(numCourses):
            if i not in global_visit:
                if not dfs(i):return []
        
        return list(res)

        