class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        

        helper = {}
        for index, row in enumerate(mat):
            helper[index] = 0
            for num in row:
                if num!=0: 
                    helper[index] += 1
        
        ans = sorted(helper, key = helper.get)
        return ans[:k]

        
                
            
            
            
                
        