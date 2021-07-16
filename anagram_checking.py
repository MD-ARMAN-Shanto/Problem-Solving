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


# solution 2 count and compare with time complexity O(n)

def anagram_checking(s1, s2):
    # take 26 size array counter for counting letters with 0
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOk = True

    while j < 26 and stillOk:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOk = False

    return stillOk


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



