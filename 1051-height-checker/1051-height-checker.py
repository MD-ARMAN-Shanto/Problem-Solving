class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        duplicate = sorted(heights)
        count = 0
        
        for i, j in zip(heights, duplicate):
            
            if i != j:
                count += 1
                
        return count