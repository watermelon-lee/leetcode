"""
@File    : 32.最长有效括号.py
@Time    : 2019-12-15 09:31
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


# 类型 动态规划/栈

# 思路
# 使用dp数组保存以第i个元素结尾的有效括号长
# 若s【i】==），s【i-1】==（，那么这两个可以匹配。然后在加上i-1之前的有效长度，就是以i结尾的有效长度
# 即dp[i]=dp[i-2]+2

# 若s【i】==），s【i-1】==），那么只需要s[i-dp[i-1]-1]=='(' ，就可以组成有效括号，如'((()))'。
# 此时，dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2




class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp=[0 for _ in range(len(s))]
        if not s:
            return 0

        for i in range(1,len(s)):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i]=dp[i-2]+2
                elif s[i-1]==')':
                    if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                        dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
        return max(dp)


S=Solution()

print(S.longestValidParentheses("(()))())("))

