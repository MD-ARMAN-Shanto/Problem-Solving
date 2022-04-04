class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        d = {}
        
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        res = list(d.values())
        
        rev_list = sorted(res, reverse=True)[:k]
        
        
        final_result = []

        for i in range(len(rev_list)):
            if rev_list[i] in d.values():
                position = list(d.values()).index(rev_list[i])
                f_n = list(d.keys())[position]           
                final_result.append(f_n)
                del d[list(d.keys())[position]]
    
        return final_result