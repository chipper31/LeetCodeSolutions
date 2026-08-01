class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        outList = []

        for i in range(0, numRows):
            if i == 0:
                outList.append([1])
            elif i == 1:
                outList.append([1,1])
            else:
                rowList = []
                for j in range(0, i + 1):
                    if j == 0:
                        rowList.append(1)
                    elif j == i:
                        rowList.append(1)
                    else:
                        rowList.append(outList[i-1][j]+outList[i-1][j-1])
                outList.append(rowList)

        return outList

print(Solution.generate(Solution, 6))