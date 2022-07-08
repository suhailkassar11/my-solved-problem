class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=nums[0]
        ma=ans
        mi=ans
        for i in range(1,len(nums)):
            if nums[i]<0:
                ma,mi=mi,ma
    
            ma=max(nums[i],ma*nums[i])
            mi=min(nums[i],mi*nums[i])
            ans=max(ans,ma)
        return ans