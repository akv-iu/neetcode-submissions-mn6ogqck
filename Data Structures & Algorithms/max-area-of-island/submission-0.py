class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows_l , cols_l = len(grid), len(grid[0])
        area = 0
        visit = set()
        q = deque()

        def bfs(row,col,count):
            q.append([row,col])
            visit.add((row,col))
            while q:
                q_row, q_col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for ro,co in directions:
                    r = q_row + ro
                    c = q_col + co

                    if (r in range(rows_l) and c in range(cols_l)
                        and grid[r][c] == 1 and (r,c) not in visit):
                        visit.add((r,c))
                        q.append([r,c])
                        print(q)
                        count+=1
            
            return count

        for r in range(rows_l):
            for c in range(cols_l):
                if grid[r][c] == 1 and (r,c) not in visit:
                    
                    area = max(area,bfs(r,c,1))

        return area
            

        