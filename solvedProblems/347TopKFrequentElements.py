class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        numsDict = {}
        kNums = []
        outList = []

        for x in nums:
            if x in numsDict:
                numsDict[x] += 1
            else:
                numsDict[x] = 1

        for i in range(0,k):
            kNums.append((0,0))

        for x in numsDict:
            if numsDict[x] > kNums[0][1]:
                kNums[0] = (x, numsDict[x])
                for i in range(0,k-1):
                    if kNums[i][1] > kNums[i+1][1]:
                        temp = kNums[i+1]
                        kNums[i+1] = kNums[i]
                        kNums[i]=temp
                    else:
                        break

        for i in range(0,k):
            outList.append(kNums[i][0])

        return outList

print(Solution.topKFrequent(Solution, [1,1,1,2,2,3], 2))