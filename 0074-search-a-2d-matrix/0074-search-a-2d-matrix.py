class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            for j in matrix[i]:
                if j == target:
                    return True
                
        return False
        