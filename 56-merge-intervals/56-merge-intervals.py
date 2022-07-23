class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack=[]
        stack.append(intervals[0])
        for i in intervals[1:]:
            if stack[-1][1]>=i[0] :
                if i[1]<=stack[-1][1]:
                    continue
                else:
                    stack[-1][1]=i[1]

            else:
                stack.append(i)
        return stack