class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        outList = []
        digitsDict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        self.helper(self, digits, outList, "", 0, digitsDict)

        return outList

    def helper(self, digits, outList, outString, index, digitsDict):
        if index == len(digits) - 1: #base case, last digit
            for i in range(0, len(digitsDict[digits[index]])):
                outList.append(outString + digitsDict[digits[index]][i])
        else: #recursive case
            for i in range(0, len(digitsDict[digits[index]])):
                self.helper(self, 
                            digits, 
                            outList, 
                            outString + digitsDict[digits[index]][i],
                            index + 1,
                            digitsDict)

print(Solution.letterCombinations(Solution, "234"))