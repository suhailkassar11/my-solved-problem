class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res= [[0 for i in range(n)]for j in range(n)]
        top = 0
        left = 0
        bottom = n-1
        right= n-1
        val=1
        while (top <= bottom and left <= right):
            for i in range(left,right+1):
                res[top][i]=val
                val+=1
            top += 1
            for i in range(top,bottom+1):
                res[i][right]=val
                val+=1
            right -= 1
            if (top <=bottom):
                for i in range(right,left-1,-1):
                    res[bottom][i]=val
                    val+=1
                bottom -= 1
            if (left <= right):
                for i in range(bottom,top-1,-1):
                    res[i][left]=val
                    val+=1
                left += 1
        return res
        