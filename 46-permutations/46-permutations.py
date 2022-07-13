class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtracking(res):
            
            if len(res) == len(nums):
                ans.append(list(res))
                return

            for i in  nums:
                if i not in res:
                    res.append(i)
                    backtracking(res)
                    res.pop()
        backtracking([])
        return ans