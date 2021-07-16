# solution1 sort and compare with time complexity O(n^2)

def anagram_checking(s1: str, s2: str) -> bool:

    # take the string to the list
    a1List = list(s1)
    a2List = list(s2)

    # sort the list ascending
    a1List.sort()
    a2List.sort()

    # take position and the boolean variable
    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a1List[pos] == a2List[pos]:
            pos += 1
        else:
            matches = False
    return matches


if __name__ == '__main__':
    s1, s2 = 'heart', 'earth'
    func_call = anagram_checking(s1,s2)
    expected_result = True
    assert expected_result == func_call, func_call
    print(func_call)

    s1, s2 = 'python', 'typhon'
    func_call = anagram_checking(s1, s2)
    expected_result = True
    assert expected_result == func_call, func_call
    print(func_call)

    s1, s2 = 'arman', 'german'
    func_call = anagram_checking(s1, s2)
    expected_result = False
    assert expected_result == func_call, func_call
    print(func_call)





