class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_idx, curr_subsets):
            self.res.append(curr_subsets.copy())
            for next_idx in range(curr_idx + 1, len(nums)):
                if next_idx > 0 and nums[next_idx] == nums[next_idx - 1] and curr_idx != next_idx - 1:
                    continue
                curr_subsets.append(nums[next_idx])
                backtrack(next_idx, curr_subsets)
                curr_subsets.pop()
                
        nums.sort()
        self.res = []
        backtrack(-1, [])
        return self.res