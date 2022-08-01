class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        
        count = {}
        res = 0
        
        l = maxf = 0
        
        
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            maxf = max(maxf, count[s[i]])
            
            while (i-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
                
            res = max(res, i-l+1)
        
        return res
                
        
        