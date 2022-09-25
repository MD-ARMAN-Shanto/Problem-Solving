class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        S = sum(x for x in nums if x % 2 == 0)
        ans = []

        for x, k in queries:
            if nums[k] % 2 == 0: 
                S -= nums[k]
            nums[k] += x
            if nums[k] % 2 == 0: 
                S += nums[k]
            ans.append(S)

        return ans