class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        outList = []
        intSet = set()

        for num in nums1:
            intSet.add(num)

        for num in nums2:
            if num in intSet:
                outList.append(num)
                intSet.remove(num)

        return outList