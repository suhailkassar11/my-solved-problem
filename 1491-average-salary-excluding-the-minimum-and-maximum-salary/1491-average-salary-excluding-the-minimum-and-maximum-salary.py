class Solution:
    def average(self, salary: List[int]) -> float:
        res=0
        salary.sort()
        n=len(salary)-2
        for i in range(1,len(salary)-1):
            res=salary[i]+res   
        return res/n
        