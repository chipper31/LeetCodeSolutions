class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:

        n = len(nums1)
        dict12 = {}
        dict34 = {}
        numTuples = 0

        for i in range(0,n):
            for j in range(0,n):
                if nums1[i]+nums2[j] in dict12:
                    dict12[nums1[i]+nums2[j]] += 1
                else:
                    dict12[nums1[i]+nums2[j]] = 1

        for i in range(0,n):
            for j in range(0,n):
                if nums3[i]+nums4[j] in dict34:
                    dict34[nums3[i]+nums4[j]] += 1
                else:
                    dict34[nums3[i]+nums4[j]] = 1

        for num in dict12:
            if (num * (-1)) in dict34:
                numTuples += dict12[num] * dict34[num*(-1)]

        return numTuples

print(Solution.fourSumCount(Solution, [1,2], [-2,-1], [-1,2], [0,2]))