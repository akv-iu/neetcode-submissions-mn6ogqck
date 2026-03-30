class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
       ROWS, COLS = len(heights), len(heights[0])
       pac, atl = set(), set()

       def dfs(row, col, visit, prevheight):
        if ((row,col) in visit or
        row < 0 or col < 0 or row == ROWS or col == COLS or
        heights[row][col] < prevheight):
            return
        visit.add((row,col))
        dfs(row + 1, col, visit, heights[row][col])
        dfs(row - 1, col, visit, heights[row][col])
        dfs(row, col + 1, visit, heights[row][col])
        dfs(row, col - 1, visit, heights[row][col])

       for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS-1, c, atl, heights[ROWS-1][c])
       
       for r in range(ROWS):
        dfs(r,0,pac,heights[r][0])
        dfs(r,COLS-1,atl,heights[r][COLS-1])
       
       res = []
       for r in range(ROWS):
        for c in range(COLS):
            if (r,c) in atl and (r,c) in pac:
                res.append([r,c])
        
       return res

 