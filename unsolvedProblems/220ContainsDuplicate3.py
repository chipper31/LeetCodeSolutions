class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:

        # takes too long for worst case scenario
        for i in range(0,len(nums)):
            for j in range(i+1, indexDiff+i+1):
                if j >= len(nums):
                    break
                if abs(nums[i]-nums[j]) <= valueDiff:
                    return True

        return False