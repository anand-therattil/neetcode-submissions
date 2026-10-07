class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        r = 9
        c = 9
        seen_row = [set() for _ in range(r)]
        seen_col = [set() for _ in range(c)]
        seen_square = [set() for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j]==".":
                    continue
                if board[i][j] not in seen_row[i]:
                    seen_row[i].add(board[i][j])
                else:
                    return False
        
        for i in range(c):
            for j in range(r):
                if board[j][i]==".":
                    continue
                if board[j][i] not in seen_col[i]:
                    seen_col[i].add(board[j][i])
                else:
                    return False

        for i in range(r):
            for j in range(c):
                if board[i][j]==".":
                    continue
                if board[i][j] not in seen_square[(i//3)*3+ j//3]:
                     seen_square[(i//3)*3+ j//3].add(board[i][j])
                else:
                    return False
        return True
        