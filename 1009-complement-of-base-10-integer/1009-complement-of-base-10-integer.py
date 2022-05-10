class Solution:
    def bitwiseComplement(self, num: int) -> int:
        
        bin_number = bin(num)[2:]
        masking = int(math.pow(2, len(bin_number))) -1
        
        return num ^ masking