class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count1 = defaultdict(set)
        count2 = defaultdict(set)
        count3 = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in count1[i] or board[i][j] in count2[j] or board[i][j] in count3[(i//3, j//3)]:
                    return False
                
                count1[i].add(board[i][j])
                count2[j].add(board[i][j])
                count3[(i//3, j//3)].add(board[i][j])
        return True