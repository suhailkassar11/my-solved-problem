class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        cur=prev=0
        for i in range(n):
            cur+=i*nums[i]
            prev+=nums[i]
        ans=cur
        for  i in range(1,n):
            cur-=n*nums[n-i]
            cur+=prev
            ans=max(ans,cur)
        return ans
        