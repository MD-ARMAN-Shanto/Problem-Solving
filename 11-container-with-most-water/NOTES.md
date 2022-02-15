1. take a max_area variable = 0
2. take two pointer as start = 0 and end = len(height)-1
​
while start < end:
3. find the area = width(end-start) * minimum value of two pointer (height[end], height[start])
4. find the max_area = max(area, max_area)
5.  move the pointer like if height[end] > height[start]
6. then move the pointer to right (start += 1)
7. else move the pointer to left (end -=1)