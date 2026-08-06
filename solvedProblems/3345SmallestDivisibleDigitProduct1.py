class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        for i in range(0, t):
            nstr = str(n+i)
            product = 1
            for j in range(0, len(nstr)):
                product = product * int(nstr[j])
            if product % t == 0:
                return n+i

        return -1