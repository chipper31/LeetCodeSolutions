class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        outList = []
        strDict = {}
        #sorted_text = "".join(sorted(text))

        for s in strs:
            sSorted = "".join(sorted(s))
            if sSorted in strDict:
                strDict[sSorted].append(s)
            else:
                strDict[sSorted] = [s]

        for l in strDict:
            outList.append(strDict[l])

        return outList