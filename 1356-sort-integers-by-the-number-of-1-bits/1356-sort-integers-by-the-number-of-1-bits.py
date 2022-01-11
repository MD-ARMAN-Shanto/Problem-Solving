class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        arr.sort()
        d = {}
        
        for i in arr:
            count = bin(i).count('1')
            
            if count not in d:
                d[count] = [i]
            else:
                d[count].append(i)
        
        res = []
        
        for j in sorted(d.keys()):
            res.extend(d[j])
            
        return res
            
        