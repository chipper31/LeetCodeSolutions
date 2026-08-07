class Solution:
    def isHappy(self, n: int) -> bool:

        fastDigits = str(n)
        slowDigits = str(n)
        fastSum = 0
        slowSum = 0

        while True:
            for digit in fastDigits:
                fastSum = fastSum + int(digit)**2
            fastDigits = str(fastSum)
            fastSum = 0

            for digit in fastDigits:
                fastSum = fastSum + int(digit)**2
            fastDigits = str(fastSum)

            for digit in slowDigits:
                slowSum = slowSum + int(digit)**2
            slowDigits = str(slowSum)

            if fastSum == 1:
                return True
            if fastSum == slowSum:
                return False
            fastSum = 0
            slowSum = 0


print(Solution.isHappy(Solution, 19))