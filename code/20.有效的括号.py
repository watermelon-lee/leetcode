# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i=='{' or i=='[' or i=='(':
                stack.append(i)
            else:
                if len(stack)!=0:
                    a=stack.pop()
                else:
                    return False
                if a=='(' and i!=')':
                    return False
                if a=='[' and i!=']':
                    return False
                if a=='{' and i!='}':
                    return False
        if len(stack)==0:
            return True
        else:
            return False