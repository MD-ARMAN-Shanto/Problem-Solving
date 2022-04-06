class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        d = [0] * 300
        res = 0
        for i in range(len(arr)):
            res += d[target-arr[i]] if target-arr[i] >=0 else 0
            res %= (10**9+7)
            for j in range(i):
                d[arr[i] + arr[j]] += 1
        return res % (10**9+7)