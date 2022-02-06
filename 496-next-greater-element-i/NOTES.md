Algorithm
​
nums1 is a subset of nums2 so all the values of nums1 are present in nums2
1st step:
1. take a stack and dict variable
2. loop thru nums 2
3. while stack has the value we compare the next element from the list with the last value of the stack if the value from the list is greater than the stack value
4. then we put the stack value as a key with the value from the list in out dictionary variable
5. then pop the value from the stack like this we will iterate over the list
​
then our dictionary hae the next greater element from nums2 list
now we loop over the nums1 list
1. then we check our num is belong to the key of the dictionary
2. if it is then we append the value from the list of the key in our list
3. else we append -1
4. return the new list
​