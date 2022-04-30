#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        i = 0
        j = 0
        mx = 0
        s = 0
        
        while j < N:
            s += Arr[j]
            
            if j-i+1 < K:
                j += 1
            else:
                mx = max(mx, s)
                s -= Arr[i]
                i += 1
                j += 1
                
        return mx
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends