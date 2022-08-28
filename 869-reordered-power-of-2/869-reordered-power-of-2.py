class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
#         l = list(str(n))
#         if l[0] == 0:
#             return False
        
#         d = {}
        
#         for ch in l:
#             d[ch] = d.get(ch, 0) + 1
        
#         rep = {}
#         for i in range(30):
#             p = 2 ** i
#             for ch in list(str(p)):
#                 rep[ch] = rep.get(ch, 0) + 1
#             if rep == d:
#                 return True
#             rep.clear()
            
#         return False

        counter_number = Counter(str(n))
            
        i = 1
        iteration = 0
        while iteration <= 30:
            iteration += 1
            counter_tmp = Counter(str(i))
            if counter_tmp == counter_number:
                return True
            i *= 2
        return False
                
        
                