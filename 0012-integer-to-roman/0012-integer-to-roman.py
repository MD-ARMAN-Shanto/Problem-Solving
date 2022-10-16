class Solution:
    def intToRoman(self, num: int) -> str:
        
        num_rom_map = {
            
            1000  : "M",
            900   : "CM",
            500   : "D",
            400   : "CD",
            100   : "C",
            90    : "XC",
            50    : "L",
            40    : "XL",
            10    : "X",
            9     : "IX",
            5     : "V",
            4     : "IV",
            1     : "I"
        }
        
        ans = ''
        
        for x in num_rom_map:
            if x <= num:
                ans += (num//x) * num_rom_map[x]
                num %= x
                
        return ans
        
        
        