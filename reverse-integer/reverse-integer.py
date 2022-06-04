class Solution:
    def reverse(self, x: int) -> int:
        regex = "^0+(?!$)"
        mina = -2**31  
        maxa = 2**31 - 1  

        if x==0 :
            return 0
        
        if x < 0:
            out = -int(re.sub(regex, "", str(x*-1)[::-1]))
            if out not in range(mina,maxa):
                return 0
            else :
                return out
        else:
            out=int(re.sub(regex, "", str(x)[::-1]))
            if out not in range(mina,maxa):
                return 0
            else :
                return out