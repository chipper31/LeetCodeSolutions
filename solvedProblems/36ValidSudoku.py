class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        boardDict = set()

        #row check
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in boardDict:
                    return False
                boardDict.add(board[i][j])
            boardDict.clear()

        #column check
        for i in range(0,9):
            for j in range(0,9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in boardDict:
                    return False
                boardDict.add(board[j][i])
            boardDict.clear()

        #3x3 box check
        for i in range(0,9,3):
            for j in range(0,9,3):
                for a in range(i,i+3):
                    for b in range(j,j+3):
                        if board[a][b] == '.':
                            continue
                        if board[a][b] in boardDict:
                            return False
                        boardDict.add(board[a][b])
                boardDict.clear()

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