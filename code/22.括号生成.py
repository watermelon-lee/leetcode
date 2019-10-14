# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#


class Solution:

    def kuohao(self,inside, n, string,list1):
        if n==0:
            while inside:
                inside-=1
                string+=')'
            list1.append(string)
        if inside>0 and n>0:
            self.kuohao(inside-1,n,string+')',list1)
            self.kuohao(inside+1,n-1,string+'(',list1)
        if inside==0 and n>0:
            string+='('
            n-=1
            inside+=1
            self.kuohao(inside,n,string,list1)

    def generateParenthesis(self, n: int):
        list1 = []
        self.kuohao(0,n,'',list1)
        return list1

