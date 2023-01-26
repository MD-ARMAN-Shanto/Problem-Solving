class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        d = {}
        
        for val, name in zip(heights, names):
            d[val] = name
            
        sorted_result = dict(reversed(sorted(d.items())))
        
        return list(sorted_result.values())
                
        