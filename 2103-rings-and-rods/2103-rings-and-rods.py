class Solution:
    def countPoints(self, rings: str) -> int:
        
        count = 0
        result = ['']*10
        
        for rod in range(1, len(rings), 2):
            result[int(rings[rod])] += rings[rod-1]
            
        for i in result:
            if 'R' in i and 'G' in i and 'B' in i:
                count +=1
                
        return count
            