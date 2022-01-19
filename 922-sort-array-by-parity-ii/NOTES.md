1. take 2 array 1 is even and another is odd
2. append the even and odd numbers from the nums array
3. then take a result list
4. loop thru the even array
5. append even and odd number to the res list
6. return the res list
---------
2nd approch:
1. take j =1
2. loop the nums value from (0, len(nums), 2)
3. if nums[i] % 2: (means if remaider is 1 insert into the if condition neither go to else:
4. loop thru all the A[j]%2 until length:
5. change the value nums[i]. numsj] = nums[j], nums[i]
6. return the nums
