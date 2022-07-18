class Solution:
    def integerReplacement(self, n: int) -> int:
        cout=0
        while n>1:
            cout+=1
            if n%2==0:
                n=n//2
                
            else:
                temp=((n-1)//2)%2
                if temp==0 or n==3:
                    n=n-1
                else:
                    n=n+1
        return cout