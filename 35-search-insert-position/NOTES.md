take start = 0 and end = len(nums)-1
while start <= end:
find the mid
if mid == target return mid
elif target > mid:
start comes to mid+1
else end comes to mid-1 from the end
​
then just return the start