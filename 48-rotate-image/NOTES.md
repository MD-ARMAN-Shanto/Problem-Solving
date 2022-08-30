rotate image
​
step1:
transpose the array list with i, j = j, i
​
then just reverse the list with the half of the length
for len(3)//2 = skip lenght 1 like 3-1 = 2
then just replace value like
mat[r][c], mat[r][length_of_row-c-1] = mat[r][length_of_row-c-1], mat[r][c]
​