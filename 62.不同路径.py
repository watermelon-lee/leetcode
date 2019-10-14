"""
@File    : 62.不同路径.py
@Time    : 2019-09-20 16:30
@Author  : Wade
@Software: PyCharm
"""

import copy
class Solution:
    # dfs 超时
    # dirction=[[1,0],[0,1]]
    # count=0
    # def uniquePaths(self,m,n):
    #     self.count=0
    #     map=[[0 for i in range(m)] for j in range(n)]
    #     startx,starty=0,0
    #     self.dfs(startx,starty,map)
    #     return self.count
    #
    #
    # def dfs(self,startx,starty,map):
    #     if startx==len(map)-1 and starty==len(map[0])-1:
    #         self.count+=1
    #         return
    #     map1 = copy.deepcopy(map)
    #     for k,v in enumerate(self.dirction):
    #         if startx+v[0]>=0 and starty+v[1]>=0 and startx+v[0]<len(map1) and starty+v[1]<len(map1[0]) and not map1[startx+v[0]][starty+v[1]]:
    #             new_startx=startx+v[0]
    #             new_starty=starty+v[1]
    #             map1[new_startx][new_starty]=1
    #             self.dfs(new_startx,new_starty,map1)

    def uniquePaths(self, m, n):
        map = [[0 for i in range(m)] for j in range(n)]
        for i in range(len(map)):
            map[i][0]=1
        for i in range(len(map[0])):
            map[0][i]=1

        for i in range(1,len(map)):
            for j in range(1,len(map[0])):
                map[i][j]=map[i-1][j]+map[i][j-1]
        return map[len(map)-1][len(map[0])-1]

s=Solution()
print(s.uniquePaths(10,10))

