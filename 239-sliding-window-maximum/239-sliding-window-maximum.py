class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        i, j = 0, 0
        q, res = [], []
        N = len(nums)
        
        while j < N:
            while len(q) > 0 and q[-1] < nums[j]:
                q.pop()
            q.append(nums[j])
            
            if j - i + 1 < k:
                j += 1
            else:
                res.append(q[0])
                if q[0] == nums[i]:
                    q.pop(0)
                i += 1
                j += 1
        return res
            
            
        