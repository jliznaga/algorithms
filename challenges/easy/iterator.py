from itertools import combinations


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.nodes = []
        self.head = None

        comb = list(combinations(characters, combinationLength))
        node = Node(data=''.join(comb.pop(0)))
        self.head = node

        for c in comb:
            node.next = Node(data=''.join(c))
            node = node.next

    def next(self) -> str:
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data

    def hasNext(self) -> bool:
        return self.head is not None


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator('abc', 2)
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())