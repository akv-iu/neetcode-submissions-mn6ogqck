class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visit = set()
        rows_l , cols_l = len(grid), len(grid[0])
        q = deque()

        for r in range(rows_l):
            for c in range(cols_l):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        dist = 0

        while q:
            for i in range(len(q)):    
                s_row, s_col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]

                for dr,dc in directions:
                    r = s_row + dr
                    c = s_col + dc

                    if (r in range(rows_l) and c in range(cols_l)
                        and grid[r][c] > 0):
                        if (r,c) not in visit:
                        #     grid[r][c] = min(grid[r][c], grid[s_row][s_col] + 1)
                        #     q.append([r,c])
                        # else:
                            grid[r][c] = min(grid[r][c], grid[s_row][s_col] + 1)
                            q.append([r,c])
                            visit.add((r,c))
            
        