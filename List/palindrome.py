# find out whether a number a palindrome or not

def palindrome(n: int) -> bool:

    if n < 0:
        return False

    palin_str = str(n)[::-1]
    palin_drome = int(palin_str)
    if palin_drome == n:
        return True


if __name__ == '__main__':
    number = 121
    func_call = palindrome(number)
    final_result = True
    assert final_result == func_call, final_result
    print(final_result)

    number = -121
    func_call = palindrome(number)
    final_result = False
    assert final_result == func_call, final_result
    print(final_result)

    number = 0
    func_call = palindrome(number)
    final_result = True
    assert final_result == func_call, final_result
    print(final_result)