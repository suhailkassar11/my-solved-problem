class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        if len(nums)==0:
            return []
        dp=[[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(dp[j])>=len(dp[i]):
                    dp[i]=dp[j]+[nums[i]]
        max_subset=0
        res=0
        for subset in dp:
            if len(subset)>max_subset:
                max_subset=len(subset)
                res=subset
        return res
        