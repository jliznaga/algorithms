from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        res = []
        for a in nums:
            if len(res) % 2 == 0 or a != res[-1]:
                res.append(a)
        return len(nums) - (len(res) - len(res) % 2)

    def minDeletionx(self, nums: List[int]) -> int:
        deletions = 0
        i = 0
        while i < len(nums) - deletions - 1:
            if (i - deletions) % 2 == 0 and nums[i - deletions] == nums[i + 1 - deletions]:
                deletions += 1
                i += 1
            i += 1

        if (len(nums) - deletions) % 2 != 0:
            deletions += 1

        return deletions


obj = Solution()
# print(obj.minDeletion([1, 1, 2, 3, 5]))
print(obj.minDeletion([1, 1, 2, 2, 3, 3]))
# print(obj.minDeletion([5, 1, 5, 4, 8, 1, 4, 4, 1, 9, 2, 2, 2, 5, 1]))
# print(obj.minDeletion([3, 2, 7, 6, 2, 5, 8, 1, 8, 4, 2, 2, 6, 8, 7, 7, 8]))
# print(obj.minDeletion(
#     [2, 6, 2, 5, 8, 9, 7, 2, 2, 5, 6, 2, 2, 0, 6, 8, 7, 3, 9, 2, 1, 1, 3, 2, 6, 2, 4, 6, 5, 8, 4, 8, 7, 0, 4, 8, 7, 8,
#      4, 1, 1, 4, 0, 1, 5, 7, 7, 5, 9, 7, 5, 5, 8, 6, 4, 3, 6, 5, 1, 6, 7, 6, 9, 9, 6, 8, 6, 0, 9, 5, 6, 7, 6, 9, 5, 5,
#      7, 3, 0, 0, 5, 5, 4, 8, 3, 9, 3, 4, 1, 7, 9, 3, 1, 8, 8, 9, 1, 6, 0, 0]))
