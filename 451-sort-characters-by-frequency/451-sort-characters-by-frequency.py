class Solution:
    def frequencySort(self, s: str) -> str:
        
        d = {}
        
        for ch in list(s):
            d[ch] = d.get(ch, 0) + 1
            
        res = list(d.values())
        
        rev_list = sorted(res, reverse=True)
        
        final_result = []

        for i in range(len(rev_list)):
            if rev_list[i] in d.values():
                position = list(d.values()).index(rev_list[i])
                f_n =  rev_list[i] * list(d.keys())[position]           
                final_result.append(f_n)
                del d[list(d.keys())[position]]
    
        return ''.join(final_result)
        
        
        