class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        primary_diagonal = 0
        secondary_diagonal = 0
        
        n = len(mat)
        
        for index in range(n):
            primary_diagonal += mat[index][index]

            if index + index != n - 1:
                secondary_diagonal += mat[index][n - index - 1]

        return primary_diagonal + secondary_diagonal
        