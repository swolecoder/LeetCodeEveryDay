class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(set)
        c = defaultdict(set)
        rc = defaultdict(set)



        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]

                if val == ".": continue

                if val in r[i] or val in c[j] or val in rc[(i//3,j//3)]:
                    return False


                r[i].add(val)
                c[j].add(val)


                rc[(i//3,j//3)].add(val)  

        return True      