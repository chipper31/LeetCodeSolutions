class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:

        outList = []
        numsDict = {}
        min = 101
        max = 0

        for i in range(0, len(nums)):
            if nums[i] > max:
                max = nums[i]
            if nums[i] < min:
                min = nums[i]
            numsDict[nums[i]] = nums[i]

        diff = max - min

        if diff + 1 == len(nums):
            return outList

        for i in range(min + 1,max):
            if not (i in numsDict):
                outList.append(i)

        return outList

print(Solution.findMissingElements(Solution,[1,4]))