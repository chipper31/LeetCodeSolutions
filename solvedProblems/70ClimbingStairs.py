class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)
        
        return self.climbStairsRecur(self, n, memo)

    def climbStairsRecur(self, n, memo):

        #base case
        if n < 1:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        #if value is memoized
        if memo[n] != -1:
            return memo[n]

        #memoizing the value
        memo[n] = self.climbStairsRecur(self, n-1, memo) + \
                  self.climbStairsRecur(self, n-2, memo)

        return memo[n]

print(Solution.climbStairs(Solution, 5))