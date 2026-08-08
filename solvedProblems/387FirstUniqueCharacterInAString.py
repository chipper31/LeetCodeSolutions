class Solution:
    def firstUniqChar(self, s: str) -> int:

        charDict = {}
        minIndex = 100001
        outIndex = -1

        #1st value is frequency, 2nd is index of first char
        for i,c in enumerate(s):
            if c in charDict:
                charDict[c][0] += 1
            else:
                charDict[c] = [1,i]

        for c in charDict:
            if charDict[c][0] == 1:
                if charDict[c][1] < minIndex:
                    minIndex = charDict[c][1]
                    outIndex = minIndex

        return outIndex