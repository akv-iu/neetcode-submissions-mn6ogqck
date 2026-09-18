class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = set()
        res = 0

        def dfs(node):
            visit.add(node)

            for nei in range(n):
                if nei not in visit and isConnected[node][nei] == 1:
                    dfs(nei)
            return
        for i in range(n):
            if i not in visit:
                dfs(i)
                res+= 1
        return res