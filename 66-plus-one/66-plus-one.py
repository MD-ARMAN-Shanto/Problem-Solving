class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if len(digits) == 0:
            return digits
        
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                
        return [1]+digits
        