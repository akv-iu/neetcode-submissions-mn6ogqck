class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            hash[i].append(j)
        
        visit = set()
        
        def dfs(cre):
            if hash[cre] == []:
                return True
            if cre in visit:
                return False
            
            visit.add(cre)
            for pre in hash[cre]:
                if not dfs(pre) : return False
            hash[cre] = []
            visit.remove(cre)
            return True

            
        
        for i in range(numCourses):
            if not dfs(i) : return False
        return True

