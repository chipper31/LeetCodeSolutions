class Solution:
    def intToRoman(self, num: int) -> str:

        if num - 1000 >= 0:
            return "M" + self.intToRoman(num-1000)
        elif num - 900 >= 0:
            return "CM" + self.intToRoman(num-900)
        elif num -500 >= 0:
            return "D" + self.intToRoman(num-500)
        elif num - 400 >= 0:
            return "CD" + self.intToRoman(num-400)
        elif num - 100 >= 0:
            return "C" + self.intToRoman(num-100)
        elif num - 90 >= 0:
            return "XC" + self.intToRoman(num-90)
        elif num - 50 >= 0:
            return "L" + self.intToRoman(num-50)
        elif num - 40 >= 0:
            return "XL" + self.intToRoman(num-40)
        elif num - 10 >= 0:
            return "X" + self.intToRoman(num-10)
        elif num - 9 >= 0:
            return "IX" + self.intToRoman(num-9)
        elif num - 5 >= 0:
            return "V" + self.intToRoman(num-5)
        elif num - 4 >= 0:
            return "IV" + self.intToRoman(num-4)
        elif num - 1 >= 0:
            return "I" + self.intToRoman(num-1)
        else:
            return ""

print(Solution.intToRoman(Solution, 3749))