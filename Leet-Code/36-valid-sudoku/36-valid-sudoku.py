#풀이 1 (Bruteforce)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9): #가로 확인
            row = set([])
            for j in range(9):
                if board[i][j] != "." and board[i][j] in row:
                    return False
                row.add(board[i][j])

        for i in range(9): #세로 확인
            col = set([])
            for j in range(9):
                if board[j][i] != "." and board[j][i] in col:
                    return False
                col.add(board[j][i])

        for i in range(0,9,3): #3x3 확인
            for j in range(0,9,3):
                cube = set([])
                for k in range(i,i+3,1):
                    for l in range(j,j+3,1):
                        if board[k][l] != "." and board[k][l] in cube:
                            return False
                        cube.add(board[k][l])

        return True
