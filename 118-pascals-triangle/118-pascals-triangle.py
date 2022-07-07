class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        while len(output) < numRows:
            temp = [1, 1]
            [temp.insert(idx, output[-1][idx - 1] + output[-1][idx]) for idx in range(1, len(output[-1]))]
            output.append(temp)
        return output