class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # count = 0
        numbers = []
        
        for i in range(n+1):
            numbers.append(bin(i)[2:].count('1'))
            
            
        return numbers