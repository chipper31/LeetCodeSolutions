class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:

        listOneDict = {}
        commonWordDict = {}
        minIndex = 2000
        outList = []

        for i, word in enumerate(list1):
            listOneDict[word] = i

        for i, word in enumerate(list2):
            if word in listOneDict:
                commonWordDict[word] = listOneDict[word] + i
                if listOneDict[word] + i < minIndex:
                    minIndex = listOneDict[word] + i

        for word in commonWordDict:
            if commonWordDict[word] == minIndex:
                outList.append(word)

        return outList