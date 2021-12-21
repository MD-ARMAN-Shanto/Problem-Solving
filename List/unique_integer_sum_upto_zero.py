"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
"""
from typing import List


def sumZero(n: int) -> List[int]:
    result = []

    if n % 2 != 0:
        result.append(0)

    for i in range(1, n):
        if len(result) == n:
            break
        result.append(i)
        result.append(-i)

    return result


if __name__ == "__main__":
    n = 5
    func_call = sumZero(n)
    expected_result = [0, 1, -1, 2, -2]
    assert expected_result == func_call, func_call
    print(func_call)

    n = 3
    func_call = sumZero(n)
    expected_result = [0, 1, -1]
    assert expected_result == func_call, func_call
    print(func_call)

    n = 1
    func_call = sumZero(n)
    expected_result = [0]
    assert expected_result == func_call, func_call
    print(func_call)


