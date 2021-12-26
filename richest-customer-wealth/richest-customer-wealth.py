class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        # for i in range(len(accounts)):
        #     for j in accounts[0]:
        #         print(j)
        res = []
        
        for i in range(len(accounts)):
            total = [sum(accounts[i])]
            res.append(total)
            
        result = str(max(res))[1:-1]
        return int(result)
            
        