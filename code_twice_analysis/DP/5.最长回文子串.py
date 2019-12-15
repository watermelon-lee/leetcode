"""
@File    : 5.最长回文子串.py
@Time    : 2019-12-11 21:34
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""

# 类型 动态规划

#dp[i][j]=true代表i到j为回文

# if s[i]=s[j] dp[i][j]=dp[i+1][j-1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[0 for _ in range(len(s))]for _ in range(len(s))]

        start,length=0,0
        for j in range(len(s)):
            for i in range(0,j+1): # i从0到j遍历
                if s[i]==s[j]:
                    if j-i<2:# 长度为1或者2，必是回文
                        dp[i][j]=1
                        if j-i+1>length:
                            start=i
                            length=j-i+1
                    else:
                        dp[i][j]=dp[i+1][j-1]
                        if dp[i][j] and j-i+1>length:
                            start=i
                            length=j-i+1

        return s[start:start+length]

S=Solution()
print(S.longestPalindrome("aaaa"))
