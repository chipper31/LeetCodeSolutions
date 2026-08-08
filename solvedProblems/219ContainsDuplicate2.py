class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        numsDict = {}

        for i, num in enumerate(nums):
            if num in numsDict:
                if i - numsDict[num] <= k:
                    return True
                else:
                    numsDict[num] = i
            else:
                numsDict[num] = i

        return False