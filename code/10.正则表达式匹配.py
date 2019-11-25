"""
@File    : 10.正则表达式匹配.py
@Time    : 2019-11-25 10:00
@Author  : 李浩然
@Software: PyCharm
@Email: 1901210423@pku.edu.cn
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s #当p匹配完了，s也要没有了

        first_match=bool(s) and p[0] in [s[0],'.']#s还有，p【0】=s【0】或者p【0】='.'匹配任何字符

        if len(p)>=2 and p[1]=='*':
            return first_match and self.isMatch(s[1:],p) or self.isMatch(s,p[2:])
        # 第一个匹配，然后从s【1】开始。 第一个不匹配，用*消除p【0】。
        else: #第二个不为*，则第一个必须匹配
            return first_match and self.isMatch(s[1:],p[1:])


s = "mississippi"
p = "mis*is*ip.."
S=Solution()
print(S.isMatch(s,p))