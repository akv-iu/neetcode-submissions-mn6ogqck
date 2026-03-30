class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        visit = set()
        rows_l, cols_l = len(grid), len(grid[0])
        

        def bfs(rows,cols):
            q = collections.deque()
            q.append((rows,cols))
            visit.add((rows,cols))

            while q:
                rows,cols = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r = rows + dr
                    c = cols + dc
                    if (r in range(rows_l) and
                        c in range(cols_l) and
                        grid[r][c] == "1" and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))

        for i in range(rows_l):
            for j in range(cols_l):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i,j)
                    
                    islands += 1
        return islands