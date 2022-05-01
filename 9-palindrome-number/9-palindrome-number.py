class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        res=0
        while x>0:
            r=x%10
            res=res*10+r
            x=x//10
        if temp==res:
            return "true"
        