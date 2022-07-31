class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.arr, self.fenwick = nums, [0] * (self.n + 1)
        
        # contruct the fenwick/bit 
        for i in range(self.n):
            k = i + 1
            while k <= self.n:
                self.fenwick[k] += nums[i]
                k += (k & -k)
        
        
    def update(self, index: int, val: int) -> None:
        
        diff, self.arr[index] = val - self.arr[index], val
        index += 1
        
        while index <= self.n:
            self.fenwick[index] += diff
            index += (index & -index)
            

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        right = right + 1
        
        while right:
            res += self.fenwick[right]
            right -= (right & -right)
            
        while left:
            res -= self.fenwick[left]
            left -= (left & -left)
            
        return res
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)