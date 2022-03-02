class Solution:
    def fib(self, n: int) -> int:
        lst=[0,1]
        num=0
        for i in range(1,n+1):
            num=lst[i]+lst[i-1]
            lst.append(num)
        if n>=1:
            return lst[n-1]+lst[n-2]
        else:
            return 0
            