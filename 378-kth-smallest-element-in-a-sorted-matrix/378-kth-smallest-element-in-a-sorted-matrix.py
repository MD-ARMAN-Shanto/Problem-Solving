class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        matrix[:]=sorted(list(itertools.chain(*matrix)))
        
        return matrix[k-1]
        
        
        