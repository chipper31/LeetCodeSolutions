class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        rSum = []

        rSum.append(nums[0])

        for i in range(1, len(nums)):
            rSum.append(rSum[i-1] + nums[i])

        return rSum

print(Solution.runningSum(Solution, [1,2,3,4]))