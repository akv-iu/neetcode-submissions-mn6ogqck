class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows_l , cols_l = len(board), len(board[0])
        dire = [[1,0],[-1,0],[0,1],[0,-1]]

        def capture(ro,co):
            q = deque()
            q.append([ro,co])
            board[ro][co] = -1
            while q:
                row, col = q.popleft()
                for dr, dc in dire:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows_l) and c in range(cols_l)
                    and board[r][c] == "O"):
                        board[r][c] = -1
                        q.append([r,c])

        for r in range(rows_l):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][cols_l - 1] == "O":
                capture(r, cols_l - 1)

        for c in range(cols_l):
            if board[0][c] == "O":
                capture(0, c)
            if board[rows_l - 1][c] == "O":
                capture(rows_l - 1, c)
        

        for i in range(rows_l):
            for j in range(cols_l):
                if board[i][j] =='O':
                    board[i][j] = 'X'
                if board[i][j] == -1:
                    board[i][j] = 'O' 
        