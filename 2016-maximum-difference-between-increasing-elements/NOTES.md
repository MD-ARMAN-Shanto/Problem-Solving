Algorithm
1. first take the initial value from the numbers[0]
2. take max_val = 0
3. loop thru the list from 1 to length-1
4. find the difference from cur_val - initial value
5. and then find the min_val between initial and current_num
6. then if curren_diff > max_val change max_val= curr_diff
7. return if max_val >0 return max_val else -1