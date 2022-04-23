class Solution:
    def sortSentence(self, s: str) -> str:
        
        extract = s.split(" ")
        # number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = {}
        
        
        
        for val in extract:
            for i in range(len(val)):
                if val[i].isdigit():
                    s = val.split(val[i])
                    res[val[i]] = s[0]
        
        keys = sorted(res, key=lambda k: k) 
        
        f_res = []
        for val in keys:
            if val in res.keys():
                f_res.append(res[val])
                
        return " ".join(f_res)
                
                    
        
                    
                    
                    
        