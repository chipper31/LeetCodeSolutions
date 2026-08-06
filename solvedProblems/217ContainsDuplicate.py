class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        numsDict = set()

        for i in nums:
            if i in numsDict:
                return True
            numsDict.add(i)

        return False