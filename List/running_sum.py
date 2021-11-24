"""
Prog: Md. Arman Hossain
site: Leetcode
Type: List
"""
from typing import List


def runningSum(nums: List[int]) -> List[int]:
    # res = [nums[i]*(nums[i]+1)/2 for i in range(len(nums)]
    res = []
    s = 0
    for i in range(len(nums)):
        s = s + nums[i]
        res.append(s)
    return res

if __name__ == '__main__':
    nums = [1,2,3,4]
    fc = runningSum(nums)
    expected_result = [1,3,6,10]
    assert expected_result == fc, fc
    print(fc)

    nums = [1,1,1,1,1]
    fc = runningSum(nums)
    expected_result = [1,2,3,4,5]
    assert expected_result == fc, fc
    print(fc)

    nums = [3,1,2,10,1]
    fc = runningSum(nums)
    expected_result = [3,4,6,16,17]
    assert expected_result == fc, fc
    print(fc)
