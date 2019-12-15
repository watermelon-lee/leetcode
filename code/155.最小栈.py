"""
@File    : 155.最小栈.py
@Time    : 2019-12-02 16:13
@Author  : 李浩然
@Software: PyCharm
@Email: leehaoran@pku.edu.cn
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stock=[]
        self.min=[]

    def push(self, x: int) -> None:
        self.stock.append(x)
        if len(self.min)==0:
            self.min.append(x)
        else:
            if x<=self.min[-1]:
                self.min.append(x)

    def pop(self) -> None:
        num=self.stock.pop()
        if num==self.min[-1]:
            self.min=self.min[:-1]

    def top(self) -> int:
        return self.stock[-1]

    def getMin(self) -> int:
        if  self.min:
            return self.min[-1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack();
print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-3))
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())