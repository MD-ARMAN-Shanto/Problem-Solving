**Algorithm•nums1 is a subset of nums2 so all the values of nums1 are present in nums2
**1st step:**
take a stack and dict variable
loop thru nums 2
while stack has the value we compare the next element from the list with the last value of the stack if the value from the list is greater than the stack value
then we put the stack value as a key with the value from the list in out dictionary variable
**2nd step**
1. then pop the value from the stack like this we will iterate over the list•then our
2. dictionary hae the next greater element from nums2 list now we loop over the nums1 list
3. then we check our num is belong to the key of the dictionary
4. if it is then we append the value from the list of the key in our list
5. else we append -1
6. return the new list•