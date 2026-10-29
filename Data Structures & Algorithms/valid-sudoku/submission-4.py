class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cnt1 = defaultdict(set)
        cnt2 = defaultdict(set)
        cnt3 = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in cnt1[r] or board[r][c] in cnt2[c] or board[r][c] in cnt3[(r//3, c//3)]:
                    return False
                
                cnt1[r].add(board[r][c])
                cnt2[c].add(board[r][c])
                cnt3[(r//3, c//3)].add(board[r][c])
        return True
