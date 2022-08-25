class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        # Defining a dict
        d = collections.defaultdict(list)
        
        for i in range(len(groupSizes)):
            d[groupSizes[i]].append(i)
            
        res, j = [], 0
        
        for i, v in d.items():
            l =len(v)
            
            while  l > 0:
                a = v[j:i+j]
                res.append(a)
                j += i
                l -= i
            j = 0
                
        return res                
                