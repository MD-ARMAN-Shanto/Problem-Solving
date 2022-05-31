class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        d = {}
        
        for n in nums:
            d[n] = d.get(n, 0) + 1 
            
        answer = []
        
        for i in range(len(nums)):
            if (nums[i]-1) not in d:
                if (nums[i]+1) not in d:
                    if d[nums[i]] == 1:
                        answer.append(nums[i])
                        
        return answer
                
                
                