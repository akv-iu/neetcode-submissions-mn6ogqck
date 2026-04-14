class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = False
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if m==0 or n == 0 and matrix[m][n] == 0:
                    row = True

                if matrix[m][n] == 0 and m > 0 and n > 0:
                    matrix[m][0] = 0
                    matrix[0][n] = 0

        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][0] == 0 or matrix[0][n] == 0:
                    matrix[m][n] = 0
                    
        
        