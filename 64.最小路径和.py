"""
@File    : 64.最小路径和.py
@Time    : 2019-09-21 08:49
@Author  : Wade
@Software: PyCharm
"""
import copy
class Solution:
    # rumtime error
    # dirction = [[1, 0], [0, 1]]
    # min=10000
    # def minPathSum(self,grid):
    #     self.grid = 0
    #     startx, starty = 0, 0
    #     map=[[0 for i in range(len(grid[0]))]for j in range(len(grid))]
    #     self.dfs(startx, starty, map,grid,grid[0][0])
    #     return self.min
    #
    # def dfs(self, startx, starty, map,grid,count):
    #     if startx == len(map) - 1 and starty == len(map[0]) - 1:
    #         if count<self.min:
    #             self.min=count
    #         return
    #     map1 = copy.deepcopy(map)
    #     for k, v in enumerate(self.dirction):
    #         if startx + v[0] >= 0 and starty + v[1] >= 0 and startx + v[0] < len(map1)\
    #                 and starty + v[1] < len(map1[0]) and not map1[startx + v[0]][starty + v[1]]:
    #             new_startx = startx + v[0]
    #             new_starty = starty + v[1]
    #             map1[new_startx][new_starty] = 1
    #             self.dfs(new_startx, new_starty, map1,grid,count+grid[new_startx][new_starty])
    def minPathSum(self, grid):
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        dp[0][0]=grid[0][0]
        for i in range(1, len(grid[0])):
            dp[0][i]= dp[0][i-1] + grid[0][i]
        for i in range(1,len(grid)):
            dp[i][0]= dp[i-1][0] + grid[i][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[len(grid) - 1][len(grid[0]) - 1]


s=Solution()
grid=[
  [1]
]
print(s.minPathSum(grid))