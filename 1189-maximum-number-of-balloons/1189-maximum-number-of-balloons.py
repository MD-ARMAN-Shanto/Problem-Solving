class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        d = {'b': 0, 'a': 0, 'l':0, 'o':0, 'n': 0}
        d_d =['l', 'o']
        
        for ch in text:
            if ch in d:
                d[ch] = d.get(ch, 0) + 1
                
        for ch in d_d:
            d[ch] //= 2
        return min(d.values())
        
            
                
        
            
        