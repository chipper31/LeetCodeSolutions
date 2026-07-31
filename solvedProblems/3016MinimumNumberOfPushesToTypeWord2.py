class Solution:
    def minimumPushes(self, word: str) -> int:

        letterFrequencies={}
        letterFreqList = []
        totalKeyPresses = 0

        # getting the frequency for each letters occurence in word
        for i in range(0,len(word)):
            if word[i] in letterFrequencies:
                letterFrequencies[word[i]] = letterFrequencies[word[i]] + 1
            else:
                letterFrequencies[word[i]] = 1

        letterFreqList.append((word[0], letterFrequencies[word[0]]))
        letterFrequencies.pop(word[0])

        # insertion sort to sort frequencies into an array
        i = 1
        for x in letterFrequencies:
            insertIndex = i
            currentValue = (x, letterFrequencies[x])
            for j in range(i-1, -1, -1):
                if letterFreqList[j][1] < currentValue[1]:
                    insertIndex = j
            letterFreqList.insert(insertIndex, currentValue)
            i += 1

        for i in range(0, len(letterFreqList)):
            if i <= 7:
                totalKeyPresses += letterFreqList[i][1]
            elif i <= 15:
                totalKeyPresses += 2 * letterFreqList[i][1]
            elif i <= 23:
                totalKeyPresses += 3 * letterFreqList[i][1]
            else:
                totalKeyPresses += 4 * letterFreqList[i][1]

        return totalKeyPresses

print(Solution.minimumPushes(Solution, "aabbccddeeffgghhiiiiii"))