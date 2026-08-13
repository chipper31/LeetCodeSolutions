class Solution:
    def missingInteger(self, nums: list[int]) -> int:

        rightIndex = 0
        numsSet = set()
        numsSet.add(nums[0])
        sum = nums[0]

        for i in range(1,len(nums)):
            if nums[i-1] == nums[i] - 1:
                rightIndex = i
                sum += nums[i]
            else:
                break

        for i in range(rightIndex + 1, len(nums)):
            numsSet.add(nums[i])

        while sum in numsSet:
            sum += 1
        
        return int(sum)

print(Solution.missingInteger(Solution, [3,4,5,1,12,14,13]))