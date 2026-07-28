class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        boardDict = {}

        for i in range(0,9):
            for j in range(0,9):
                boardDict[(i,j)] = board[i][j]

        # horizontal line check
        for i in range(0,9):
            for j in range(0,9):
                currCell = boardDict[(i,j)]
                if currCell == ".":
                    continue
                for k in range(j + 1,9):
                    if currCell == boardDict[(i,k)]:
                        return False

        # vertical line check
        for i in range(0,9):
            for j in range(0,9):
                currCell = boardDict[(j,i)]
                if currCell == ".":
                    continue
                for k in range(j + 1,9):
                    if currCell == boardDict[(k,i)]:
                        return False

        # 3x3 box check        
        for i in range(0,9,3):  # cols of 3x3 boxes
            for j in range(0,9,3):  # rows of 3x3 boxes
                cellList = []
                for k in range(i,i+3):  
                    for a in range(j,j+3):
                        cellList.append(boardDict[(k,a)])
                for k in range(0,9):
                    currCell = cellList[k]
                    if currCell == ".":
                        continue
                    for a in range(k+1,9):
                        if currCell == cellList[a]:
                            return False

        return True

print(Solution.isValidSudoku(Solution,
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))