# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        open_chars = ['(', '{', '[']
        close_chars = [')', '}', ']']
        stack = []
        for item in s:
            if item in open_chars:
                stack.append(item)
            elif item in close_chars:
                index = close_chars.index(item)
                if len(stack) == 0 or open_chars[index] != stack.pop():
                    return False
        
        return True if len(stack) == 0 else False

obj = Solution()

# print(obj.isValid("()"))
# print(obj.isValid("()[]{}"))
print(obj.isValid("{{[]"))
