class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit = set()
        rows_l , cols_l = len(grid), len(grid[0])
        q = deque()
        res = -1
        for r in range(rows_l):
            for c in range(cols_l):
                if grid[r][c] == 2:
                    q.append([r,c])

        while q:
            for i in range(len(q)):
                rs,cs = q.popleft()
                visit.add((rs,cs))
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    r = rs + dr
                    c = cs + dc

                    if (r in range(rows_l) and c in range(cols_l)
                        and (r,c) not in visit and grid[r][c] == 1):
                        visit.add((r,c))
                        q.append([r,c])
                        grid[r][c] = 2
            print(grid)
            res += 1
        
        for r in range(rows_l):
            for c in range(cols_l):
                if grid[r][c] == 1:
                    return -1
        return (res if res > 0 else -1)



        