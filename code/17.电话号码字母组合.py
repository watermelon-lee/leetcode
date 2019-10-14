# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

class Solution(object):

    char = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'nmo', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}


    def getChar(self,digits,index,list,string):

        if index == len(digits)-1:
            for i in self.char.get(int(digits[index])):
                list.append(string+i)
            return list
        else:
            i=int(digits[index])
            for j in str(self.char.get(i)):
                self.getChar(digits,index+1,list,string+j)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        if len(digits) == 0:
            return ans
        self.getChar(digits,0,ans,'')
        return ans


