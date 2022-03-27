class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n_l = set(nums)
        m_n = []

        for i in range(1, len(nums)+1):
            if i not in n_l:
                m_n.append(i)
            
        return m_n
                
            
            
            
                
                
        