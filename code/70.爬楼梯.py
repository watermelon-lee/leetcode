class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        # runtime error
        one,two=1,2
        for i in range(3,n+1):
            sum=one+two
            one=two
            two=sum
        return sum




s=Solution()
print(s.climbStairs(4))