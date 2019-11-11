"""
@File    : 51.N皇后.py
@Time    : 2019-11-11 10:09
@Author  : 李浩然
@Software: PyCharm
@Email: 1901210423@pku.edu.cn
"""

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
            # 注意，count中加入map，但是之后map变化，count中的加入的mao也会变化，我们需要加入copy
            count.append(map.copy())
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



    def solveNQueens(self, n: int) -> List[List[str]]:
        map=[-1 for _ in range(n)]
        count=[]
        row=1
        if n==0:
            return 0
        for column in range(n):
            map[0]=column
            self.NQueen(map,count,row,n)
            map[0]=-1

        ans=[]
        for i in range(len(count)):
            cube=[]
            for j in range(n):
                line=''
                for k in range(n):
                    if k!=count[i][j]:
                        line=line+'.'
                    else:
                        line=line+'Q'
                cube.append(line)
            ans.append(cube)
        return ans

s=Solution()
print(s.solveNQueens(4))