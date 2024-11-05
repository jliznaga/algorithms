from dataclasses import dataclass, field
from collections import deque


@dataclass
class Tree:
    x: int = 0
    l: "Tree" = None
    r: "Tree" = None

    def __init__(self, raw_tree: tuple):
        self.x = raw_tree[0]
        self.l = Tree(raw_tree[1]) if raw_tree[1] is not None else None
        self.r = Tree(raw_tree[2]) if raw_tree[2] is not None else None

    def __repr__(self) -> str:
        return f"({self.x}, {self.l}, {self.r})"


tree = Tree(
    (1, (2, (5, (3, None, None), None), (9, None, None)), (7, (4, None, None), None))
)


# def solution(T, digits=[]):
#     node = T
#     count = 0
#     digits.append(node.x)

#     if len(digits) == 3:
#         digits.clear()
#         return 1

#     if node.l is None and node.r is None:
#         return 0

#     if node.l:
#         count += solution(node.l, digits)

#     if node.r:
#         count += solution(node.r, digits)

#     return count


def solution(T, digits=None):
    if digits is None:
        digits = []

    digits.append(T.x)
    count = 0

    if len(digits) == 3:
        count += 1
        digits.pop(0)

    if T.l is not None:
        count += solution(T.l, digits.copy())
    if T.r is not None:
        count += solution(T.r, digits.copy())

    return count


print(solution(tree))
