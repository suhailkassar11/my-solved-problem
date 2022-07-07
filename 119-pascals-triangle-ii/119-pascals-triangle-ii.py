class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=1
        lst=[1]
        for i in range(rowIndex):
            res*=(rowIndex-i)
            res//=(i+1)
            lst.append(res)
        return lst
        