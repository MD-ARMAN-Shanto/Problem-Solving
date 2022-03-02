class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # if len(digits)==0:
        #     # fail safe
        #     return digits
        # else:
        #     # increment the number to a single integer
        #     number = int(''.join([str(k) for k in digits]))+1
        #     # return back a list representation
        #     return [int(k) for k in str(number)]
        
        if len(digits) == 0:
            return digits
        
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                
        return [1]+digits
        
