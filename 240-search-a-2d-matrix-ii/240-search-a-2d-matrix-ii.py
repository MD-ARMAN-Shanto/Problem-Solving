class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            l = 0
            r = len(matrix[i])

            while l < r:
                mid = (l+r)//2

                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    r = mid
                else:
                    l = mid+1
                        
        return False