class Solution:
    def capitalizeTitle(self, title: str) -> str:
    
        li = title.split(' ')
        res = []
        
        for word in li:
            if len(word) > 2:
                cap = word.title()   
                res.append(cap)
            else:
                res.append(word.lower())
                
        return ' '.join(res)
