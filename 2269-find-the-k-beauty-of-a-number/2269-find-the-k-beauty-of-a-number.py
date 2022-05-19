class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        i = 0
        count = 0
        s = str(num)
        
        
        while (i+k) <= len(s):
            z = int(s[i:i+k])
            
            if z and not num%z:
                count += 1
            i += 1
            
        return count