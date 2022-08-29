using dfs(depth first search)
​
steps:
1. first check the row column == 1
2. if 1 then pass it to the dfs recursive call to check whether it's adjacent edges have already the value of 1
3. handle the boundary limit
4. if adjacent edges is one mark them to be visited
5. call recursive dfs to it's four coordinate edge
6. finally count the number of island after every dfs call
7. return the count number of island