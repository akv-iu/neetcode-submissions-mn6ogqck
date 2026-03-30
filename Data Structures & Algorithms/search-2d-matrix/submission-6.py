class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        top, bottom = 0, row - 1
        
        
        while top <= bottom:
            mid = (top + bottom) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                bottom = mid - 1
        
        if not (top <= bottom):
            return False
        top = 0
        bottom = len(matrix[mid]) -1 
        curr = mid 
        
        while top <= bottom:
            mid = (top + bottom) // 2
            if target == matrix[curr][mid]:
                return True
            elif target > matrix[curr][mid]:
                top = mid + 1
            else:
                bottom = mid - 1
        
        return False
        
        