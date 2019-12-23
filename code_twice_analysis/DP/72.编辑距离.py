"""
@File    : 72.编辑距离.py
@Time    : 2019-12-19 09:21
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""

# 类型 动态规划

# 思路
# 我们使用dp[i][j]表示word1前i位转换为word2前j位的最小编辑距离
# 总共有三种变法
# 第一个单词的前i位变为前二个单词的前j-1位，然后插入一个字符（dp[i][j-1]+1)
# 第一个单词的前i-1位变为第二个单词的前j位，然后删除第i个字符（dp[i-1][j]+1)
# 第一个单次前i-1位变为第二个单词前j-1位，然后将第i个变为第j个，分情况考虑word1[i]==word2[j]是否成立

# 注意，我们初始化的dp[0][0]代表第一个长度位0变为第二个长度为0。dp[0][0]=0

# 对于的word1[0]即第一个单词的第一位，在dp中的下标是从1开始的





class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m,n=len(word1),len(word2)
        dp=[[0 for _ in range(n+1)] for _ in range(m+1)]


        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        return dp[m][n]