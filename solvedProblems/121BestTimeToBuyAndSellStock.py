class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minCost = prices[0]
        bestProfit = 0

        for i in range(1, len(prices)):
            newProfit = prices[i] - minCost
            if newProfit > bestProfit:
                bestProfit = newProfit
            if prices[i] < minCost:
                minCost = prices[i]

        return bestProfit

print(Solution.maxProfit(Solution, [7,6,4,3,1]))
        