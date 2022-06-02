class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        mat=[]
        for i in range(len(matrix[0])):
            mat1=[]
            for j in range(len(matrix)):
                ele=matrix[j][i]
                mat1.append(ele)
            mat.append(mat1)
        return mat