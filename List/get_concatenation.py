from typing import List


def getConcatenation(nums: List[int]) -> List[int]:

    # process 1
    return nums + nums

    # process 2
    return nums * 2

    # process 3
    nums1 = nums.copy()
    res = nums1 + nums
    return res