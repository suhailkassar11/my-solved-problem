class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                nums.append(matrix[i][j])
        nums.sort()
        return nums[k-1]