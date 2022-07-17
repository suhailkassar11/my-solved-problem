class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=1
        res=0
        while j<len(nums):
            
            res+=min(nums[i],nums[j])
            
            i=j+1
            j=j+2
        return res