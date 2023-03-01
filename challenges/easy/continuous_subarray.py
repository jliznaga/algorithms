import os
import psutil
from typing import List

from urllib3.connectionpool import xrange


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        summ = 0
        for i, n in enumerate(nums):
            if k != 0:
                summ = (summ + n) % k
            else:
                summ = n
            if summ not in dic:
                dic[summ] = i
            else:
                if i - dic[summ] >= 2:
                    return True
        return False

    def checkSubarraySumx(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {0: -1}
        summ = 0
        for i, n in enumerate(nums):
            if k != 0:
                summ = (summ + n) % k
            else:
                summ += n
            if summ not in dic:
                dic[summ] = i
            else:
                if i - dic[summ] >= 2:
                    return True
        return False


obj = Solution()
# print(obj.checkSubarraySum(
#     [405, 504, 203, 96, 43, 50, 214, 327, 120, 345, 33, 314, 377, 62, 431, 379, 114, 208, 106, 345, 391, 513, 9, 405,
#      452, 186, 295, 33, 423, 122, 355, 311, 192, 429, 320, 360, 85, 96, 32, 258, 407, 71, 436, 370, 365, 199, 443, 521,
#      262, 232, 355, 241, 250, 10, 258, 324, 335, 446, 474, 385, 74, 101, 111, 162, 349, 149, 51, 399, 371, 139, 199,
#      264, 118, 155, 134, 518, 388, 113, 520, 441, 384, 449, 14, 104, 267, 92, 477, 50, 505, 368, 466, 519, 105, 443, 31,
#      21, 485, 146, 115, 94], 337))

print(obj.checkSubarraySum(
    [23, 2, 4, 6, 7], 6))
