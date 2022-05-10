class Solution:
    def bitwiseComplement(self, num: int) -> int:
        
        bin_number = list(bin(num)[2:])
        
        for i in range(len(bin_number)):
            if bin_number[i] == '1':
                bin_number[i] = '0'
            else:
                bin_number[i] = '1'
        
            
        number = ''.join(bin_number)
        
        return int(str(number), 2)