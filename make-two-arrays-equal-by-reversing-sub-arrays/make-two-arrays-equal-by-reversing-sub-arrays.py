class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        for i, j in zip(sorted(target), sorted(arr)):
            if i == j:
                continue
            else:
                return False
            
        return True