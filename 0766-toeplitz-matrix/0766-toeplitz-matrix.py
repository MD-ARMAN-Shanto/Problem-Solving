class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        group = {}
        
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in group:
                    group[r-c] = val
                elif group[r-c] != val:
                    return False

        return True
                
        