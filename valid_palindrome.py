"""
Approach: Two Pointer
Status: Accepted
131 / 131 test cases passed.
Runtime: 120 ms
Memory Usage: 14.3 MB
Problem link:
Time complexity: O(n)
space complexity: O(n)
"""


def valid_palindrome(s: str) -> bool:
    result = [x.lower() for x in s if x.isalnum()]

    start = 0
    end = len(result) - 1
    while start < end:

        if result[start] != result[end]:
            return False
        start += 1
        end -= 1

    return True


if __name__ == '__main__':
    s = 'I amd a boy, sHe is , a git'
    func_call = valid_palindrome(s)
    expected_result =  False
    assert expected_result == func_call, func_call
    print(func_call)

    s = 'MaDam'
    func_call = valid_palindrome(s)
    expected_result = True
    assert expected_result == func_call, func_call
    print(func_call)

    s = 'tenET'
    func_call = valid_palindrome(s)
    expected_result = True
    assert expected_result == func_call, func_call
    print(func_call)