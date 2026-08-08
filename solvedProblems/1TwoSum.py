class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        numsDict = {}

        for i in range(0,len(nums)):
            if nums[i] in numsDict:
                if target - nums[i] == nums[i]:
                    return [numsDict[nums[i]], i]
            numsDict[nums[i]] = i

        for i in range(0,len(nums)):
            if (target - nums[i] in numsDict) and \
                target / 2 != nums[i]:
                return [numsDict[nums[i]], numsDict[target-nums[i]]]
            
        return []

print(Solution.twoSum(Solution, [2,7,11,15], 9))
print(Solution.twoSum(Solution, [3,2,4], 6))
print(Solution.twoSum(Solution, [3,3], 6))