class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash = {i:[] for i in range(numCourses)}
        visit = set()
        for i,j in (prerequisites):
            hash[i].append(j)
            

        def dfs(i):
            if hash[i] == []:
                return True
            if i in visit:
                return False
            visit.add(i)
            for j in hash[i]:
                if not dfs(j):
                    return False
            # hash[i] = []
            # visit.remove(i)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

            
             
        