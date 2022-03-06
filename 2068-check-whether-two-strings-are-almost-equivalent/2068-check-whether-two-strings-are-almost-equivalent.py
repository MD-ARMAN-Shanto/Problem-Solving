class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        
        for ch1 in word1:
            if ch1 not in d1:
                d1[ch1] = 1
            else:
                d1[ch1] += 1
                
        for ch2 in word2:
            if ch2 not in d2:
                d2[ch2] = 1
            else:
                d2[ch2] += 1
        
        for key in d1:
            if abs(d1[key] - d2[key]) > 3:
                return False
                    
        
        for key in d2:
            if abs(d1[key] - d2[key]) > 3:
                return False
                
        return True
