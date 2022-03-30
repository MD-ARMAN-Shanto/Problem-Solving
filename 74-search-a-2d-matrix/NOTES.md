loop thru the matrix for initial length
1. take two pointer for binary search
2. while l < h:
3. find the mid
4. if matrix[i][mid]==target return True
5. elif number > target then make r = mid
6. else l = mid + 1
7. return False if not find number in matrix