class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


obj = Solution()
print(obj.isPalindrome(10))
