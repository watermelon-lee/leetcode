class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # rows=[[] for i in range(9)]
        # lines=[[] for i in range(9)]
        # boxes=[[] for i in range(9)]
        #
        # for i in range(9):
        #     for j in range(9):
        #         box_index=(i//3)*3 + j//3
        #         num=board[i][j]
        #         if num!='.':
        #             if num not in rows[i] and num not in lines[j] and num not in boxes[box_index]:
        #                 rows[i].append(num)
        #                 lines[j].append(num)
        #                 boxes[box_index].append(num)
        #             else:
        #                 return False
        # return True

        rows = [{} for i in range(9)]
        lines = [{} for i in range(9)]
        boxes = [{} for i in range(9)]


        for i in range(9):
            for j in range(9):
                box_index = (i // 3) * 3 + j // 3
                num=board[i][j]
                if num!='.':
                    num = int(num)
                    rows[i][num]=rows[i].get(num,0)+1
                    lines[j][num]=lines[j].get(num,0)+1
                    boxes[box_index][num]=boxes[box_index].get(num,0)+1
                    if rows[i][num]>1 or boxes[box_index][num]>1 or lines[j][num]>1:
                        return False
        return True



# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
board = [[".","8","7","6","5","4","3","2","1"],
        ["2",".",".",".",".",".",".",".","."],
        ["3",".",".",".",".",".",".",".","."],
        ["4",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".",".","."],
        ["6",".",".",".",".",".",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        ["8",".",".",".",".",".",".",".","."],
        ["9",".",".",".",".",".",".",".","."]]
