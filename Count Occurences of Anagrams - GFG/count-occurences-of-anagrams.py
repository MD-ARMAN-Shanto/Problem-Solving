#User function Template for python3
class Solution:
	def search(self, pat, txt):
	    # code here
	    i, j = 0, 0
        d = {}
        
        for p in pat:
            d[p] = d.get(p, 0) + 1
            
        count = len(d)
        
        ans = 0
        
        while j < len(txt):
            
            if txt[j] in d:
                d[txt[j]] -= 1
                if d[txt[j]] == 0:
                    count -= 1
            
            if j - i + 1 < len(pat):
                j += 1
                
            elif j - i + 1 == len(pat):
                if count == 0:
                    ans += 1
                if txt[i] in d:
                    d[txt[i]] += 1
                    if d[txt[i]] == 1:
                        count += 1
                        
                i += 1
                j += 1
                    
        return ans
	    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends