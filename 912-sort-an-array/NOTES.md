priority queue
1. push value to heap
2. then pop element one by one and append to a list
​
recursion
1. base condition
1. if len(li) == 0 return
2. Hypothesis
2. take the last value in temp variable
3. pop the list
3. Induction
3. call the recusive function with small input
4. call insert function for sorting the list with temp value insertSort(li, temp)
​
insert function recursion
1. base condition
1. if the len(li) == 0 or temp >= n[-1]:
2. then append the temp value to the list
​
2. Hypothesis
2. take the last value into tmp variable
3. pop the list
3. Induction
3. call the insert array recursively with list and temp variable
4. finally append the last value to the list