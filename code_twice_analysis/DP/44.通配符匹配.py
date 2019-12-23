"""
@File    : 44.通配符匹配.py
@Time    : 2019-12-22 09:29
@Author  : LEE
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


# 类型 字符串
# 技巧 动态规划（递归超时）

# 首先，我们使用dp[i][j]表示都s前i个字符与p前j个字符是否匹配
# dp[0][0]=true表示两个0个字符可以匹配
# 初始化还需要看dp[0][j],即p的前j个能否匹配空字符
# 当p[j]='*'的时候，dp[0][j]=dp[0][j-1]即p[j]='*'置为空，然后看前j-1个能否匹配空字符

# s第i个和p的第j个匹配的时候，即s[i-1]=p[j-1] or p[j]='?
# dp[i][j]=dp[i-1][j-1]

# 当p的第j个为'*'的时候，p[j-1]='*
# 1 使用'*'号，，p[j-1]='*'可以匹配s[i-1]，此外，还可以匹配s[i-1]之前的字符，则dp[i][j]=dp[i-1][j]
# 2 不使用'*'号，p[j-1]='*'置为空，则dp[i][j]=dp[i][j-1]

# 最后返回dp[-1][-1]即可



class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # 超时 md
        # if not p: #p空了
        #     return len(s)==0 # s为空即为true
        # if s:
        #     first_match= True if s[0]==p[0] or p[0]=='?'or p[0]=='*' else False
        # else:
        #     first_match=False
        # if p[0]=='*':
        #     return first_match and (self.isMatch(s[1:],p[:]) or self.isMatch(s[1:],p[1:])) or self.isMatch(s[:],p[1:])
        # else:
        #     return first_match and self.isMatch(s[1:],p[1:])

        m,n=len(s),len(p)
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[0][0]=True
        for j in range(1,n+1):
            if p[j-1]=='*':
                dp[0][j]=dp[0][j-1]
            else:
                dp[0][j]=False

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                if p[j-1]=='*':
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]



S=Solution()

s='abbdbabababdba'
p='?*bbd*bab?bd*'

print(S.isMatch(s,p))

