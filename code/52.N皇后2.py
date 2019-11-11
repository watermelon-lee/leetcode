"""
@File    : 52.N皇后2.py
@Time    : 2019-11-11 09:08
@Author  : 李浩然
@Software: PyCharm
@Email: 1901210423@pku.edu.cn
"""


from typing import List
class Solution:

    def NQueen(self,map,count,row,n):
        if n==row:
            count[0]+=1
            return

        def valid(map,row,column):
            if column not in map and column<len(map):
                for i in range(row):
                    if abs(map[i]-column)==abs(row-i):
                        return False
                return True
            return False

        for column in range(n):
            if valid(map, row, column):
                map[row] = column
                self.NQueen(map, count, row+1,n)
                map[row] = -1



    def totalNQueens(self, n: int) -> int:
        map=[-1 for _ in range(n)]
        count=[0]
        row=1
        if n==0:
            return 0
        for column in range(n):
            map[0]=column
            self.NQueen(map,count,row,n)
            map[0]=-1
        return count[0]


s=Solution()
print(s.totalNQueens(0))