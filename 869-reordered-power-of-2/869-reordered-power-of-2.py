class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        counter_number = Counter(str(n))
            
        i = 1
        iteration = 0
        while iteration <= 30:
            iteration += 1
            tmp_i = str(i)
            counter_tmp = Counter(tmp_i)
            if counter_tmp == counter_number:
                return True
            i *= 2
        return False
                
        
                