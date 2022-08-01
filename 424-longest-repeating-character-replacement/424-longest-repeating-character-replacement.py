class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        res = 0
        l = 0
        
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            
            while (i-l+1) - max(count.values()) > k:
                
                count[s[l]] -= 1
                l += 1
            
            res = max(res, i - l + 1)
            
        return res