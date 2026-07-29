class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        if n == 0:  #base case
            return("")
        else:   #recursive case
            return(["("+self.generateParenthesis(self,n-1)])

print(Solution.generateParenthesis(Solution, 3))
