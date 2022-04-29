class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        # sort by value in descending order, keep track of original indices
        nums = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)
		# sort k large numbers by original indices (as it's supposed to be a sequence)
        snums = sorted(nums[:k])
		# get rid of the indices, and return only the numbers
        return [x[1] for x in snums]
                