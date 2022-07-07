class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(0,n+1):
            bit=bin(i).replace("0b", "")
            s=str(bit)
            t=s.count("1")
            ans.append(t)
        return ans
           
