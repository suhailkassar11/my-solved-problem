class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n<=2:
            return 1
        else:
            a=0
            b=1
            c=1
            sume=0
            index=3
            while index<=n:
                sume=a+b+c
                index+=1
                a=b
                b=c
                c=sume
            return sume
        