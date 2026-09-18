class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ash = {i:[] for i in range(numCourses)}

        for i,j in prerequisites:
            ash[i].append(j)
        
        valid = set()
        def dfs(i):
            if ash[i] == []:
                return True
            valid.add(i)
            for nex in ash[i]:
                if nex in valid:
                    return False
                ans = dfs(nex)
                if ans:
                    return True
                if not ans:
                    return False
            valid.remove(i)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True


        

        