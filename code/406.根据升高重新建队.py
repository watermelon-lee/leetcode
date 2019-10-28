"""
@File    : 406.根据升高重新建队.py
@Time    : 2019-10-28 10:13
@Author  : 李浩然
@Software: PyCharm
@Email: 1901210423@pku.edu.cn
"""

from typing import List
import functools
class Solution:
    def sorted_key(self,x,y):
        if x[0]>y[0]:
            return 1
        if x[0]<y[0]:
            return -1
        else:
            if x[1]>y[1]:
                return -1
            else:
                return 1

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 按照身高降序，位置升序排列,然后以此选择位置插入
        people_down=sorted(people,key=functools.cmp_to_key(self.sorted_key),reverse=True)
        # x = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        # sorted(x, key=lambda x: x[0], reverse=True)
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]

        reRankList=[]
        for i in people_down:
            reRankList.insert(i[1],i)

        return reRankList

s=Solution()
print(s.reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]))
