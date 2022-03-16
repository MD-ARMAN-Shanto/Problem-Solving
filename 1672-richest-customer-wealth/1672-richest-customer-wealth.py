class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        # for i in range(len(accounts)):
        #     for j in accounts[0]:
        #         print(j)
        res = []
        
#         for i in range(len(accounts)):
#             total = [sum(accounts[i])]
#             res.append(total)
            
#         result = str(max(res))[1:-1]
#         return int(result)
            
    
        m_w = 0
        
        for i in range(len(accounts)):
            total = sum(i for i in accounts[i])
            
            if total > m_w:
                m_w = total
                
        return m_w
        