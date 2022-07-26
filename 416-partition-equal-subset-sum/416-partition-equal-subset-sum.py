class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N=len(nums)
        total_sum=sum(nums)
        if total_sum%2!=0:
            return False
        half_sum=total_sum//2
        dp=[[False for i in range(half_sum+1)] for j in range(N+1)]
        #dp = [[False for i in range(half_sum+1)] for j in range(N+1)
        dp[0][0]=True
        for i in range(1,N+1):
            n=nums[i-1]
            for j in range(half_sum+1):
                if j>=n:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-n]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[N][half_sum]