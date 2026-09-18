class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ash = {i:[] for i in range(numCourses)}

        for i,j in prerequisites:
            ash[i].append(j)
        
        valid = set()
        def dfs(i):
            if ash[i] == []:
                return []
            valid.add(i)
            for next in range(len(ash[i])):
                number = ash[i][next]
                if number in valid:
                    return -1
                    if number == []:
                        return []
                ans = dfs(number)
                if ans == []:
                    ash[i][next] = []
                if ans == -1:
                    return -1
            valid.remove(i)

            return 0
        
        for i in range(numCourses):
            if dfs(i) == -1:
                return False
        
        return True


        

        