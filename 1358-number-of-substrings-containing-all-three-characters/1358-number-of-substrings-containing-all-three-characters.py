class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        j, result, counter = 0, 0, collections.Counter()
        
        for i, c in enumerate(s):
            counter[c] += 1
            
            while len(counter) == 3:
                result += len(s) - i 
                counter[s[j]] -= 1
                
                if not counter[s[j]]:
                    del counter[s[j]]
                j += 1
                    
        return result
            
            