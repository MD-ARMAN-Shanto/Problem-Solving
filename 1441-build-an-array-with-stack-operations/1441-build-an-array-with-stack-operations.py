class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        res = []
        input = 1
        for i in target:
            while input < i :
                res.append('Push')
                res.append('Pop')
                input += 1
            res.append('Push')
            input += 1
                
        return res
        
        