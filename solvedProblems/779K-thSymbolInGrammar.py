class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        memo = {}
        self.helper(self, n, k, memo)

        return (memo[n,k])

    def helper(self, n, k, memo):

        # base case
        if n == 1 and k == 1:
            memo[n, k] = 0
            return memo[n, k]

        if (n, k) in memo:
            return memo[n, k]

        if k % 2:   # k is odd
            memo[n, k] = self.helper(self, n-1, -(k//-2), memo)
        else:   # k is even
            if self.helper(self, n-1, -(k//-2), memo):
                memo[n, k] = 0
            else:
                memo[n, k] = 1

        return memo[n, k]


print(Solution.kthGrammar(Solution, 2, 2))