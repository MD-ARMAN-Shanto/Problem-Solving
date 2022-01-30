if len(nums)==1
return 0
​
1. find the max of higest val
2. find the index of highest val
3. pop the val from the list
4. find the 2nd highest val
5. return index if s_l * 2 <= f_l else -1
​
2nd algorithm:
1. find the max and it's index
2. then loop thru the list
3. if not max > 2*num and max != num then return -1
4. else return max index