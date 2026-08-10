class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewelsDict = set()
        numJewels = 0

        for c in jewels:
            jewelsDict.add(c)

        for c in stones:
            if c in jewelsDict:
                numJewels += 1

        return numJewels