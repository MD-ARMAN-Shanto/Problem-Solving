class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        d = {}
        o = set(nums)
        s = set()
        res = []
        
        for ch in nums:
            d[ch] = d.get(ch, 0) + 1

        for i, v in d.items():
            if v < 2:
                s.add(i)

        for n in s:
            if n-1 in o or n+1 in o:
                continue
            res.append(n)
            
        return res
                
                
                