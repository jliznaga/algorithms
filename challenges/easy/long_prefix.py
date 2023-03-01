from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        i = 1
        while i < len(strs):
            prefix = ""
            for a, b in zip(strs[i - 1], strs[i]):
                if a == b:
                    prefix += a
                else:
                    break
            i += 1

            if i > 0 and len(prefix) < len(common_prefix):
                common_prefix = prefix

        return common_prefix


obj = Solution()
# print(obj.longestCommonPrefix(["flower", "flight", "flow"]))
print(obj.longestCommonPrefix(["asfdlfower", "terflrtigrtht", "ertflerow"]))
