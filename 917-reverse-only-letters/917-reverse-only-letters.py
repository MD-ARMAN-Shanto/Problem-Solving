class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        l = list(s)
        i, j = 0, len(l)-1
                
        while i < j:
            if l[i].isalpha() and l[j].isalpha():
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
                
            elif l[i].isalpha() and not l[j].isalpha():
                j -= 1
                
            elif not l[i].isalpha() and l[j].isalpha():
                i += 1
            else:
                i += 1
                j -= 1
            
        return ''.join(l)
            