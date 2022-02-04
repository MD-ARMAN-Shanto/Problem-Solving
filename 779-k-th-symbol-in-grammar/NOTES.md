​
**Algorithm for recursion process**
**base case**
1. given in the question if n==1 and k==1 return 0
​
**find the mid of row n so that we can define where the k belongs**
1. find the mid of using power function of 2 upto n-1
mid = math.pow(2, n-1)//2
2. using the mid we will compare with kth value
​
​
**if k is less then mid the we can define the previous row of n**
1. if k is less then the mid then our answer lies on (n-1)th row cause
len(n)//2 == len(n-1)
2. else return kthGrammar(n-1, k-mid) with compliment the return statement cause            nth second half is complimentary value of n-1 values, that's the reason
​
​