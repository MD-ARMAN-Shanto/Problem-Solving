#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    # code here
    
    i, j = 0, 0 
    stack, res = [], []
    
    while j < N:
        if A[j] < 0:
            stack.append(A[j])
        
        if j - i + 1 < K:
            j += 1
        
        elif j - i + 1 == K:
            # check the stack empty
            if len(stack) == 0:
                res.append(0)
            # stack not zero 
            else:
                res.append(stack[0])
                # again check for similar arr[i] value
                if A[i] == stack[0]:
                    stack.pop(0)
            i += 1
            j += 1
            
    return res
                
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends