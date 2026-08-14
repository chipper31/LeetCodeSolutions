class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        SSDict = {}
        ri = 0
        li = 0
        maxLen = 0
        currLen = 0

        while ri < len(s):
            if s[ri] in SSDict:
                SSDict[s[ri]] +=1
            else:
                SSDict[s[ri]] = 1
            currLen += 1
            while SSDict[s[ri]] > 2:
                SSDict[s[li]] -= 1
                li += 1
                currLen -= 1
            ri += 1
            if currLen > maxLen:
                maxLen = currLen

        return maxLen