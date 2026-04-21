class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row_l, col_l = len(grid), len(grid[0])
        visit = set()
        

        def bfs(row,col):
            q = deque()
            q.append([row,col])
            visit.add((row,col))
            
            
            while q:
                rows,cols = q.popleft()
                directions = [[1,0], [-1,0], [0,1],[0,-1]]
                for r,c in directions:
                    if (rows+r in range (row_l) and cols + c in range(col_l) 
                    and grid[rows+r][cols+c] == "1" and (rows+r,cols+c) not in visit):
                        visit.add((rows+r,cols+c))
                        q.append([rows+r,cols+c])
                        print(visit)
        count = 0
        for row in range(row_l):
            for col in range(col_l):
                if grid[row][col] == "1" and (row,col) not in visit:
                    bfs(row,col)
                    count += 1
                    print(count)
        
        return count




