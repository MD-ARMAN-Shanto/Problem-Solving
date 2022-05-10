class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        s_n, b_n = min(nums), max(nums)
        return math.gcd(s_n, b_n)