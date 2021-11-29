"""
design an ordered item into the list using class methods
"""
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.list = [None] * 5
        self.pointer = 0

    def insert(self, idKey, value: str) -> List[None]:
        self.list[idKey - 1] = value

        result = []

        while self.pointer < len(self.list) and self.list[self.pointer] is not None:
            result.append(self.list[self.pointer])
            self.pointer += 1
        # print(result)
        return result


os = OrderedStream(5)
os.insert(3, 'ccccc')
os.insert(1, 'aaaaa')
os.insert(2, "bbbbb")
os.insert(5, "eeeee")
os.insert(1, 'ddddd')


