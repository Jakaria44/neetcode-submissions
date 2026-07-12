class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    continue
                
                box = (i//3)*3 + j//3
                if num in rows[i] or num in cols[j] or num in sqrs[box]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                sqrs[box].add(num)
        return True