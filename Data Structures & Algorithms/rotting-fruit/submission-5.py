class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        valid = set()
        q = deque()
        row = len(grid)
        col = len(grid[0])
        

        def dfs(q,grid):
            count = 0
            while q:
                count += 1
                directions = [[0,1],[1,0],[-1,0],[0,-1]]

                for i in range(len(q)):
                    r,c = q.popleft()
                    
                    valid.add((r,c))
                    for i,j in directions:
                        nr = r + i
                        nc = c + j
                        if nr in range(row) and nc in range(col) and (nr,nc) not in valid:
                            if grid[nr][nc] == 1:
                                grid[nr][nc] = 2
                                q.append([nr,nc])


                
            return count
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append([i,j])
        ans = dfs(q,grid)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1

        return ans - 1
        

        