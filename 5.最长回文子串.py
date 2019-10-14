#给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

class Solution(object):

    def check(self, s):
        return s == s[::-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = 0
        begin = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.check(s[i:j + 1]):
                    if (j - i + 1 > length):
                        length = j - i + 1
                        begin = i

        return s[begin:begin + length]

#         length=0
#         begin=0
#         dp=[]
#         for i in range(len(s)):
#             dp.append([])
#             for j in range(len(s)):
#                 dp[i].append(False)

#         if len(s)==1:
#             return s
#         for j in range(len(s)):
#             for i in range(0,j+1):
#                 if s[i]==s[j]:
#                     if j-i<2:
#                         dp[i][j]=True
#                     else:
#                         dp[i][j]=dp[i+1][j-1]
#                 else:
#                     dp[i][j]=False
#                 if dp[i][j] and j-i+1>length:
#                     length=j-i+1
#                     begin=i
#         return s[begin:begin+length]


