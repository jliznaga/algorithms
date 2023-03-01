from typing import List
from itertools import combinations


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        for i in range(1, len(nums)):
            comb = combinations(nums, i)
            print(comb)


obj = Solution()
print(obj.countDistinct([2, 3, 3, 2, 2], 2, 2))
# print(obj.countDistinct([9, 29, 49, 50], "cbcd"))
