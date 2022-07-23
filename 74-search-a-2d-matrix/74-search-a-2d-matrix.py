class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        flag=0
        for i in range(m):
            for j in range(n):
                if target<=matrix[i][-1]:
                    if target==matrix[i][j]:
                        flag=1
                else:
                    break
        return bool(flag)