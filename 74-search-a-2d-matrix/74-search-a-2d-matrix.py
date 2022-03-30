class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            l = 0
            h = len(matrix[i])

            while l < h:
                mid = (l+h)//2

                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    h = mid
                else:
                    l = mid+1
                        
        return False