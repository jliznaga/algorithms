from typing import List
from itertools import combinations


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        comb = combinations(stones, 2)
        cont = 0
        res = 0
        for ([x1, y1], [x2, y2]) in comb:
            cont += 1
            if x1 == x2 or y1 == y2:
                res += 1
        print(f"CONT: {cont}")
        return res


obj = Solution()

print(obj.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
print(obj.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
print(obj.removeStones([[0, 0]]))

# print(obj.removeStones([[0, 1], [1, 0], [1, 1]]))
