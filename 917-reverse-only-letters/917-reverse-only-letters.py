class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        l = list(s)
        i, j = 0, len(l)-1
                
        while i < j:
            
            if not l[i].isalpha():
                i += 1
                continue
                
            if not l[j].isalpha():
                j -= 1
                continue
                
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
            
        return ''.join(l)
            