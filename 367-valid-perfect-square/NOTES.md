to find a perfect square using binary search the algorithm is
take left and right variable as l=1 and r=given_number
1. loop thru l<=r
2. find the mid
3. if mid * mid > num: reduce the r = mid -1
4. elif mid*mid < num: increase the l = mid+1
5. else it will be equal to number with mid square so return true
6. if no match found then break out from the loop and return False