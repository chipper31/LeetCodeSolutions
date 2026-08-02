class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:

        maxWealth = 0

        for i in range(0, len(accounts)):
            currentWealth = 0
            for j in range(0, len(accounts[i])):
                currentWealth += accounts[i][j]

            if currentWealth > maxWealth:
                maxWealth = currentWealth

        return maxWealth

print(Solution.maximumWealth(Solution, [[1,5],[7,3],[3,5]]))