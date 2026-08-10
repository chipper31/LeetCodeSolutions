class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seenLettersDict = {}
        firstIndex = 0
        maxSSlen = 0

        for i, num in enumerate(s):
            if num in seenLettersDict:
                if seenLettersDict[num] + 1 > firstIndex:
                    firstIndex = seenLettersDict[num] + 1
            seenLettersDict[num] = i

            currSSLen = i - firstIndex + 1
            if currSSLen > maxSSlen:
                maxSSlen = currSSLen

        return maxSSlen

print(Solution.lengthOfLongestSubstring(Solution, "ccbbcc"))