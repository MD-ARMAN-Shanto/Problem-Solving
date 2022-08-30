class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(mat[0])
    
        for i in range(n//2 + n%2):
            for j in range(n//2):
                tmp = mat[n-1-j][i] #7
                mat[n-1-j][i] = mat[n-1-i][n-j-1]
                mat[n-1-i][n-j-1] = mat[j][n-1-i]
                mat[j][n-1-i] = mat[i][j]
                mat[i][j] = tmp