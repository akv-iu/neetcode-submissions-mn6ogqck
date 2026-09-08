class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        has_row = defaultdict(set)
        has_col = defaultdict(set)
        has_grid = defaultdict(set)


        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in has_row[row]:
                    return False
                if board[row][col] in has_col[col]:
                    return False
                if board[row][col] in has_grid[(row//3,col//3)]:
                    return False
                
                has_row[row].add(board[row][col])
                has_col[col].add(board[row][col])
                has_grid[(row//3 , col//3)].add(board[row][col])
        return True

