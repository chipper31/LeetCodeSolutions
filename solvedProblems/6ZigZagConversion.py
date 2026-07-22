class Solution:
    def convert(self, s: str, numRows: int) -> str:
       
        sLength = len(s)
        outString = []

        for i in range(0,numRows):
            currRow = 0
            if numRows == 1:
                increment = 0
            else:
                increment = 1
            for j in range(0,sLength):
                print(str(currRow) + " "+ str(j))
                if currRow == i:
                    outString.append(s[j])
                if currRow == 0:
                    increment = 1
                elif (currRow == numRows - 1):
                    increment = -1
                if numRows == 1:
                    increment = 0
                currRow += increment

        return "".join(outString)
    
print(Solution.convert(Solution, "PAYPALISHIRING", 1))