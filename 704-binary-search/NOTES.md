taking left and right two variables as 0 and len(nums)
​
loop upto left is less than or equal to right
1. find the mid of the list using left + right // 2
2. then check the mid == target value if it is return mid
3. else if mid > target then increase the left by left = mid + 1
4. else mid is less then target then make right to right = mid -1
5. if the target not find in the list then return -1