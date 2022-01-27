Understanding:
Reverse sort the array of costs. Now the first two will be highest costs which can help us get the third one for free and so on.
​
Algorithm:
​
Reverse sort the array
Initialize index i at 0, resultant cost as 0 and N as length of array cost
Add the cost of 2 candies to result, i.e., the cost at index and the next one
Increment index by 3, continue this step and above one till index reaches length of array
Return the result
​