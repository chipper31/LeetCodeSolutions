class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        mergedArray = []
        nums1Counter = 0
        nums2Counter = 0
        m = len(nums1)
        n = len(nums2)
        median = -1.0
        loop = True

        if m == 0:
            loop = False
            mergedArray = nums2
        elif n == 0:
            loop = False
            mergedArray = nums1

        while loop:
            if nums1[nums1Counter] <= nums2[nums2Counter]:
                mergedArray.append(nums1[nums1Counter])
                nums1Counter += 1
                if nums1Counter >= m:
                    for i in range(nums2Counter, n):
                        mergedArray.append(nums2[nums2Counter])
                        nums2Counter += 1
                    loop = False
            else:
                mergedArray.append(nums2[nums2Counter])
                nums2Counter += 1
                if nums2Counter >= n:
                    for i in range(nums1Counter, m):
                        mergedArray.append(nums1[nums1Counter])
                        nums1Counter += 1
                    loop = False

        mergedArrayLength = len(mergedArray)
        mergedArrayMedian = mergedArrayLength//2

        if mergedArrayLength % 2 == 1:
            median = mergedArray[mergedArrayMedian]
        else:
            median = (mergedArray[mergedArrayMedian] + mergedArray[mergedArrayMedian - 1]) / 2

        return median

print(Solution.findMedianSortedArrays(Solution, [], [1]))