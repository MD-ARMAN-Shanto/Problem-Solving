class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        """ GCD Eucledian Algorithm
        
        general equation 
        step 1: bigest_number = smallest_number * nearer_times + remainder
        step 2: smallest_number = remainder * nearer_times + new_remainder
        step 3: remainder = new_remainder * nearer_times + n_new_remainder
        go until the last past will be zero then the previous number of the remainder would be the GCD of         the two number 
        
        
        GCD(10, 45)
        
        45 = 10 * 4 + 5 --> GCD
        10 = 5 * 2 + 0
        
        """
        
        small_val = min(nums)
        high_val = max(nums)
        
        while small_val <= high_val:
            remainder = high_val % small_val
            if  remainder == 0:
                return small_val
            
            high_val = small_val
            small_val = remainder
                
        return small_val
            
        