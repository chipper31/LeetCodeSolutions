class Solution:
    def maxArea(self, height: list[int]) -> int:
        areaMax = 0
        listLen = len(height)
        lc = 0
        rc = listLen-1
        leftPost = (height[lc], lc)
        rightPost = (height[rc], rc)

        while leftPost[1] < rightPost[1]:
            if leftPost[0] < rightPost[0]:
                newArea = leftPost[0] * (rightPost[1] - leftPost[1])
                lc += 1
                leftPost = (height[lc], lc)
            else:
                newArea = rightPost[0] * (rightPost[1] - leftPost[1])
                rc -= 1
                rightPost = (height[rc], rc)
            if newArea > areaMax:
                areaMax = newArea
            
        return areaMax

print(Solution.maxArea(Solution, [1,2,4,3]))