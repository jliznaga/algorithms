class Solution:
    def romanToInt(self, s: str) -> int:
        letters = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000
                   }
        total = 0
        for index, letter in enumerate(s):
            if letter not in letters.keys():
                return
            number = letters[letter]
            last_letter = letters[s[index - 1]]
            if index - 1 >= 0 and number > last_letter:
                total += (number - (last_letter * 2))
            else:
                total += number
        return total


obj = Solution()
print(obj.romanToInt("LVIII"))
print(obj.romanToInt("MCMXCIV"))
print(obj.romanToInt("IV"))
