class Solution:
    def fib(self, n: int) -> int:
        # n1=0
        # n2=1
        # count=1
        # if n==0:
        #     return 0
        # elif n==1:
        #     return 1
        # else:
        #     while count<n:
        #         nth = n1 + n2
        #         n1 = n2
        #         n2 = nth
        #         count += 1
        # return nth
        if  n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib(n-2)+self.fib(n-1)
        