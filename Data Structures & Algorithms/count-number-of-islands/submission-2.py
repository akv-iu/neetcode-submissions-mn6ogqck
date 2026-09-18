class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        valid = set()

        def dfs(node,valid):
            i,j = node
            q = deque()
            q.append([i,j])

            while q:
                directions = [[0,1],[1,0],[-1,0],[0,-1]]

                for i in range(len(q)):
                    r,c = q.popleft()
                    valid.add((r,c))
                    for i,j in directions:
                        nr = r + i
                        nc = c + j

                        if nr in range(row) and nc in range(col) and (nr,nc) not in valid:
                            if grid[nr][nc] == '1':
                                q.append([nr,nc])
                                valid.add((nr,nc))
            return
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in valid:
                    dfs([i,j],valid)
                    count += 1
        
        return count