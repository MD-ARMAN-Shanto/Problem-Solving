# adding two binary stirngs , return also as a binary string


def add_binary(a: str, b: str) -> str:
    #         con_a = int(a, 2) # 2nd argument defines the number system
    #         print(con_a)
    #         con_b = int(b, 2)
    #         sumi = con_a + con_b

    #         return f"{sumi:b}"

    return f"{(int(a, 2) + int(b, 2)):b}"


if __name__ == '__main__':
    a = '11'
    b = '1'
    functon_call = add_binary(a, b)
    expected_result = '100'
    assert expected_result == functon_call, functon_call
    print(functon_call)