the algorithm is to left shift 1 time and or to the next value
​
1. take num val to head.val
2. while head.next
3. num = num << 1 | head.next.val
4. head = head.next
5. return num