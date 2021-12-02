"""
programmed by Md. Arman Hossain

approach -> first split the string into a list then slice and take the subarray to parameter k
then join the list to make it str again

"""



def truncate_sentence(s: str, k:int) -> str:

    # res = s.split(' ')[:k]
    # return ' '.join(res)
    #
    # or
    return ' '.split(list(s.split(' ')[:k]))


if __name__ == '__main__':
    s = 'ami tomake bhalo bashi'
    k = 3
    fc = truncate_sentence(s, k)
    expect_result = 'ami tomake bhalo'

