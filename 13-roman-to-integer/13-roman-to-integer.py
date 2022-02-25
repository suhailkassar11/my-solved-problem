class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        for i in range(0,len(s)-1):
            if d[s[i]]<d[s[i+1]]:
                res=res-d[s[i]]
            else:
                res=res+d[s[i]]
        return res+d[s[-1]]