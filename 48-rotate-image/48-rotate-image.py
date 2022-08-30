class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # first tranpose the matrix
        l = len(mat[0])
        
        
        for i in range(len(mat)):
            for j in range(i, len(mat)):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
                
        # reverse the list with half of the length
        for r in range(len(mat)):
            for c in range(0, l//2):
                mat[r][c], mat[r][l-c-1] = mat[r][l-c-1], mat[r][c]
        
        
        return mat