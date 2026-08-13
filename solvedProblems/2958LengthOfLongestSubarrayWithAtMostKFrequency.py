class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:

        subArrayDict = {}
        ri = 0
        li = 0
        maxSubLen = 0
        subLen = 0

        while True:
            if ri >= len(nums):
                break
            if nums[ri] in subArrayDict:
                subArrayDict[nums[ri]] += 1
            else:
                subArrayDict[nums[ri]] = 1
            subLen += 1
            while subArrayDict[nums[ri]] > k:
                subArrayDict[nums[li]] -= 1
                li += 1
                subLen -= 1
            if subLen > maxSubLen:
                maxSubLen = subLen
            ri += 1

        return maxSubLen

print(Solution.maxSubarrayLength(Solution, [1,4,4,3], 1))