class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        bitString = bin(num)[2:]
        return len(bitString) - 1 + bitString.count('1')
        