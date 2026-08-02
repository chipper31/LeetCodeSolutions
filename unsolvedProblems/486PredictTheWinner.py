class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:

        sumEven = 0
        sumOdd = 0

        # if there is an even number of numbers
        # player 1 has a winning strategy. See
        # P877 Stone Game for explanation
        if len(nums) % 2 == 0:
            return True

        #sum of even numbers
        for i in range(0,len(nums),2):
            sumEven += nums[i]
        
        #sum of odd numbers
        for i in range(1,len(nums),2):
            sumOdd += nums[i]

        if sumOdd > sumEven:
            return False

        if (sumEven - nums[0] > sumOdd + nums[0]) and (sumEven - nums[-1] > sumOdd + nums[-1]):
            return False


        return False

print(Solution.predictTheWinner(Solution, [1,5,2]))