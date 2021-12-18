"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Good Ding"
Output: "dooG gniD"
"""


def reverseWords(s: str) -> str:
    li = s.split(' ')

    result = []

    for word in li:
        result.append(word[::-1])

    return ' '.join(result)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    func_call = reverseWords(s)
    expected_result = "s'teL ekat edoCteeL tsetnoc"
    assert expected_result == func_call, func_call
    print(func_call)

    s = "Good Ding"
    func_call = reverseWords(s)
    expected_result = "dooG gniD"
    assert expected_result == func_call, func_call
    print(func_call)
