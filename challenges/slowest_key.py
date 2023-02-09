from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        dic_max = {keysPressed[0]: releaseTimes[0]}
        for i, k in enumerate(releaseTimes):
            if i + 1 >= len(releaseTimes):
                break
            next_time = releaseTimes[i + 1] - k
            max_val = dic_max.get(next(iter(dic_max)))
            if next_time > max_val:
                dic_max.clear()
                dic_max[keysPressed[i + 1]] = next_time
            if next_time == max_val:
                dic_max[keysPressed[i + 1]] = next_time

        return max(dic_max.keys())



obj = Solution()
print(obj.slowestKey([12, 23, 36, 46, 62], "spuda"))
print(obj.slowestKey([9, 29, 49, 50], "cbcd"))
