class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        tortoise = hare = nums[0]
        
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            
            if tortoise == hare:
                break
        
        # entrance of loop of the cycle
        tortoise = nums[0]
        
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
                
        return hare
    
        # 2nd approch using set
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)

        # 3rd approch using hashmap
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
            return num
    
            
                
