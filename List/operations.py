"""
Prog: Md. Arman Hossain
site: Leetcode
Type: List
"""
from typing import List


def finalValueAfterOperations(operations: List[str]) -> int:
    x = 0
    for op in operations:
        if op == '--X':
            x -= 1
        elif op == 'X--':
            x -= 1
        elif op == '++X':
            x += 1
        else:
            x += 1
    return x


if __name__ == '__main__':
    operations = ["--X", "X++", "X++"]
    fc = finalValueAfterOperations(operations)
    expected_result = 1
    assert expected_result == fc, fc
    print(fc)

    operations = ["X++", "++X", "--X", "X--"]
    fc = finalValueAfterOperations(operations)
    expected_result = 0
    assert expected_result == fc, fc
    print(fc)