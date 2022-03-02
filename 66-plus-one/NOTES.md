Algorithm
1. if len(digits)==0
2. return digits
​
1. loop thru reversed index from the list
2. if digits[i] < 9
3. add 1 to the numbers
4. return the digits ex: [1, 0, 9] = [1,1,0]
5. else make the digit 0
​
finally return the list with [1] + digits
ex: [1] + [9,9,9] = [1,0,0,0]