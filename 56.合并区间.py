"""
@File    : 56.合并区间.py
@Time    : 2019-09-19 21:55
@Author  : Wade
@Software: PyCharm
"""

class Solution:
    def merge(self,intervals):
        intervals.sort()
        ans=[]
        for interval in intervals:
            if not ans or ans[-1][1]<interval[0]:
                ans.append(interval)
            else:
                ans[-1][1]=max(ans[-1][1],interval[1])
        return ans

s=Solution()
a=[[1,3],[2,6],[8,10],[15,18]]
print(s.merge(a))