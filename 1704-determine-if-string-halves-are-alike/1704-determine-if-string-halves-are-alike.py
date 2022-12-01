class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        v_d = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        first_half = s[:len(s)//2]
        second_half = s[len(s)//2:]
        
        count = 0
        for i in first_half:
            if i in v_d:
                count += 1
        
        total = 0
        for j in second_half:
            if j in v_d:
                total += 1
        
        return count==total