class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ash = {i:[] for i in range(numCourses)}

        for i,j in prerequisites:
            ash[i].append(j)
        
        valid = set()
        def dfs(i):
            if ash[i] == []:
                return True
            if i in valid:
                return False
            valid.add(i)
            for nex in ash[i]:
                ans = dfs(nex)
                if not ans:
                    return False
            valid.remove(i)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True


        

        