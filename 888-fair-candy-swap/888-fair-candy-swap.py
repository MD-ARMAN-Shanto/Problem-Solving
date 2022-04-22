class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        asum = sum(aliceSizes)
        bsum = sum(bobSizes)
        
        delta = (asum - bsum)//2
        
        ahash = set(aliceSizes)
        
        for number in bobSizes:
            if number + delta in ahash:
                return [number+delta, number]
        