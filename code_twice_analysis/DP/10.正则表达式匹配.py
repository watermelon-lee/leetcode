"""
@File    : 10.正则表达式匹配.py
@Time    : 2019-12-16 08:26
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""

# 类型 字符串
# 技巧 回溯（还可用动态规划）

# 思路
# 首先查看第一个是否匹配
# 若p第二位为'*'
# 第一个匹配，然后s往后一位，p仍然是p
# 第一个不匹配，s保持不变，p用*匹配0个第一个字,p变成p[2:]

# p第二个不为'*'
# 第二个不为"*',则第一个匹配的话都从第二个位置开始比较


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:# p匹配完毕之后，s也要没有
            return not s
        # 先看第一个是否匹配
        if s: # S不为空
            first_match=True if s[0]==p[0] or p[0]=='.' else False
        else:
            first_match=False

        if len(p)>=2 and p[1]=='*':
            # 第一个匹配，然后s往后一位，p仍然是p
            # 第一个不匹配，s保持不变，p用*匹配0个第一个字,p变成p[2:]
            return first_match and self.isMatch(s[1:],p[:]) or self.isMatch(s[:],p[2:])
        else:
            # 第二个不为"*',则第一个匹配的话都从第二个位置开始比较
            return first_match and self.isMatch(s[1:],p[1:])



S=Solution()
s='aa'
p='a*'
print(S.isMatch(s,p))