# Length Of Last Word in a String

def lengthOfLastWord(s: str) -> int:
    count = 0
    x = s.strip()

    for i in range(len(x)):
        if x[i] == " ":
            count = 0
        else:
            count += 1
    return count


# test cases

if __name__ == '__main__':
    string = 'hello world'
    expected_ans = 5
    final_result = lengthOfLastWord(string)
    assert expected_ans == final_result, final_result
    print(final_result)

    string = ''
    expected_ans = 0
    final_result = lengthOfLastWord(string)
    assert expected_ans == final_result, final_result
    print(final_result)

    string = 'hello world welcome to arman programming'
    expected_ans = 11
    final_result = lengthOfLastWord(string)
    assert expected_ans == final_result, final_result
    print(final_result)