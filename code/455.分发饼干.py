"""
@File    : 455.分发饼干.py
@Time    : 2019-10-28 10:46
@Author  : 李浩然
@Software: PyCharm
@Email: 1901210423@pku.edu.cn
"""

from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        continue_j=0
        count=0
        for i in range(len(g)):
            j=continue_j
            while j<len(s):
                if s[j]<g[i]:
                    continue_j = j
                    del s[j]
                else:
                    count+=1
                    del s[j]
                    continue_j = j
                    break
        return count

s=Solution()
print(s.findContentChildren([1,2,3,2,4,1,5,6,6,2,23,2], [1,1,6,8,9,9,4,3,23,2,2]))