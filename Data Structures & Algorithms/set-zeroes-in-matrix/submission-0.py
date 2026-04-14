class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == 0:
                    matrix[m][0] = 0
                    matrix[0][n] = 0

        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][0] == 0 or matrix[0][n] == 0:
                    matrix[m][n] = 0
                    
        
        