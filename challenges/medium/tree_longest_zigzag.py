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
    (
        5,
        (3, (20, (6, None, None), None), None),
        (10, (1, None, None), (15, (30, None, (9, None, None)), (8, None, None))),
    )
)


# def solution(T: Tree):
#     node = T
#     direction = None
#     count = 0
#     while node is not None and (node.l is not None or node.r is not None):
#         if node.l and node.r:
#             if node.l.x > node.r.x:
#                 if direction is not None and direction != "L":
#                     count += 1
#                 direction = "L"
#                 node = node.l
#             else:
#                 if direction is not None and direction != "R":
#                     count += 1
#                 direction = "R"
#                 node = node.r
#         elif node.l:
#             if direction is not None and direction != "L":
#                 count += 1
#             direction = "L"
#             node = node.l
#         elif node.r:
#             if direction is not None and direction != "R":
#                 count += 1
#             direction = "R"
#             node = node.r
#         else:
#             break

#     return count


def solution(T: Tree, direction=None):
    node = T
    count = 0
    if node.l is None and node.r is None:
        return 0

    if node.l and node.r:
        if node.l.x > node.r.x:
            if direction is not None and direction != "L":
                count += 1
            count += solution(node.l, "L")
        elif node.r:
            if direction is not None and direction != "R":
                count += 1
            count += solution(node.r, "R")
    elif node.l:
        if direction is not None and direction != "L":
            count += 1
        count += solution(node.l, "L")
    else:
        if direction is not None and direction != "R":
            count += 1
        count += solution(node.r, "R")

    return count


print(solution(tree))
