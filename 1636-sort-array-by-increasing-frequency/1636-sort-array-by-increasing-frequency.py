class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        d = {}
        
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        return sorted(sorted(nums, reverse=True), key=lambda x: d[x])
            